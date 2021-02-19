# refactor-exchange-service

- tags refactor
      - [ ] 法郎與美元互相轉換
      - [ ] Sum需指定幣別才能加總，是否可以像sum一樣在轉換幣別時才進行換算
      - [ ] 利用extension方法，如Money result =service.Sum(money[]).Time(n).Exchange("currency")
      - [ ] IExchangeService 與 IExpression方法重覆
          - [ ] ExchangeService 與 Sum物件重覆
          - [ ] 運算式部份是否獨立出來，ExchangeService只進行匯率轉換