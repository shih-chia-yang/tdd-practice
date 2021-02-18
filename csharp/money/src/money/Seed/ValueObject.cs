using System.Collections.Generic;
using money;

namespace src.money.Seed
{
    public abstract class ValueObject
    {

        public abstract bool GetEquality(object obj);

        public override bool Equals(object obj)
        {
            return Equals(obj as Money);
        }

        
    }
}