using System;

namespace money
{
    public class Franc:Money
    {
        //  public int amount{ get; private set; }
        public Franc(int amount)
        {
            _amount = amount;
        }

        public Franc times(int multiplier)
        {
            return new Franc(amount * multiplier);
        }

        // public override bool Equals(object obj)
        // {
        //     if (obj == null || GetType() != obj.GetType())
        //     {
        //         return false;
        //     }
        //     Money money = (Franc)obj;
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