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
        [Trait("money","amount")]
        public void TestMultiplication()
        {
            int fakeAmount = 5;
            var fiveDollar = Bank.Dollar(fakeAmount);
            var fiveFranc = Bank.Franc(fakeAmount);
            Assert.True(Bank.Dollar(10).Equals(fiveDollar.Times(2)));
            Assert.True(Bank.Dollar(15).Equals(fiveDollar.Times(3)));
            Assert.True(Bank.Franc(10).Equals(fiveFranc.Times(2)));
            Assert.True(Bank.Franc(15).Equals(fiveFranc.Times(3)));
        }

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
            IExpression sum = new Sum(Bank.Dollar(3), Bank.Dollar(5));
            //When
            Money reduced = exchange.reduce(sum,"USD");
            //Then
            Assert.Equal(Bank.Dollar(8), reduced);
        }

        [Fact]
        public void TestReduceMoney()
        {
            //Given
            ExchangeService exchange = new ExchangeService();
            //When
            Money result = exchange.reduce(Bank.Dollar(1), "USD");
            //Then
            Assert.Equal(Bank.Dollar(1), result);
        }

        [Fact]
        public void TestReduceMoneyDifferentCurrency()
        {
            //Given
            ExchangeService change = new ExchangeService();
            //When
            change.AddRate("CHF", "USD", 2);
            Money result = change.reduce(Bank.Franc(2), "USD");
            //Then
            Assert.Equal(Bank.Dollar(1), result);
        }

        [Fact]
        public void TestMixedAddition()
        {
            //Given
            ExchangeService exchange = new ExchangeService();
            IExpression fivebucks = Bank.Dollar(5);
            IExpression tenfranc = Bank.Franc(10);
            //When
            exchange.AddRate("CHF", "USD", 2);
            Money result=exchange.reduce(fivebucks.Plus(tenfranc), "USD");
            //Then
            Assert.Equal(Bank.Dollar(10), result);
        }

        [Fact]
        public void TestSumPlusMoney()
        {
            //Given
            ExchangeService exchange = new ExchangeService();
            IExpression fiveBucks = Bank.Dollar(5);
            IExpression tenFranc = Bank.Franc(10);
            exchange.AddRate("CHF", "USD", 2);
            //When
            IExpression sum = new Sum(fiveBucks, tenFranc).Plus(fiveBucks);
            Money result = exchange.reduce(sum, "USD");
            //Then
            Assert.Equal(Bank.Dollar(15), result);
        }

        [Fact]
        public void TestSumTimesMoney()
        {
            //Given
            ExchangeService exchange = new ExchangeService();
            IExpression fiveBucks = Bank.Dollar(5);
            IExpression tenFranc = Bank.Franc(10);
            exchange.AddRate("CHF", "USD", 2);
            //When
            IExpression sum = new Sum(fiveBucks, tenFranc).Times(2);
            Money result = exchange.reduce(sum, "USD");
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
            IExpression sum = Bank.Dollar(1).Plus(Bank.Dollar(1));
            Money result = exchange.reduce(sum, "USD");
            //Then
            Assert.IsType<Money>(result);
        }
    }
}
