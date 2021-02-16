using System.Linq.Expressions;
using System;
using money;
using Xunit;

namespace moneytest
{
    public class MoneyTest
    {
        [Fact]
        [Trait("money","amount")]
        public void TestMultiplication()
        {
            int fakeAmount = 5;
            IExchange exchange = new Exchange();
            var fiveDollar = exchange.Dollar(fakeAmount);
            var fiveFranc = exchange.Franc(fakeAmount);
            Assert.True(exchange.Dollar(10).Equals(fiveDollar.times(2)));
            Assert.True(exchange.Dollar(15).Equals(fiveDollar.times(3)));
            Assert.True(exchange.Franc(10).Equals(fiveFranc.times(2)));
            Assert.True(exchange.Franc(15).Equals(fiveFranc.times(3)));
        }

        [Fact]
        [Trait("money","equality")]
        public void TestEquality()
        {
            //Given
            IExchange exchange = new Exchange();
            
            //When

            //Then
            Assert.True(exchange.Dollar(5).Equals(exchange.Dollar(5)));
            Assert.False(exchange.Dollar(5).Equals(exchange.Dollar(6)));
            Assert.True(exchange.Franc(5).Equals(exchange.Franc(5)));
            Assert.False(exchange.Franc(5).Equals(exchange.Franc(6)));
            Assert.False(exchange.Franc(5).Equals(exchange.Dollar(5)));
        }

        [Fact]
        public void TestCurrency()
        {
            //Given
            IExchange exchange = new Exchange();
            //When

            //Then
            Assert.Equal("USD", exchange.Dollar(5).GetCurrency());
            Assert.Equal("CHF", exchange.Franc(5).GetCurrency());
        }

        [Fact]
        public void TestReduceSum()
        {
            //Given
            var exchange = new Exchange();
            IExpression sum = new Sum(exchange.Dollar(3), exchange.Dollar(5));
            //When
            Money reduced = exchange.reduce(sum,"USD");
            //Then
            Assert.Equal(exchange.Dollar(8), reduced);
        }

        [Fact]
        public void TestReduceMoney()
        {
            //Given
            Exchange exchange = new Exchange();
            //When
            Money result = exchange.reduce(exchange.Dollar(1), "USD");
            //Then
            Assert.Equal(exchange.Dollar(1), result);
        }

        // [Fact]
        // public void TestReduceMoneyDifferentCurrency()
        // {
        //     //Given
        //     Exchange change = new Exchange()
        //     //When
        //     change.AddRate("CHF", "USD", 2);
        //     Money result = change.reduce(change.Franc(2), "USD");
        //     //Then
        //     Assert.Equal(change.Dollar(1), result);
        // }
    }
}
