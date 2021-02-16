# money Specification

|標的|股份|股價|合計
|--|--|--|--|
|IBM|1000|25美元|25000美元|
|GE|400|100瑞士法郎|40000瑞士法郎|
|合計|||65000美元|

|幣別|兌換幣別|匯率|
|--|--|--|
|瑞士法郎|美元|1.5|

- [ ] #tags rules 當瑞士法郎與美元的匯率為2：1的時候，則5美元+10瑞士法郎=10美元
        - [x] add TestSimpleAddition test method
        - [ ] 5美元+5美元=10美元
        - [ ] 5美元+5美元應回傳一個Money物件
        - [x] Exchange.reduce(Money);
        - [ ] 有轉換功能的Reduce Money
        - [ ] Reduce(Exchange,string)
- [ ] #tags rules Dollar 物件
        - [x] 5美元×2=10美元
        - [x] 5法郎×2=10法郎
        - [x] 將amount 宣告為private
        - [x] Dollar類別有副作用嗎？
        - [ ] 金額（amount)是否需要整數？
- [x] #tags Dollar與Franc物件重覆設計
        - [x]  新增 abstract class Money
        - [x]  equals方法重覆
        - [x]  times方法重覆
                - [x] times方法移至抽象類別，發生錯誤，無法回傳抽象類別，將Money更改為class
                - [x] 測試失敗，TestMultiplication發生錯誤，型別不相等，應調整為判斷Currency是否相等
        - [x]  Money新增times抽象方法，提供子類別實作
        - [x]  新增IExchange介面，Exchange類別繼承實作工廠模式，解除測試程式與Dollar與Franc的相依關係
        - [X]  新增貨幣概念
                - [x] 新增Currency欄位
        - [X]  刪除Dollar與Franc物件，因類別僅剩建構子方法，已可被Money物件取代
        
- [x] #tags rules equals()
        - [x]  比較Dollar與Franc物件是否相等
        - [x]  判斷是否null
        - [x]  判斷位何型別物件的相等
        - [ ]  hashCode()

## practice experience
