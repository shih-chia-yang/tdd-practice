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
        public void If_Same_Amount_Currency_Then_Compare_Equal_It_Should_Be_Return_True()
        {
            //Given
            var fiveBucks=FakeDataBuilder.MakeDollar(5);
            var fiveFranc=FakeDataBuilder.MakeFranc(5);
            //When

            //Then
            Assert.True(fiveBucks.Equals(FakeDataBuilder.MakeDollar(5)));
            Assert.False(fiveBucks.Equals(FakeDataBuilder.MakeDollar(6)));
            Assert.True(fiveFranc.Equals(FakeDataBuilder.MakeFranc(5)));
            Assert.False(fiveFranc.Equals(FakeDataBuilder.MakeFranc(6)));
            Assert.False(fiveFranc.Equals(FakeDataBuilder.MakeDollar(5)));
        }

        [Fact]
        public void If_Create_Money_Then_Get_Currency_It_Should_Be_Return_Currency()
        {
            //Given
            var fiveBucks=FakeDataBuilder.MakeDollar(5);
            var fiveFranc=FakeDataBuilder.MakeFranc(5);
            //When

            //Then
            Assert.Equal("USD", fiveBucks.GetCurrency());
            Assert.Equal("CHF", fiveFranc.GetCurrency());
        }
    }
}
