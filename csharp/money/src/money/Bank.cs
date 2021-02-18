using System;
namespace money
{
    public class Bank:Entity
    {
        private IExchangeService _exchangeService;
        public Bank(IExchangeService service)
        {
            _exchangeService = service;
        }
        public static Money Dollar(int amount) => new Money(amount, "USD");
        public static Money Franc(int amount) => new Money(amount, "CHF");

        public void AddRate(string source, string to, int rate)
        {
            _exchangeService.AddRate(source, to, rate);
        }

        public Money reduce(IExpression source,string to)
        {
            return _exchangeService.reduce(source, to);
        }
    }
}