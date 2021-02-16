using System;
namespace money
{
    public interface IExchange
    {
        Money Dollar(int amount);

        Money Franc(int amount);

    }

    public class Exchange : IExchange
    {
        public Money Dollar(int amount)=> new Money(amount,"USD");

        public Money Franc(int amount)=> new Money(amount,"CHF");

        public Money reduce (IExpression source,string to)=>source.reduce(this,to);

        public int Rate (string source,string to)
        {
            return (source=="CHF" && to =="USD")? 2 : 1;
        }
        public void AddRate(string source,string to,int rate)
        {

        }
    }

    public class Sum:IExpression
    {
        public Money Augend{ get; private set;}
        public Money Added{ get; private set; }

        public Sum(Money augend,Money added)
        {
            Augend = augend;
            Added = added;
        }

        public Money reduce (string to)
        {
            return new Money(Augend.amount + Added.amount, to);
        }

        public Money reduce(Exchange exchange, string to)
        {
            return new Money(Augend.amount + Added.amount, to);
        }
    }
}