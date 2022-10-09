from flask import Flask, render_template, request
import wait_time_API 
import flight_engine_API 
app = Flask(__name__)

def getInstructions(flightNum, date, arrival, bagCheck, boardingPass,):
    terminalX = "A" #insert flight info
    airportCode = "BWI" #get from user
    departureTime = "00:18:23AM" #get from user
    waitTime = wait_time_API.waitTimeFinder(departureTime, airportCode,) #insert getWaitTime script
    print(waitTime)
    instructionsList = ["arrive to parking garage", "go to shuttle pickup, board shuttle", "arrive at terminal " + terminalX, "check bag at ticket Counter", "go through security, wait time will be approx " + str(waitTime) + " minutes", "proceed to gate", "board plane, enjoy trip"]

    if arrival == "dropOff":
        instructionsList.pop(0)
        instructionsList.pop(0)
    if bagCheck == "no":
        instructionsList.remove("check bag at ticket Counter")
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
    instructions = getInstructions(flightNum, flightDate, arrival, bagCheck) 

    return render_template('instructions.html', len = len(instructions), instructions = instructions)


if __name__ == "__main__":
    app.run()