using System;
namespace money
{
    public interface IExpression
    {
        Money reduce(string to);

        Money reduce(Exchange exchange, string to);
    }
}