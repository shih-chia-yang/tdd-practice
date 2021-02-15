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
            Dollar five = new Dollar(fakeAmount);
            var product=five.times(2);
            Assert.Equal(10, product.amount);
            product=five.times(3);
            Assert.Equal(15, product.amount);
        }

        [Fact]
        [Trait("money","equality")]
        public void TestEquality()
        {
            //Given
            Assert.True(new Dollar(5).Equals(new Dollar(5)));
            Assert.False(new Dollar(5).Equals(new Dollar(6)));
            //When

            //Then
        }
    }
}
