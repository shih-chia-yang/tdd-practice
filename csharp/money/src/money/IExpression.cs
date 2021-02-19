using System;
namespace money
{
    public interface IOperatorExpression
    {
        Money reduce(IExchangeService exchange, string to);

        IOperatorExpression Times(int multiplier);
    }
}