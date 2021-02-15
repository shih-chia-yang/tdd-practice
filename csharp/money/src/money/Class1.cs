using System;

namespace money
{
    public class Dollar
    {
        public int amount{ get; set; }
        public Dollar(int _amount)
        {
            amount = _amount;
        }

        public Dollar times(int multiplier)
        {
            return new Dollar(amount * multiplier);
        }

        public bool Equals(object obj)
        {
            // //
            // // See the full list of guidelines at
            // //   http://go.microsoft.com/fwlink/?LinkID=85237
            // // and also the guidance for operator== at
            // //   http://go.microsoft.com/fwlink/?LinkId=85238
            // //

            // if (obj == null || GetType() != obj.GetType())
            // {
            //     return false;
            // }

            // // TODO: write your implementation of Equals() here
            // throw new System.NotImplementedException();
            // return base.Equals (obj);
            return true;
        }
        
        // public override int GetHashCode()
        // {
        //     // TODO: write your implementation of GetHashCode() here
        //     // throw new System.NotImplementedException();
        //     return base.GetHashCode();
        // }
    }
}
