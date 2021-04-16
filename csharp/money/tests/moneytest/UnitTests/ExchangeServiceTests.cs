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
        public void Invalid_paramsters_to_AddRate_then_throw_exception(
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
        public void AddRate_Then_RatesList_have_value()
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

        [Theory]
        [InlineData("","USD","Source can not be null or empty")]
        [InlineData("CHF","","To can not be null or empty")]
        [InlineData("123","456","This pair dose not exist")]        
        public void Invalid_parameters_to_Rate_then_throw_exception(
            string source,
            string to,
            string errorMessage
        )
        {
            //Given
            IExchangeService service = new ExchangeService();
            service.AddRate("CHF", "USD", 2);
            //When
            ArgumentException exception = Assert.Throws<ArgumentException>(
                ()=>service.Rate(source,to)
            );
            //Then
            Assert.Contains(errorMessage,exception.Message);
        }

        [Fact]
        public void After_AddRate_then_input_currency_get_Rate()
        {
            //Given
            string fakeFranc = "CHF";
            string fakeDollar = "USD";
            int fakeRate = 2;
            IExchangeService exchange = new ExchangeService();
            exchange.AddRate(fakeFranc, fakeDollar, fakeRate);
            //When
            int actual = exchange.Rate(fakeFranc, fakeDollar);
            //Then
            Assert.Equal(fakeRate, actual);
        }

        [Fact]
        public void Invalid_parameters_to_Sum_then_throw_exception()
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
        public void Sum_Params_contains_diff_money_and_param_To_is_null_then_throw_exception()
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
        public void Null_ExpressionsList_to_ExchangeTo_then_throw_exception()
        {
            //Given
            IExchangeService exchange = new ExchangeService();
            //When
            ArgumentException exception = Assert.Throws<ArgumentException>(
                () => exchange.ExchangeTo("USD")
            );
            //Then
            Assert.Contains("ExpressionsList can not be empty", exception.Message);
        }

        [Fact]
        public void Invalid_params_to_Exchange_then_throw_exception()
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
        public void Not_setting_Rate_Then_Exchange_then_throw_exception()
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
        public void Exchange_currency_then_return_assign_currency_and_correct_amount()
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
        public void Multiplicand_is_null_then_throw_exception()
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
        public void Multiplier_equal_0_then_throw_exception()
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
        public void Null_ExpressionsList_to_Times_then_throw_exception()
        {
            //Given
            IExchangeService service = new ExchangeService();
            //When
            ArgumentException exception = Assert.Throws<ArgumentException>(
                () => service.Times(2)
            );
            //Then
            Assert.Contains("ExpressionsList can not be empty", exception.Message);
        }

        [Fact]
        public void Currency_Times_N_then_return_amount_multiplied_by_N()
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
    }
}