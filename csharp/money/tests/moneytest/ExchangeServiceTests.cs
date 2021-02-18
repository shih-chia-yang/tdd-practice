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
        public void if_ParamArray_is_null_or_Empty_It_Should_Be_Return_Exception()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            //When
            //Then
            ArgumentNullException exception=Assert.Throws<ArgumentNullException>(()=>exchange.Plus(null));
            Assert.Contains("addeds can't be null or empty", exception.Message);
        }
        
        [Fact]
        public void TestPlusMoney()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var fiveBucks = Bank.Dollar(5);
            var fiveFranc = Bank.Franc(5);
            //When
            Money dollarResult=exchange.Plus(new Money[]{fiveBucks, fiveBucks});
            Money francResult=exchange.Plus(new Money[]{fiveFranc, fiveFranc});
            //Then
            Assert.Equal(Bank.Dollar(10), dollarResult);
            Assert.Equal(Bank.Franc(10), francResult);
        }
    }
}