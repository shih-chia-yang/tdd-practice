using System.Security.Authentication;
using System.Linq;
using System.Reflection.Metadata;
using System.Linq.Expressions;
using System;
using money;
using Xunit;

namespace moneytest
{
    public class ExchangeScenario
    {

        [Fact]
        public void After_ExchangeTo_currency_then_clean_ExpressionList()
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
        public void Sum_and_Times_N_and_ExchangeTo_then_return_correct_total()
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
        public void ExchangeTo_then_return_correct_currency()
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