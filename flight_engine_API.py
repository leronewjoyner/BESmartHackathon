import requests
import json

def getFlightInfo(date,flightnum):
    baseUrl = "https://morgan-knights-flight-engine.herokuapp.com/flights?"
    url = baseUrl + ("date=" + date) + ("&flightNumber="+flightnum)
    response = requests.get(url)
    data = response.json()
    print(data)

