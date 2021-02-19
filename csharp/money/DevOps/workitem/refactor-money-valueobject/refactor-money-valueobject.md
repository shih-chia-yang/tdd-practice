# Refactor Money valueobject

- [x] #tags refact/refactor-Money-entity Plus方法移至ExchangeService
    - [x] 新增Plus方法
      - [x] 更名為Sum 
    - [x] 使用參數陣列傳值
    - [x] 進行多參數陣列加總
      - [x] 空集合判斷
    - [x] 法郎加總
    - [x] 指定幣別轉換
    - [x] 混合幣別加總
    - [x] 是否有比foreach更快捷的方式
      - [x]使用linq aggregate進行加總 
    - [x] 加入匯率轉換
      - [x] 將算式獨立出來取代Money.Reduce，新增Exchange method
      - [x] Money.Plus與Exchange.Plus Rate方法重覆
    - [x] ExchangeServiceTests與MoneyTests測試方法重覆
    - [x] Money移除IExpression
    - [x] 移除Times方法