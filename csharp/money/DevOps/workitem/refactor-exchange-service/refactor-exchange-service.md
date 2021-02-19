# refactor-exchange-service

- tags refactor
      - [ ] 法郎與美元互相轉換
      - [x] Sum需指定幣別才能加總，是否可以像sum一樣在轉換幣別時才進行換算
        - [x] 新增Sum方法
        - [x] 新增ExchangeTo方法 
      - [x] Money result =service.Sum(money[]).Time(n).Exchange("currency")
      - [x] IExchangeService 與 IExpression方法重覆
          - [x] ExchangeService 與 Sum物件重覆
          - [ ] 運算式部份是否獨立出來，ExchangeService只進行匯率轉換
      - [x] 進行換匯時，若無設定匯率 throw exception