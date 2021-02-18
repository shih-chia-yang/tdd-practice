using System.Collections;
using System;
namespace money
{
    public interface IExchange
    {
        Money Dollar(int amount);

        Money Franc(int amount);

    }

    public class Exchange : Entity, IExchange
    {
        private Hashtable rates = new Hashtable();
        public Money Dollar(int amount)=> new Money(amount,"USD");

        public Money Franc(int amount)=> new Money(amount,"CHF");

        public Money reduce (IExpression source,string to)=>source.reduce(this,to);

        public Exchange()
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

        public Money reduce(Exchange exchange, string to)
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