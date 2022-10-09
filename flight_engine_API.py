import requests as rq
import json

def getFlightInfo(date,flightnum):
    baseUrl = "https://morgan-knights-flight-engine.herokuapp.com/flights?"
    url = baseUrl + ("date=" + date) + ("&flightNumber="+flightnum)
    response = rq.get(url)
    print(response.json()[0]['orgin']['code'])
    # # print(data)
    # print(data[0]['orgin']['code'])
    # return(data)

getFlightInfo("2022-10-12","3301")
