using System;

namespace money
{
    public class Franc:Money
    {
        public Franc(int amount)
        {
            _amount = amount;
        }

        public Money times(int multiplier)
        {
            return new Franc(amount * multiplier);
        }
    }
}