import requests
import json

def getAirport(date,flightnum):
    baseUrl = "https://morgan-knights-flight-engine.herokuapp.com/flights?"
    url = baseUrl + ("date=" + str(date)) + ("&flightNumber="+str(flightnum))
    response = requests.get(url)
    
    return response.json()[0]['origin']['code']
    
def getDepart(date,flightnum):
    baseUrl = "https://morgan-knights-flight-engine.herokuapp.com/flights?"
    url = baseUrl + ("date=" + str(date)) + ("&flightNumber="+str(flightnum))
    response = requests.get(url)
    
    depart = response.json()[0]['departureTime']
    return depart[-11:-19:-1]
