import csv
from pathlib import Path
import openpyxl

# 格式設定，請參閱文件 https://openpyxl.readthedocs.io

def output_csv(headers,contents,path):
    output_path=Path(path)
    with open(output_path,'w',newline='',encoding="utf-8") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerow(contents)

def output_xlsx(input,output):
    data_row=[ fields for fields in csv.reader(input)]
    wb=openpyxl.Workbook()
    ws=wb.active
    ws.title="test data"
    for row in data_row:
        ws.append(row)
    wb.save(output)
