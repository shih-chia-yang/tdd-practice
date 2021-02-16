using System;


namespace money
{
    public interface IMoney
    {
        int amount { get; }

        string Currency{ get;}

        Money times(int multiplier);

    }
    public class Money:IMoney
    {
        public int amount => _amount;
        protected int _amount{ get; set;}

        public string Currency => _currency;

        protected string _currency{ get; set;}

        public Money(int amount,string currency)
        {
            _amount = amount;
            _currency = currency;
        }

        public Money times(int multiplier)
        {
            return new Money(amount * multiplier, Currency);
        }

        public string GetCurrency() => Currency;

        public bool Equals(object obj)
        {
            if (obj == null)
            {
                return false;
            }
            Money money = (Money)obj;
            if(this.Currency!=money.Currency)
            {
                return false;
            }
            return this._amount == money.amount;
        }
    }
}