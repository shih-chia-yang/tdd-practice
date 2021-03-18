# 用pandas和matplotlib進行資料分析

- python並不是最快的語言，但python的一些資料處理與分析函式庫(如NumPy)主要是用c語言編寫，經過大量優化，使用這些函式庫，速度就可以大幅提升

## pandas使用時機
pandas無法適用實務上所有資料分析的情境，特別是遇到不須數學運算的龐大資料集，其資料通常不易放入pandas的格式中，pandas就幫不上忙。包括是清理(munging)大量產品資訊(清除異常資料、處理缺漏資料)，資料串流的異動處理等都非pandas的強項。

|功能|DataFrame的相關method|
|建立DataFrame|pd.DataFrame()|
|將所有項目加一個值|df.add()|
|處理csv資料|pd.read_csv(),pd.to_csv()|
|處理json資料|pd.read_json(),pd.to_json()|
|轉換為數值|pd.to_numeric()|
|合併DataFrame|pd.merge()|
|加總、平均、中位數、最大值、最小值|sum(),mean(),median(),max(),min()|
|依欄位值分組|df.groupby()|
|呼叫matplotlib來繪圖|df.plot.bar(),df.plot.line(),df.plot.pie()|