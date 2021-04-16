import requests
response=requests.get(r"https://data.cityofchicago.org/resource/6zsd-86xi.json?"
                                    r"$where=date between '2019-01-10T12:00:00'and '2019-01-10T13:00:00'")
print(response.text)