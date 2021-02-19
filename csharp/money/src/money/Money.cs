using System.Runtime.InteropServices;
using System;
using System.Collections.Generic;
using src.money.Seed;

namespace money
{
    public interface ICurrencyExpression
    {
        int Amount { get; }
        string Currency {get;}
}
    public class Money:ValueObject,ICurrencyExpression
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
    
        public string GetCurrency() => Currency;

        public override IEnumerable<object> GetEquality()
        {
            yield return Currency;
            yield return Amount;
        }
    }
}