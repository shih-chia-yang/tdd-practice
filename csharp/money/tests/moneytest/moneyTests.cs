using System.Reflection.Metadata;
using System.Linq.Expressions;
using System;
using money;
using Xunit;

namespace moneytest
{
    public class MoneyTest
    {
        [Fact]
        [Trait("money","equality")]
        public void TestEquality()
        {
            //Given
            //When

            //Then
            Assert.True(Bank.Dollar(5).Equals(Bank.Dollar(5)));
            Assert.False(Bank.Dollar(5).Equals(Bank.Dollar(6)));
            Assert.True(Bank.Franc(5).Equals(Bank.Franc(5)));
            Assert.False(Bank.Franc(5).Equals(Bank.Franc(6)));
            Assert.False(Bank.Franc(5).Equals(Bank.Dollar(5)));
        }

        [Fact]
        public void TestCurrency()
        {
            //Given
            //When

            //Then
            Assert.Equal("USD", Bank.Dollar(5).GetCurrency());
            Assert.Equal("CHF", Bank.Franc(5).GetCurrency());
        }

        [Fact]
        public void TestReduceSum()
        {
            //Given
            var exchange = new ExchangeService();
            // IExpression sum = new Sum(Bank.Dollar(3), Bank.Dollar(5));
            ICurrencyExpression sum = exchange.Sum("USD",new Money[] { Bank.Dollar(3), Bank.Dollar(5) });
            //When
            // Money reduced = exchange.reduce(sum,"USD");
            ICurrencyExpression result = exchange.Exchange(sum, "USD");
            //Then
            Assert.Equal(Bank.Dollar(8), result);
        }

        [Fact]
        public void TestSumTimesMoney()
        {
            //Given
            ExchangeService exchange = new ExchangeService();
            Money fiveBucks = Bank.Dollar(5);
            Money tenFranc = Bank.Franc(10);
            exchange.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression mixedTotal=exchange.Times(exchange.Sum("USD", new Money[]{ fiveBucks, tenFranc }),2);
            // IExpression sum = new Sum(fiveBucks, tenFranc).Times(2);
            ICurrencyExpression result = exchange.Exchange(mixedTotal, "USD");
            //Then
            Assert.Equal(Bank.Dollar(20), result);
        }

        [Fact]
        public void TestPlusSameCurrencyReturnMoney()
        {
            //Given
            ExchangeService exchange = new ExchangeService();
            exchange.AddRate("CHF", "USD", 2);
            //When
            ICurrencyExpression sum = exchange.Sum("USD", Bank.Dollar(1), Bank.Dollar(1));
            // IExpression sum = Bank.Dollar(1).Plus(Bank.Dollar(1));
            ICurrencyExpression result = exchange.Exchange(sum, "USD");
            //Then
            Assert.IsType<Money>(result);
        }
    }
}
