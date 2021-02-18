using System.Linq;
using System.Collections.Generic;
namespace src.money.Seed
{
    public abstract class ValueObject
    {
        public abstract IEnumerable<object> GetEquality();

        public override bool Equals(object obj)
        {
            if (obj == null || obj.GetType() != GetType())
            {
                return false;
            }
            var compare = (ValueObject)obj;
            return this.GetEquality().SequenceEqual(compare.GetEquality());
        }

        public override int GetHashCode()
        {
            return 0;
        }
    }
}