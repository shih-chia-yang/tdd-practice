# Refactor Money valueobject

- [ ] #tags refact/refactor-Money-entity Plus方法移至ExchangeService
    - [x] 新增Plus方法
    - [x] 使用參數陣列傳值
    - [ ] 進行多參數陣列加總
      -[x] 空集合判斷 
    - [x] 法郎加總
    - [x] 指定幣別轉換
    - [ ] 混合幣別加總
    - [x] 是否有比foreach更快捷的方式
      - [x]使用linq aggregate進行加總 
    - [x] 加入匯率轉換
      - [ ] 法郎與美元互相轉換 