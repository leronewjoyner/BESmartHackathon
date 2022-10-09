from hashlib import new
from operator import ne
from flask import Flask, render_template, request
import new_flight_engine
import wait_time_API 

app = Flask(__name__)

def getInstructions(flightNum, date, arrival, bagCheck, boardingPass,):

    terminalX = "A" #unavailable info
    airportCode = new_flight_engine.getAirport(str(date),str(flightNum))
    departureTime = new_flight_engine.getDepart(str(date),str(flightNum))
    departHour = departureTime[0:2]
    #waitTime = wait_time_API(int(departHour),airportCode)
    waitTime = wait_time_API.waitTimeFinder(int(departHour), airportCode,) #insert getWaitTime script
    instructionsList = ["Arrive and park at parking garage", "Walk to shuttle pickup, board shuttle","Arrive at terminal " + terminalX, 
    "Get your boarding pass via self-service kiosk" ,"Check bag at ticket Counter", "Go through security, wait time will be approximately " + str(waitTime) + 
    " minutes", "Proceed to gate", "Board plane, enjoy your trip!"]

    if arrival == "dropOff":
        instructionsList.pop(0)
        instructionsList.pop(0)
    if bagCheck == "no":
        instructionsList.remove("Check bag at ticket Counter")
    if boardingPass == "no":
        instructionsList.remove("Get your boarding pass via self-service kiosk")
    return instructionsList


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def getFormInfo():
    flightNum = request.form['flightNum']
    flightDate = request.form['flightDate']
    arrival = request.form['arrival']
    bagCheck = request.form['bagcheck']
    boardingPass = request.form['boardingPass']
    instructions = getInstructions(flightNum, flightDate, arrival, bagCheck, boardingPass) 

    return render_template('instructions.html', len = len(instructions), instructions = instructions)


if __name__ == "__main__":
    app.run()