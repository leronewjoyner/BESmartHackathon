

# instructions list - 
# [
#     arrive to parking garage
#     go to shuttle pickup, board shuttle
#     arrive at terminalx
#     check bag at ticket Counter
#     go through security, wait time will be approx x
#     proceed to gate
#     board plane, enjoy trip
# ]

# if not parking
#     remove list 0
#     remove list 1

# if not checking
#     remove list 3
def getInstructions():
    terminalX = "A" #insert flight info
    waitTime = "5" #insert getWaitTime script
    instructionsList = ["arrive to parking garage", "go to shuttle pickup, board shuttle", "arrive at " + terminalX, "check bag at ticket Counter", "go through security, wait time will be approx " + waitTime + " minutes", "proceed to gate", "board plane, enjoy trip"]
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