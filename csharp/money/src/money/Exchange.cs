using System.ComponentModel.DataAnnotations.Schema;
using System.Collections;
using System;
namespace money
{
    public interface IExchangeService
    {
        int Rate(string source, string to);
        void AddRate(string source, string to, int rate);
        Money reduce(IExpression source, string to);

        Money Plus(params Money[] addeds);
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

        public Money Plus (params Money[] addeds)
        {
            if(addeds is null || addeds.Length==0)
            {
                throw new ArgumentNullException("addeds can't be null or empty", nameof(Plus));
            }
            int amount = 0;
            string currency = addeds[0].Currency;
            foreach(Money money in addeds)
            {
                amount += money.Amount;
            }
            return new Money(amount, currency);
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