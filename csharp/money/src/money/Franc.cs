using System;

namespace money
{
    public class Franc
    {
         public int amount{ get; private set; }
        public Franc(int _amount)
        {
            amount = _amount;
        }

        public Franc times(int multiplier)
        {
            return new Franc(amount * multiplier);
        }

        public override bool Equals(object obj)
        {
            if (obj == null || GetType() != obj.GetType())
            {
                return false;
            }
            if(this.amount==((Franc)obj).amount)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        
        // public override int GetHashCode()
        // {
        //     // TODO: write your implementation of GetHashCode() here
        //     // throw new System.NotImplementedException();
        //     return base.GetHashCode();
        // }
    }
}