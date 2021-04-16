using System.Security.Cryptography.X509Certificates;
using System.Reflection.Metadata;
using System.Linq.Expressions;
using System;
using money;

namespace moneytest
{
    public class FakeDataBuilder
    {
        public static Money MakeDollar(int amount)=> new Money(amount, "USD");

        public static Money MakeFranc(int amount) => new Money(amount, "CHF");

    }
}