using System;
namespace money
{
    public interface IExpression
    {
        Money reduce(Exchange exchange, string to);

        IExpression Plus(IExpression added);
    }
}