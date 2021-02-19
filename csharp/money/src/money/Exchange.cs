using System.Security.Cryptography.X509Certificates;
using System.ComponentModel.DataAnnotations.Schema;
using System.Collections;
using System;
using System.Collections.Generic;
using System.Linq;

namespace money
{
    public interface IExchangeService
    {
        int Rate(string source, string to);
        void AddRate(string source, string to, int rate);

        ICurrencyExpression Sum(string to,params ICurrencyExpression[] addeds);

        ICurrencyExpression Times(ICurrencyExpression source, int multiplier);

        ICurrencyExpression Exchange(ICurrencyExpression source, string to);
    }
    public class ExchangeService : IExchangeService
    {
        private Hashtable rates { get; set; }

        public ExchangeService()
        {
            rates= new Hashtable();
        }

        public int Rate (string source,string to)
        {
            if(source.Equals(to))return 1;
            Pair targetPair =new Pair(source, to);
            int rate = (int)rates[targetPair];
            return rate;
        }
        public void AddRate(string source,string to,int rate)
        {
            rates.Add(new Pair(source, to), rate);
        }

        public ICurrencyExpression Sum (string to,params ICurrencyExpression[] addeds)
        {
            if(addeds is null || addeds.Count()==0)
            {
                throw new ArgumentNullException("addeds can't be null or empty", nameof(Sum));
            }
            if(addeds.Select(x=>x.Currency).Distinct().Count()>1 && string.IsNullOrEmpty(to))
            {
                throw new ArgumentNullException("addeds contains diff currency,mush be assign currency", nameof(Sum));
            }
            string currency = string.IsNullOrEmpty(to)?addeds[0].Currency:to;
            int amount=addeds.Select(x =>Exchange(x,currency).Amount).Aggregate((x, y)=>x + y);
            return new Money(amount,to);
        }

        public ICurrencyExpression Exchange(ICurrencyExpression source, string to)
        {
            if(source is null)
            {
                throw new ArgumentNullException("Exchange must be have Money", nameof(Exchange));
            }
            if(string.IsNullOrEmpty(to))
            {
                throw new ArgumentNullException("Exchange must assign Currency", nameof(Exchange));
            }
            return new Money(source.Amount / Rate(source.Currency, to), to);
        }

        public ICurrencyExpression Times(ICurrencyExpression source, int multiplier)
        {
            if(source is null)
            {
                throw new ArgumentNullException("Multiplicand can not be null", nameof(Times));
            }
            return new Money(source.Amount * multiplier, source.Currency);
        }
    }

    public class Sum:IOperatorExpression
    {
        public IOperatorExpression Augend{ get; private set;}
        public IOperatorExpression Added{ get; private set; }

        public Sum(IOperatorExpression augend,IOperatorExpression added)
        {
            Augend = augend;
            Added = added;
        }

        public Money reduce(IExchangeService exchange, string to)
        {
            return new Money(Augend.reduce(exchange, to).Amount 
            + Added.reduce(exchange, to).Amount,to);
        }

        public IOperatorExpression Times(int multiplier)
        {
            return new Sum(Augend.Times(multiplier), Added.Times(multiplier));
        }
    }
}