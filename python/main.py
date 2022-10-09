import python.wait_time_API as wait_time_API
def getInstructions():
    terminalX = "A" #insert flight info
    waitTime = wait_time_API.waitTimeFinder() #insert getWaitTime script
    instructionsList = ["arrive to parking garage", "go to shuttle pickup, board shuttle", "arrive at " + terminalX, "check bag at ticket Counter", "go through security, wait time will be approx " + str(waitTime) + " minutes", "proceed to gate", "board plane, enjoy trip"]
    parking = True
    checking = True
    if not parking:
        instructionsList.pop(0)
        instructionsList.pop(1)
    if not checking:
        instructionsList.pop(3)
    return instructionsList

inst = getInstructions()
print(*inst,sep='\n')