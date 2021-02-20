using System;
using money;
using Xunit;

namespace moneytest
{
    public class PairTests
    {
        [Fact]
        public void If_Same_Value_It_Should_Be_Equality()
        {
            //Given
            var pair1 = new Pair("1", "2");
            var pair2 = new Pair("1", "2");
            //When
            bool isEqual = pair1.Equals(pair2);
            //Then
            Assert.True(isEqual);
        }
    }
}