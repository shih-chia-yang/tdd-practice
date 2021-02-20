using System.Security.Cryptography.X509Certificates;
using System.ComponentModel.DataAnnotations.Schema;
using System.Collections;
using System;
using System.Collections.Generic;
using System.Linq;

namespace money
{
    public interface IExchangeService:IOperatorExpression
    {
        Hashtable RatesList{ get; }
        IEnumerable<ICurrencyExpression> ExpressionsList{ get; }
        int Rate(string source, string to);
        void AddRate(string source, string to, int rate);
    }
    public class ExchangeService : IExchangeService
    {

        public Hashtable RatesList => rates;
        private Hashtable rates { get; set; }

        public IEnumerable<ICurrencyExpression> ExpressionsList => sumList.AsReadOnly();

        private List<ICurrencyExpression> sumList{ get; set;}

        public ExchangeService()
        {
            rates= new Hashtable();
            sumList = new List<ICurrencyExpression>();
        }

        public int Rate (string source,string to)
        {
            if(string.IsNullOrEmpty(source))
            {
                throw new ArgumentException("Source can not be null or empty", nameof(source));
            }
            if(string.IsNullOrEmpty(to))
            {
                throw new ArgumentException("To can not be null or empty",nameof(to));
            }
            if(source.Equals(to))return 1;
            Pair targetPair =new Pair(source, to);
            if(!rates.ContainsKey(targetPair))
            {
                throw new ArgumentException("This pair dose not exist",nameof(Rate));
            }
            int rate = (int)rates[targetPair];
            return rate;
        }
        public void AddRate(string source,string to,int rate)
        {
            if(string.IsNullOrEmpty(source))
            {
                throw new ArgumentException("Source can not be null or empty", nameof(source));
            }
            if(string.IsNullOrEmpty(to))
            {
                throw new ArgumentException("To can not be null or empty",nameof(to));
            }
            if(rate.Equals(0))
            {
                throw new ArgumentException("Rate can not be zero", nameof(rate));
            }
            rates.Add(new Pair(source, to), rate);
        }

        private void ClearList()
        {
            sumList.Clear();
        }

        public IExchangeService Sum(params ICurrencyExpression[] addeds)
        {
            sumList.AddRange(addeds);
            return this;
        }

        public ICurrencyExpression Sum (string to,params ICurrencyExpression[] addeds)
        {
            if(addeds is null || addeds.Count()==0)
            {
                throw new ArgumentNullException("addeds can't be null or empty", nameof(Sum));
            }
            if(addeds.Select(x=>x.Currency).Distinct().Count()>1 && string.IsNullOrEmpty(to))
            {
                throw new ArgumentNullException("addeds contains diff currency,mush be assign currency", nameof(Sum));
            }
            string currency = string.IsNullOrEmpty(to)?addeds[0].Currency:to;
            int amount=addeds.Select(x =>Exchange(x,currency).Amount).Aggregate((x, y)=>x + y);
            return new Money(amount,to);
        }
        
        public ICurrencyExpression ExchangeTo(string to)
        {
            if(sumList.Count.Equals(0))
            {
                throw new ArgumentException("ExpressionsList can not be empty", nameof(ExchangeTo));
            }
            int totalAmount=sumList
                    .Select(x => Exchange(x, to).Amount)
                    .Aggregate((x, y) => x + y);
            ClearList();
            return new Money(totalAmount, to);
        }

        public ICurrencyExpression Exchange(ICurrencyExpression source, string to)
        {
            if(source is null)
            {
                throw new ArgumentNullException("Exchange must be have Money", nameof(Exchange));
            }
            if(string.IsNullOrEmpty(to))
            {
                throw new ArgumentNullException("Exchange must assign Currency", nameof(Exchange));
            }
            if(rates.Count==0)
            {
                throw new ArgumentNullException("Before Exchange must be setting Exchange rates", nameof(Exchange));
            }
            return new Money(source.Amount / Rate(source.Currency, to), to);
        }

        public IExchangeService Times(int multiplier)
        {
            if(sumList.Count.Equals(0))
            {
                throw new ArgumentException("ExpressionsList can not be empty", nameof(Times));
            }
           sumList=sumList.Select(x => Times(x, multiplier)).ToList();
           return this;
        }

        public ICurrencyExpression Times(ICurrencyExpression source, int multiplier)
        {
            if(source is null)
            {
                throw new ArgumentNullException("Multiplicand can not be null", nameof(Times));
            }
            if(multiplier ==0)
            {
                throw new ArgumentNullException("Multiplier can not be 0", nameof(Times));
            }
            return new Money(source.Amount * multiplier, source.Currency);
        }
    }
}