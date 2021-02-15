using System;

namespace money
{
    public class Dollar
    {
        public int amount{ get; private set; }
        public Dollar(int _amount)
        {
            amount = _amount;
        }

        public Dollar times(int multiplier)
        {
            return new Dollar(amount * multiplier);
        }
    }
}
