using System;


namespace money
{
    public abstract class Money
    {
        public int amount => _amount;
        protected int _amount{ get; set;}

        public abstract Money times(int multiplier);

        public bool Equals(object obj)
        {
            if (obj == null || GetType() != obj.GetType())
            {
                return false;
            }
            Money money = (Money)obj;
            return this._amount == money.amount;
        }
    }
}