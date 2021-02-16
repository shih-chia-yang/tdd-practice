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
            var five = new Dollar(fakeAmount);
            var fiveFranc = new Franc(fakeAmount);
            Assert.True(new Dollar(10).Equals(five.times(2)));
            Assert.True(new Dollar(15).Equals(five.times(3)));
            Assert.True(new Franc(10).Equals(fiveFranc.times(2)));
            Assert.True(new Franc(15).Equals(fiveFranc.times(3)));
        }

        [Fact]
        [Trait("money","equality")]
        public void TestEquality()
        {
            //Given
            Assert.True(new Dollar(5).Equals(new Dollar(5)));
            Assert.False(new Dollar(5).Equals(new Dollar(6)));
            Assert.True(new Franc(5).Equals(new Franc(5)));
            Assert.False(new Franc(5).Equals(new Franc(6)));
            Assert.False(new Franc(5).Equals(new Dollar(5)));
            //When

            //Then
        }
    }
}
