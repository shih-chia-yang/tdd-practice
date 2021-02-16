using System;
namespace money
{
    public class Pair
    {
        public string  Source{ get; private set; }
        public string To{ get; private set; }

        public Pair(string source,string to)
        {
            Source = source;
            To = to;
        }

        public override bool Equals(object obj)
        {
            //
            // See the full list of guidelines at
            //   http://go.microsoft.com/fwlink/?LinkID=85237
            // and also the guidance for operator== at
            //   http://go.microsoft.com/fwlink/?LinkId=85238
            //
            
            if (obj == null || GetType() != obj.GetType())
            {
                return false;
            }

            // TODO: write your implementation of Equals() here
            Pair pair = (Pair)obj;
            return (this.Source.Equals(pair.Source)&&this.To.Equals(pair.To));
        }
        
        // override object.GetHashCode
        public override int GetHashCode()
        {
            // TODO: write your implementation of GetHashCode() here
            return 0;
        }
    }
}