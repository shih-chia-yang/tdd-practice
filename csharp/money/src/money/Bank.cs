using System;
namespace money
{
    public class Bank:Entity
    {
        public static Money Dollar(int amount) => new Money(amount, "USD");
        public static Money Franc(int amount) => new Money(amount, "CHF");
    }
}