using System.Linq;
using System.Collections.Generic;
namespace src.money.Seed
{
    public abstract class ValueObject
    {
        public abstract IEnumerable<object> GetEquality();

        public override bool Equals(object obj)
        {
            return GetEquality().Count() > 0;
        }

        public override int GetHashCode()
        {
            return 0;
        }
    }
}