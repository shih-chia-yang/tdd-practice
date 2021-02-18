using System;
namespace money
{
    public interface IExpression
    {
        Money reduce(IExchangeService exchange, string to);

        IExpression Plus(IExpression added);

        IExpression Times(int multiplier);
    }
}