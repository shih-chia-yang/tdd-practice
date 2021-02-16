using System;


namespace money
{
    public interface IMoney
    {
        int amount { get; }
        Money times(int multiplier);

    }
    public abstract class Money
    {
        public int amount => _amount;
        protected int _amount{ get; set;}

        protected string Currency{ get; set;}

        public Money(int amount,string currency)
        {
            _amount = amount;
            Currency = currency;
        }

        public abstract Money times(int multiplier);

        public string GetCurrency() => Currency;

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