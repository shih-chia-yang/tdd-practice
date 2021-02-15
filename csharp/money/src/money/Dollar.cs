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

        public override bool Equals(object obj)
        {
            if (obj == null || GetType() != obj.GetType())
            {
                return false;
            }
            if(this.amount==((Dollar)obj).amount)
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
