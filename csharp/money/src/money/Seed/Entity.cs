using System;
namespace money
{
    public abstract class Entity
    {
        int _id;
        public virtual int Id
        {
            get { return _id; }
            set { _id = value;}
        }
        
    }
}