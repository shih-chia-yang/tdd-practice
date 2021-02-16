using System;
namespace money
{
    public interface IExpression
    {
        Money reduce(string to);
    }
}