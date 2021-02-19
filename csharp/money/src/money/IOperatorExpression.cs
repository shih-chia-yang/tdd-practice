using System;
using System.Collections.Generic;

namespace money
{
    public interface IOperatorExpression
    {
        IExchangeService Sum(params ICurrencyExpression[] addeds);
        ICurrencyExpression Sum(string to,params ICurrencyExpression[] addeds);

        IExchangeService Times(int multiplier);

        ICurrencyExpression Times(ICurrencyExpression source, int multiplier);

        ICurrencyExpression ExchangeTo(string to);

        ICurrencyExpression Exchange(ICurrencyExpression source, string to);
    }
}