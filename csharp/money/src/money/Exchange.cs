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
        public Money Dollar(int amount)
        {
            return new Money(amount,"USD");
        }

        public Money Franc(int amount)
        {
            return new Money(amount,"CHF");
        }

        public Money reduce (IExpression source,string to)
        {
            return source.reduce(to);
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
    }
}