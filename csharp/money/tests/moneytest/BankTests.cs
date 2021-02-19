using System.Reflection.Metadata;
using System.Linq.Expressions;
using System;
using money;
using Xunit;

namespace moneytest
{
    public class BankTests
    {
        [Fact]
        public void TestBankExchangeService()
        {
            //Given
            IExchangeService service = new ExchangeService();
            Bank bank = new Bank(service);
            ICurrencyExpression fivebucks = Bank.Dollar(5);
            ICurrencyExpression tenfranc = Bank.Franc(10);
            bank.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression sum=service.Sum("USD", new ICurrencyExpression[] { fivebucks, tenfranc });
            ICurrencyExpression result=bank.reduce(sum, "USD");
            //Then
            Assert.Equal(Bank.Dollar(10), result);
        }
    }

}