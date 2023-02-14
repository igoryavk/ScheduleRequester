import requests
import json
from enum import Enum
class Station(Enum):
    Kurskiy="s2000001"
    Nizhegorodskaya="s9601835"
    Zheleznodorojnaya="s9601675"

class Scheduler():
    from_station=Station.Zheleznodorojnaya.value
    to_station=Station.Nizhegorodskaya.value
    format="json"
    date="2023-02-14"
    lang='RU-ru'
    apikey='a6273ab5-4d48-46d5-b498-d5a33402e2d3'
    request=f"https://api.rasp.yandex.net/v3.0/search/?from={from_station}&to={to_station}&format={format}&apikey={apikey}&date={date}"
    pars_string:str
    def RequestSchedule(self):
        result=requests.get(self.request)
        pars_string=json.loads(result.text)
        #print(pars_string['search']['from']['title'])
        #print(pars_string['search'])
        for str in pars_string['segments']:
            print(str['thread']['title'])
            print(str['departure'])
            #print(str['thread']['departure'])



if __name__=='__main__':
    scheduler=Scheduler()
    scheduler.RequestSchedule()















