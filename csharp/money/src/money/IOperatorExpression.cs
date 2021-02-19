using System;
namespace money
{
    public interface IOperatorExpression
    {
        ICurrencyExpression Sum(string to,params ICurrencyExpression[] addeds);

        ICurrencyExpression Times(ICurrencyExpression source, int multiplier);
    }
}