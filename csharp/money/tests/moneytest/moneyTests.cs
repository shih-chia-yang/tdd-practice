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
    }
}
