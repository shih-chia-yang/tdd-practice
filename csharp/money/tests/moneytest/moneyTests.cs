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
            Assert.Equal(new Dollar(10), five.times(2));
            Assert.Equal(new Dollar(15), five.times(3));
            Assert.Equal(new Franc(10),fiveFranc.times(2));
            Assert.Equal(new Franc(15), fiveFranc.times(3));
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
            //When

            //Then
        }
    }
}
