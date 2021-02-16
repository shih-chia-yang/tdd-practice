using System;

namespace money
{
    public class Dollar:Money
    {
        public Dollar(int amount):base(amount,"USD")
        {

        }
        public Dollar(int amount,string currency):base(amount,currency)
        {

        }

        public override Money times(int multiplier)
        {
            return new Dollar(amount * multiplier);
        }
    }
}