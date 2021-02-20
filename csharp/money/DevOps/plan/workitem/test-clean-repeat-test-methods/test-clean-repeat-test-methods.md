# test-clean-repeat-test-methods

- [ ] #tags remove repeat test method
  - [x] remove If_SumAndTime_ThenExchange_To_AssignedCurrency_It_Should_Be_Return_Sum_Multiplied_By_N()
    - [x] 與if_Sum_And_Multiplication_It_Should_Be_Return_Correct_Total()重覆
  - [x] If_Sum_Multiple_Money_It_Should_Be_Return_Correct_Total_Money更名為If_Sum_Multiple_Money_It_Should_Be_Clean_ExpressionList
    - [x] 主要測試當使用Sum(params)時，轉換匯率後是否有清除ExpressionList 
    - [x] 轉換匯率功能已與其他測試方法重疊
  - [x]If_SumNoAssignCurrency_Then_Exchange_To_AssignedCurrency_It_Should_Be_Correct_Currency更名為If_Use_ExchangeTo_Method_It_Should_Be_Correct_Currency
  - [x] if_Sum_And_Multiplication_It_Should_Be_Return_Correct_Total更名if_Sum_And_Multiplication_Then_ExchangeTo_It_Should_Be_Return_Correct_Total
  - [x] 新增 If_AddRate_Then_RatesList_It_Should_be_Equal_Input，測試AddRate方法是否正常
  - [ ]新增UnitTests資料夾
    - [ ] 新增 If_Invalid_Paramsters_Input_AddRate_It_Should_Throw_Exception()
  - [ ]新增Functional資料夾
    - [ ] 新增ExchangeScenario.cs