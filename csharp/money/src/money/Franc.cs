using System;

namespace money
{
    public class Franc:Money
    {
        public Franc(int amount)
        {
            _amount = amount;
        }

        public Franc times(int multiplier)
        {
            return new Franc(amount * multiplier);
        }
    }
}