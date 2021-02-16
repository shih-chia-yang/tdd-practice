using System;

namespace money
{
    public class Franc:Money
    {
        public Franc(int amount):base(amount,"CHF")
        {

        }
        public Franc(int amount,string currency):base(amount,currency)
        {

        }

        public override Money times(int multiplier)
        {
            return new Franc(amount * multiplier);
        }
    }
}