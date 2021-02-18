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

        Money Plus(string to,params Money[] addeds);
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

        public Money Plus (string to,params Money[] addeds)
        {
            if(addeds is null || addeds.Count()==0)
            {
                throw new ArgumentNullException("addeds can't be null or empty", nameof(Plus));
            }
            int amount=addeds.Select(x =>x.Amount/Rate(x.Currency,to)).Aggregate((x, y)=>x + y);
            return new Money(amount,to);
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