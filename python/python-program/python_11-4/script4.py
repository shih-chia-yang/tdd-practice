import fileinput
def main():
    for line in fileinput.input():
        if not line.startswith('##'):
            print(line,end="")
main()


#python3 script4.py sole1.tst sole2.tst