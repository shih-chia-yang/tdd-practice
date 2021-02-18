using System.Collections.Generic;
namespace src.money.Seed
{
    public abstract class ValueObject
    {
        public abstract bool GetEquality(object obj);

        public override bool Equals(object obj)
        {
            return GetEquality(obj);
        }

        public override int GetHashCode()
        {
            return 0;
        }
    }
}