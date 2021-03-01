import sys
def main():
    contents=sys.stdin.read()
    sys.stdout.write(contents.replace(sys.argv[1],sys.argv[2]))
main()
# pipe line 概念
# 執行 python3 replace.py zero 0 <infile.txt > outfile.txt
# result 將infile.txt 內容中的zero 替換成0 再輸出至outfile.txt

#執行 python3 replace.py a A <infile.txt >>outfile.txt
#將修改的內容附加至outfile.txt

#python3 replace.py 0 zero < infile.txt | python3 replace.py 1 one > outfile.txt
