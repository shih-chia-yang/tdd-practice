import csv
from pathlib import Path
import openpyxl

def output_csv(headers,contents,path):
    output_path=Path(path)
    with open(output_path,'w',newline='',encoding="utf-8") as csvfile:
        # dict_writer=csv.DictWriter(csvfile,fieldnames=headers)
        # dict_writer.writeheader()
        # dict_writer.writerows({'a':1,'b':2,'c':3,'d':4})
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
