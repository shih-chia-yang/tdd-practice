import fileinput
def main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            print(f'<檔案{fileinput.filename}的開頭',end="")
            print(line,end="")
main()

#python3 script5.py sole1.tst sole2.tst