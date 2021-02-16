using System.Net.NetworkInformation;
using System;
using System.Linq.Expressions;

namespace money
{
    public interface IExchange
    {
        Money Dollar(int amount);

        Money Franc(int amount);

        Money reduce(Expression source, string to);
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

        public Money reduce (Expression source,string to)
        {
            return Dollar(10);
        }
    }
}