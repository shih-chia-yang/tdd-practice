using System;
namespace money
{
    public interface IOperatorExpression
    {
        ICurrencyExpression Sum(string to,params ICurrencyExpression[] addeds);

        ICurrencyExpression Times(ICurrencyExpression source, int multiplier);

        ICurrencyExpression ExchangeTo(string to);
        
        ICurrencyExpression Exchange(ICurrencyExpression source, string to);
    }
}