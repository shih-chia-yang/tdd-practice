using System;
using System.Collections.Generic;
using src.money.Seed;

namespace money
{
    public class Money:ValueObject,IExpression
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

        public static Money CreateMoney(int amount, string currency) => new Money(amount, currency);
        public IExpression Times(int multiplier)
        {
            return new Money(Amount * multiplier, Currency);
        }

        public string GetCurrency() => Currency;

        public override IEnumerable<object> GetEquality()
        {
            yield return Currency;
            yield return Amount;
        }

        public IExpression Plus(IExpression added)
        {
            return new Sum(this,added);
        }

        public Money reduce(string to)
        {
            return this;
        }

        public Money reduce(Exchange exchange, string to)
        {
            return new Money(Amount / exchange.Rate(this.Currency,to), to);
        }
    }
}