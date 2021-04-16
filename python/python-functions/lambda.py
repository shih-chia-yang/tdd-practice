#lambda視為只能定義一行運算式的函式，而且不需要命名，也被稱為匿名函式(anonymous function)
#lambda沒有return敘述，運算式執行後直接自動傳回
#函式為簡單的運算，且只會使用一次不會重複呼叫，此時便適合使用lambda匿名函式

t2={'FtoK':lambda deg_f:273.15+(deg_f-32)*5/9,
'CtoK':lambda deg_c:273.15+deg_c}

print(t2['FtoK'](32))