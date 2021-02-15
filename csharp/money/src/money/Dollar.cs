using System;

namespace money
{
    public class Dollar:Money
    {
        // public int amount{ get; private set; }
        public Dollar(int amount)
        {
            _amount = amount;
        }

        public Dollar times(int multiplier)
        {
            return new Dollar(amount * multiplier);
        }

        // public override bool Equals(object obj)
        // {
        //     if (obj == null || GetType() != obj.GetType())
        //     {
        //         return false;
        //     }
        //     Money money = (Dollar)obj;
        //     return this.amount == money.amount;
        // }
        
        // public override int GetHashCode()
        // {
        //     // TODO: write your implementation of GetHashCode() here
        //     // throw new System.NotImplementedException();
        //     return base.GetHashCode();
        // }
    }
}
