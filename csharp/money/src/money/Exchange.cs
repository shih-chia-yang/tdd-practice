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
        Money reduce(IExpression source, string to);

        Money Sum(string to,params Money[] addeds);

        Money Times(Money source, int multiplier);

        Money Exchange(Money source, string to);
    }
    public class ExchangeService : IExchangeService
    {
        private Hashtable rates = new Hashtable();

        public Money reduce (IExpression source,string to)=>source.reduce(this,to);

        public ExchangeService()
        {
            
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

        public Money Sum (string to,params Money[] addeds)
        {
            if(addeds is null || addeds.Count()==0)
            {
                throw new ArgumentNullException("addeds can't be null or empty", nameof(Sum));
            }
            int amount=addeds.Select(x =>Exchange(x,to).Amount).Aggregate((x, y)=>x + y);
            return new Money(amount,to);
        }

        public Money Exchange(Money source, string to)
        {
            return new Money(source.Amount / Rate(source.Currency, to), to);
        }

        public Money Times(Money source, int multiplier)
        {
            return new Money(source.Amount * multiplier, source.Currency);
        }
    }

    public class Sum:IExpression
    {
        public IExpression Augend{ get; private set;}
        public IExpression Added{ get; private set; }

        public Sum(IExpression augend,IExpression added)
        {
            Augend = augend;
            Added = added;
        }

        public Money reduce(IExchangeService exchange, string to)
        {
            return new Money(Augend.reduce(exchange, to).Amount 
            + Added.reduce(exchange, to).Amount,to);
        }

        public IExpression Plus(IExpression added)
        {
            return new Sum(this,added);
        }

        public IExpression Times(int multiplier)
        {
            return new Sum(Augend.Times(multiplier), Added.Times(multiplier));
        }
    }
}