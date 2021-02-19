using System;
using System.Collections.Generic;
using src.money.Seed;

namespace money
{
    public class Money:ValueObject
    {
        public int Amount => _amount;
        protected int _amount{ get; set;}

        public string Currency => _currency;

        protected string _currency{ get; set;}

        public Money(int amount,string currency)
        {
            _amount = amount;
            _currency = currency;
        }
        
        public Money Times(int multiplier)
        {
            return new Money(Amount * multiplier, Currency);
        }

        public string GetCurrency() => Currency;

        public override IEnumerable<object> GetEquality()
        {
            yield return Currency;
            yield return Amount;
        }
    }
}