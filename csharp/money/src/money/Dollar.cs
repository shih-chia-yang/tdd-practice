using System;

namespace money
{
    public class Dollar:Money
    {
        public Dollar(int amount)
        {
            _amount = amount;
        }

        public Money times(int multiplier)
        {
            return new Dollar(amount * multiplier);
        }
    }
}