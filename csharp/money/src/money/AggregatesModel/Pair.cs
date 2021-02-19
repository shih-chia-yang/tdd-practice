using System;
using System.Collections.Generic;
using src.money.Seed;

namespace money
{
    public class Pair : ValueObject
    {
        public string Source { get; private set; }

        public string To { get; private set; }

        public Pair(string source, string to)
        {
            Source = source;
            To = to;
        }

        public override IEnumerable<object> GetEquality()
        {
            yield return Source;
            yield return To;
        }
    }
}