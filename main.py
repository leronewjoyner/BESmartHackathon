import wait_time_API as wait_time_API
import flight_engine_API as flight_engine_API
from flask import Flask, render_template, request


def getInstructions():
    terminalX = "A" #insert flight info
    airportCode = "BWI" #get from user
    departureTime = "00:18:23AM" #get from user
    waitTime = wait_time_API.waitTimeFinder(departureTime, airportCode,) #insert getWaitTime script
    print(waitTime)
    instructionsList = ["arrive to parking garage", "go to shuttle pickup, board shuttle", "arrive at " + terminalX, "check bag at ticket Counter", "go through security, wait time will be approx " + str(waitTime) + " minutes", "proceed to gate", "board plane, enjoy trip"]
    parking = True
    checking = True
    if not parking:
        instructionsList.pop(0)
        instructionsList.pop(1)
    if not checking:
        instructionsList.pop(3)
    return instructionsList
getInstructions()
# inst = getInstructions()
# print(*inst,sep='\n')