using System.Linq;
using System.Reflection.Metadata;
using System.Linq.Expressions;
using System;
using money;
using Xunit;

namespace moneytest
{
    public class ExchangeServiceTests
    {

        [Theory]
        [InlineData("","USD",2,"Source can not be null or empty")]
        [InlineData("CHF","",2,"To can not be null or empty")]
        [InlineData("CHF","USD",0,"Rate can not be zero")]
        public void If_Invalid_Paramsters_Input_AddRate_It_Should_Throw_Exception(
            string source,
            string to,
            int rate,
            string errorMessage
        )
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            //When
            ArgumentException exception = Assert.Throws<ArgumentException>(
                () => exchange.AddRate(source, to, rate)
            );
            //Then
            Assert.Contains(errorMessage, exception.Message);
        }

        [Fact]
        public void If_AddRate_Then_RatesList_It_Should_be_Equal_Input()
        {
            //Given
            string fakeFranc = "CHF";
            string fakeDollar = "USD";
            int fakeRate = 2;
            IExchangeService exchange = new ExchangeService();
            exchange.AddRate(fakeFranc, fakeDollar, fakeRate);
            //When
            var pair = new Pair(fakeFranc, fakeDollar);
            bool pairExist = exchange.RatesList.ContainsKey(pair);
            int rate = (int)exchange.RatesList[pair];
            //Then
            Assert.True(pairExist);
            Assert.Equal(fakeRate, rate);
        }

        [Fact]
        public void If_ParamArray_is_null_or_Empty_It_Should_Be_Throw_Exception()
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
            var Bucks=FakeDataBuilder.MakeDollar(1);
            var Franc=FakeDataBuilder.MakeFranc(10);
            //When
            ArgumentNullException exception=
                Assert.Throws<ArgumentNullException>(()=>
                    exchange.Sum(
                        null,
                        new ICurrencyExpression[]{Bucks,Franc}
                        ));
            //Then
            Assert.Contains("addeds contains diff currency,mush be assign currency", exception.Message);
        }

        [Fact]
        public void If_After_ExchangeTo_Currency_It_Should_Be_Clean_ExpressionList()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var fiveBucks = FakeDataBuilder.MakeDollar(5);
            var tenFranc = FakeDataBuilder.MakeFranc(10);
            exchange.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression sameParamSum=exchange
                .Sum(new Money[]{fiveBucks, fiveBucks})
                .ExchangeTo("USD");
            int counts = exchange.ExpressionsList.Count();
            //Then
            Assert.Equal(0, counts);
        }

        [Fact]
        public void If_Exchange_Params_Is_Null_It_Should_Be_Throw_Exception()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            //When
            ArgumentNullException exception=
                Assert.Throws<ArgumentNullException>(()=>
                    exchange.Exchange(FakeDataBuilder.MakeDollar(1),null));
            //Then
            Assert.Contains("Exchange must assign Currency", exception.Message);
            ArgumentNullException sourceException=Assert
            .Throws<ArgumentNullException>(()=>exchange.Exchange(null,"USD"));
            Assert.Contains("Exchange must be have Money", sourceException.Message);
        }
        
        [Fact]
        public void If_Not_Setting_Rate_Then_Exchange_It_Should_Be_Throw_Exception()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var tenFranc = FakeDataBuilder.MakeFranc(10);
            //When
            ArgumentNullException exception=
                Assert.Throws<ArgumentNullException>(()=> 
                    exchange.Exchange(tenFranc, "USD"));
            //Then
            Assert.Contains("Before Exchange must be setting Exchange rates", exception.Message);
        }

        [Fact]
        public void If_Currency_Exchange_It_Should_Be_Return_Assign_Currency_And_Correct_Amount()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            var tenFranc = FakeDataBuilder.MakeFranc(10);
            exchange.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression result = exchange.Exchange(tenFranc, "USD");
            //Then
            Assert.Equal(FakeDataBuilder.MakeDollar(5), result);
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
                    service.Times(FakeDataBuilder.MakeDollar(5),0));
            //Then
            Assert.Contains("Multiplier can not be 0", exception.Message);
        }

        [Fact]
        public void If_Multiplication_It_Should_Be_Return_Amount_Multiplied_By_N()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            int fakeAmount = 5;
            ICurrencyExpression fiveBucks = FakeDataBuilder.MakeDollar(fakeAmount);
            ICurrencyExpression fiveFranc = FakeDataBuilder.MakeFranc(fakeAmount);
            //When
            var result = exchange.Times(fiveBucks, 8);
            //Then
            Assert.True(FakeDataBuilder.MakeDollar(10).Equals(exchange.Times(fiveBucks, 2)));
            Assert.True(FakeDataBuilder.MakeDollar(15).Equals(exchange.Times(fiveBucks,3)));
            Assert.True(FakeDataBuilder.MakeFranc(10).Equals(exchange.Times(fiveFranc,2)));
            Assert.True(FakeDataBuilder.MakeFranc(15).Equals(exchange.Times(fiveFranc,3)));
        }

        [Fact]
        public void if_Sum_And_Multiplication_Then_ExchangeTo_It_Should_Be_Return_Correct_Total()
        {
            //Given
            IExchangeService service = new ExchangeService();
            var tenBucks = FakeDataBuilder.MakeDollar(10);
            var fiveBucks = FakeDataBuilder.MakeDollar(5);
            service.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression result =service
                .Sum(new Money[]{ tenBucks, fiveBucks })
                .Times(2)
                .ExchangeTo("USD");
            //Then
            Assert.Equal(FakeDataBuilder.MakeDollar(30), result);
        }

        [Fact]
        public void If_Use_ExchangeTo_Method_It_Should_Be_Correct_Currency()
        {
            //Given
            ExchangeService service = new ExchangeService();
            service.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression result= service
                .Sum(
                    new ICurrencyExpression[]
                    {
                        FakeDataBuilder.MakeDollar(5),
                        FakeDataBuilder.MakeFranc(10)
                    }).ExchangeTo("USD");
            //Then
            Assert.Equal(FakeDataBuilder.MakeDollar(10), result);
        }
    }
}