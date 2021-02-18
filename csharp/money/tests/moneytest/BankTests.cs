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
            IExpression fivebucks = Bank.Dollar(5);
            IExpression tenfranc = Bank.Franc(10);
            bank.AddRate("CHF", "USD", 2);
            //When
            Money result=bank.reduce(fivebucks.Plus(tenfranc), "USD");
            //Then
            Assert.Equal(Bank.Dollar(10), result);
        }
    }

}