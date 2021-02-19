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
        public void if_ParamArray_is_null_or_Empty_It_Should_Be_Throw_Exception()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            //When
            ArgumentNullException exception=
                Assert.Throws<ArgumentNullException>(()=>exchange.Sum("USD",null));
            //Then
            Assert.Contains("addeds can't be null or empty", exception.Message);
        }

        [Fact]
        public void If_Array_Contains_Diff_Money_And_Param_to_Is_Null_It_Should_Be_Throw_Exception()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            //When
            ArgumentNullException exception=
                Assert.Throws<ArgumentNullException>(()=>
                    exchange.Sum(
                        null,
                        new ICurrencyExpression[]{Bank.Dollar(1),Bank.Franc(10)}
                        ));
            //Then
            Assert.Contains("addeds contains diff currency,mush be assign currency", exception.Message);
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
            ICurrencyExpression sameParamSum=exchange.Sum("USD",new Money[]{fiveBucks, fiveBucks});
            ICurrencyExpression mixedSum=exchange.Sum("USD",new Money[]{fiveBucks, tenFranc,fiveBucks});
            //Then

            Assert.Equal(Bank.Dollar(10), sameParamSum);
            Assert.Equal(Bank.Dollar(15), mixedSum);
        }

        [Fact]
        public void if_Exchange_Params_Is_Null_It_Should_Be_Throw_Exception()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            //When
            ArgumentNullException exception=
                Assert.Throws<ArgumentNullException>(()=>
                    exchange.Exchange(Bank.Dollar(1),null));
            //Then
            Assert.Contains("Exchange must assign Currency", exception.Message);
            ArgumentNullException sourceException=Assert
            .Throws<ArgumentNullException>(()=>exchange.Exchange(null,"USD"));
            Assert.Contains("Exchange must be have Money", sourceException.Message);
        }

        [Fact]
        public void if_Currency_Exchange_It_Should_Be_Return_Assign_Currency_And_Correct_Amount()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var tenFranc = Bank.Franc(10);
            exchange.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression result = exchange.Exchange(tenFranc, "USD");
            //Then
            Assert.Equal(Bank.Dollar(5), result);
        }

        [Fact]
        public void If_Not_Setting_Rate_Then_Exchange_It_Should_Be_Throw_Exception()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var tenFranc = Bank.Franc(10);
            //When
            ArgumentNullException exception=
                Assert.Throws<ArgumentNullException>(()=> 
                    exchange.Exchange(tenFranc, "USD"));
            //Then
            Assert.Contains("Before Exchange must be setting Exchange rates", exception.Message);
        }

        [Fact]
        public void If_Multiplicand_Is_Null_It_Should_Be_Throw_Exception()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            //When
            ArgumentNullException exception =
                Assert.Throws<ArgumentNullException>(()=>
                    exchange.Times(null,2));
            //Then
            Assert.Contains("Multiplicand can not be null", exception.Message);
        }

        [Fact]
        public void If_Multiplier_Equal_0_It_Should_Be_Throw_Exception()
        {
            //Given
            IExchangeService service = new ExchangeService();
            //When
            ArgumentNullException exception =
                Assert.Throws<ArgumentNullException>(()=>
                    service.Times(Bank.Dollar(5),0));
            //Then
            Assert.Contains("Multiplier can not be 0", exception.Message);
        }

        [Fact]
        public void If_Multiplication_It_Should_Be_Return_Amount_Multiplied_By_N()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            int fakeAmount = 5;
            ICurrencyExpression fiveBucks = Bank.Dollar(fakeAmount);
            ICurrencyExpression fiveFranc = Bank.Franc(fakeAmount);
            //When
            var result = exchange.Times(fiveBucks, 8);
            //Then
            Assert.True(Bank.Dollar(10).Equals(exchange.Times(fiveBucks, 2)));
            Assert.True(Bank.Dollar(15).Equals(exchange.Times(fiveBucks,3)));
            Assert.True(Bank.Franc(10).Equals(exchange.Times(fiveFranc,2)));
            Assert.True(Bank.Franc(15).Equals(exchange.Times(fiveFranc,3)));
        }

        [Fact]
        public void if_Sum_And_Multiplication_It_Should_Be_Return_Correct_Total()
        {
            //Given
            IExchangeService service = new ExchangeService();
            var tenBucks = Bank.Dollar(10);
            var fiveBucks = Bank.Dollar(5);
            service.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression result =service
                .Sum(new Money[]{ tenBucks, fiveBucks })
                .Times(2)
                .ExchangeTo("USD");
            //Then
            Assert.Equal(Bank.Dollar(30), result);
        }

        [Fact]
        public void If_SumNoAssignCurrency_Then_Exchange_To_AssignedCurrency_It_Should_Be_Correct_Currency()
        {
            //Given
            ExchangeService service = new ExchangeService();
            service.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression result= service
                .Sum(
                    new ICurrencyExpression[]
                    {
                        Bank.Dollar(5),
                        Bank.Franc(10)
                    }).ExchangeTo("USD");
            //Then
            Assert.Equal(Bank.Dollar(10), result);
        }

        [Fact]
        public void If_SumAndTime_ThenExchange_To_AssignedCurrency_It_Should_Be_Return_Sum_Multiplied_By_N()
        {
            //Given
            ExchangeService service = new ExchangeService();
            service.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression result= service
                .Sum(
                    new ICurrencyExpression[]
                    {
                        Bank.Dollar(5),
                        Bank.Franc(10)
                    }).Times(2).ExchangeTo("USD");
            //Then
            Assert.Equal(Bank.Dollar(20), result);
        }
    }
}