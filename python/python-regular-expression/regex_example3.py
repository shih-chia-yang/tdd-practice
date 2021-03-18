import re

string="if the problem is textual, use the the re module"
pattern=r"the the"
regxp=re.compile(pattern)
#sub 第一個參數是用來替換的新字串，第二個參數則是要搜尋取代的原字串
#
print(regxp.sub("test",string))