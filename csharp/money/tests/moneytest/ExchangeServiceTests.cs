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
        public void If_Sum_MutiMoney_It_Should_Be_Return_Correct_Total_Money()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var fiveBucks = Bank.Dollar(5);
            var fiveFranc = Bank.Franc(5);
            exchange.AddRate("CHF", "USD", 2);
            //When
            Money dollarResult=exchange.Plus("USD",new Money[]{fiveBucks, fiveBucks});
            Money francResult=exchange.Plus("CHF",new Money[]{fiveFranc, fiveFranc});
            //Then
            Assert.Equal(Bank.Dollar(10), dollarResult);
            Assert.Equal(Bank.Franc(10), francResult);
        }

        [Fact]
        public void if_Assigned_Currency_It_Should_Be_Return_Correct_Assigned_Currency()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var fiveFranc= Bank.Franc(10);
            exchange.AddRate("CHF", "USD", 2);
            //When
            Money result=exchange.Plus("USD",fiveFranc);
            //Then
            Assert.Equal(Bank.Dollar(5), result);
        }
    }
}