using System.Net.NetworkInformation;
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
            return new Dollar(amount);
        }

        public Money Franc(int amount)
        {
            return new Franc(amount);
        }
    }
}