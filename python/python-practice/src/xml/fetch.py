from pprint import pprint
import requests
import xmltodict
response=requests.get(r"https://graphical.weather.gov/xml/SOAP_server/ndfdXMLclient.php?"
                                    r"whichClient=NDFDgen&lat=41.87&lon=+-87.65&product=glance")
data=xmltodict.parse(response.text)
temperature_list=data["dwml"]["data"]["parameters"]["temperature"]
max_obj=[element for element in temperature_list if element.get('@type')=='maximum'][0]
max_temperature= max_obj.get('value')[0]
time_layout=max_obj.get('@time-layout')
pprint(max_temperature)
pprint(time_layout)