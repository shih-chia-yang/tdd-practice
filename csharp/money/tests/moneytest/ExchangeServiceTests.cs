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
            ArgumentNullException exception=Assert.Throws<ArgumentNullException>(()=>exchange.Sum(null));
            //Then
            Assert.Contains("addeds can't be null or empty", exception.Message);
        }
        
        [Fact]
        public void If_Sum_Multiple_Money_It_Should_Be_Return_Correct_Total_Money()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var fiveBucks = Bank.Dollar(5);
            var tenFranc = Bank.Franc(10);
            exchange.AddRate("CHF", "USD", 2);
            //When
            Money sameParamSum=exchange.Sum("USD",new Money[]{fiveBucks, fiveBucks});
            Money mixedSum=exchange.Sum("USD",new Money[]{fiveBucks, tenFranc,fiveBucks});
            //Then

            Assert.Equal(Bank.Dollar(10), sameParamSum);
            Assert.Equal(Bank.Dollar(15), mixedSum);
        }

        [Fact]
        public void if_Currency_Exchange_It_Should_Be_Return_Assign_Currency_And_Correct_Amount()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var tenFranc = Bank.Franc(10);
            exchange.AddRate("CHF", "USD", 2);
            //When
            Money result = exchange.Exchange(tenFranc, "USD");
            //Then
            Assert.Equal(Bank.Dollar(5), result);
        }

        [Fact]
        public void if_Multiplication_It_Should_Be_Return_Amount_Multiplied_By_N()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var fiveBucks = Bank.Dollar(5);
            //When
            var result = exchange.Times(fiveBucks, 8);
            //Then
            Assert.Equal(Bank.Dollar(40), result);
        }

        [Fact]
        public void if_Sum_And_Multiplication_It_Should_Be_Return_Correct_Total()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var tenBucks = Bank.Dollar(10);
            var fiveBucks = Bank.Dollar(5);
            //When
            Money result =exchange.Times(exchange.Sum(tenBucks.Currency, new Money[]{ tenBucks, fiveBucks }),2);
            //Then
            Assert.Equal(Bank.Dollar(30), result);
        }
    }
}