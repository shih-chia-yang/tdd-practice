import json
from json.tool import main
from symbol import with_item
import requests
from pprint import pprint as pp
from pathlib import Path

crime_url=r"https://data.cityofchicago.org/resource/6zsd-86xi.json?"\
                  r"$where=date between '2019-01-10T12:00:00'and '2019-01-10T13:00:00'"
output_file1="20190110120000_chicago_crime.txt"
output_file2="20190110120000_chicago_crime1.txt"

def fetch(url):
    response=requests.get(url)
    data =response.json()
    output(data)
    output_eachline(data)

def output(json_source):
    with open(output_file1,'w') as file:
        json.dump(json_source,file,indent=2)

def output_eachline(json_source):
    with open(output_file2,'w') as file:
        for crime in json_source:
            json.dump(crime,file)
            file.write("\n")

def read(file_path):
    with open (file_path,'r') as read:
        for line in read.readlines():
            data=json.loads(line)
            print(data)

def main():
    fetch(crime_url)
    # read each line json
    read("20190110120000_chicago_crime1.txt")

if __name__ == '__main__':
    main()

