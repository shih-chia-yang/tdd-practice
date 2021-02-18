using System.Reflection.Metadata;
using System.Linq.Expressions;
using System;
using money;
using Xunit;

namespace moneytest
{
    public class ExchangeServiceTests
    {
        [Fact]
        public void TestPlusMoney()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var fiveBucks = Bank.Dollar(5);
            var fiveFranc = Bank.Franc(5);
            //When
            Money dollarResult=exchange.Plus(new Money[]{fiveBucks, fiveBucks});
            Money francResult=exchange.Plus(new Money[]{fiveBucks, fiveBucks});
            //Then
            Assert.Equal(Bank.Dollar(10), dollarResult);
            Assert.Equal(Bank.Franc(10), francResult);
        }
    }
}