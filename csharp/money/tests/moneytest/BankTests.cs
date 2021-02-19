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
            Money fivebucks = Bank.Dollar(5);
            Money tenfranc = Bank.Franc(10);
            bank.AddRate("CHF", "USD", 2);
            //When
            Money sum=service.Sum("USD", new Money[] { fivebucks, tenfranc });
            Money result=bank.reduce(sum, "USD");
            //Then
            Assert.Equal(Bank.Dollar(10), result);
        }
    }

}