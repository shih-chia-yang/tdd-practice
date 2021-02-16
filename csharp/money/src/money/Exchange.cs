using System.Collections.Generic;
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
            Sum sum = (Sum)source;
            return new Money(sum.Augend.amount + sum.Added.amount, to);
        }
    }

    public class Sum:Expression
    {
        public Money Augend{ get; private set;}
        public Money Added{ get; private set; }

        public Sum(Money augend,Money added)
        {
            Augend = augend;
            Added = added;
        }
    }
}