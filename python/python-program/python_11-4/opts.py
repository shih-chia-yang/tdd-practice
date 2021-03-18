from argparse import ArgumentParser #從argparse模組匯入ArgumentParser類別

def main():
    parser=ArgumentParser() #用ArgumentParser類別建立Parser物件
    parser.add_argument("indent",type=int,help="indent for report")#必要參數
    parser.add_argument("inputfile",help="read data from the file")#必要參數
    parser.add_argument("-f","--file",dest="filename",help="write report to file",metavar="FILE")#選用參數
    parser.add_argument("-x","--xray",help="specify xray strength factor")#選用參數
    parser.add_argument("-q","--quite",action="store_false",dest="verbose",default=True,help="don't print status messages to stdout")#選用參數
    args=parser.parse_args()#parse_args()預設從sys.argv[1:]讀取參數毫進行解析
    print("argmuents:",args)

main()

#執行結果
#python3 opts.py -x 100 -q -f outfile.txt 2 arg2
#argmuents: Namespace(filename='outfile.txt', indent=2, inputfile='arg2', verbose=False, xray='100')