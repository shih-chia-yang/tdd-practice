using System;
using money;
using Xunit;

namespace moneytest
{
    public class MoneyTest
    {
        [Theory]
        [InlineData(2,10)]
        [InlineData(3,15)]
        [Trait("money","amount")]
        public void TestMultiplication(int times,int expected)
        {
            int fakeAmount = 5;
            var dollar = new Dollar(fakeAmount);
            var actualAmount=dollar.times(times);
            Assert.Equal(expected, actualAmount);
        }
    }
}
