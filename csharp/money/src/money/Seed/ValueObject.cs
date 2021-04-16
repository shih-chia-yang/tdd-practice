using System.Xml.Linq;
using System.Security.Cryptography.X509Certificates;
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
            return GetEquality().Select(x=>x!=null?x.GetHashCode():0).Aggregate((x,y)=>x^y);
        }
    }
}