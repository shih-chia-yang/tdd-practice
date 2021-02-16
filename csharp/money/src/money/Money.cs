using System.Linq.Expressions;
using System;

namespace money
{
    public interface IMoney
    {
        int amount { get; }

        string Currency{ get;}

        Money times(int multiplier);

        Expression Plus(Money added);

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

        public override bool Equals(object obj)
        {
            return this.Equals(obj as Money);
        }

        public bool Equals(Money obj)
        {
            if (obj == null)
            {
                return false;
            }
            if(this.Currency!=obj.Currency)
            {
                return false;
            }
            return this._amount == obj.amount;
        }

        public Expression Plus(Money added)
        {
            return new Sum(this,added);
        }
    }
}