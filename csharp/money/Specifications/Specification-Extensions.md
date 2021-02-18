# Specification-Extensions

- [ ] 導入DDD
  - [ ] 識別Entity與ValueObject
    - [ ] Exchange與Money的情境
    - [x] 匯兌機制，測試方法有大量Money物件比較，表示Money於該情境並不具備唯一值，Money物件為ValueObject
      - [x] 刪除無用IMoney介面
  - [ ] 建立Entity
  - [x] 建立ValueObject
    - [x] 以使用物件內所有值計算hash
    - [x] 新增ValueObject.cs
      - [x] 將equals方法移出至ValueObject抽象類別
      - [x] 物件值判斷使用抽象方法，應該子類別實作
      - [x] 值使用集合判斷序列是否相等，不需再用指定值相等
        - [x]空集合或null判斷
        - [x]比較序列中各值是否相等 