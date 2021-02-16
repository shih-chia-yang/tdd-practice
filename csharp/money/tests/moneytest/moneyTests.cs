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
        public void TestSimpleAddition()
        {
            //Given
            var exchange = new Exchange();
            Money fiveDollar = exchange.Dollar(5);
            Expression sum = fiveDollar.Plus(fiveDollar);
            Bank bank = new Bank();
            //When
            Money reduced = bank.reduce(sum,"USD");
            //Then
            Assert.Equal(exchange.Dollar(10), reduced);
        }
    }
}
