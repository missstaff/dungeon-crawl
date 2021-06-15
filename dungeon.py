from random import randint
from constants import MAX_SIZE, PLAYER, EXIT, TRAP, TREASURE


def displayInstructions():
    """Displays instructions to user"""
    print("Welcome to Dungeon Crawl! \n" +
          "Use the 'L', 'R', 'U' and 'D' buttons to move your player\n" +
          "or use 'Q' to quit\n"
          "Let's get crawling.")
    print("\n")


def createDungeon(dungeonboard, traps, treasures):
    """Creates the dungeon by randomly placing game elements including player at its starting location"""
    playerlocation = findEmpty(dungeonboard)  # player's starting location
    dungeonboard[playerlocation[0]][playerlocation[1]] = PLAYER
    endgame = findEmpty(dungeonboard)  # exit's location
    dungeonboard[endgame[0]][endgame[1]] = EXIT

    for i in range(traps):  # places random number of traps randomly on the board
        traps = findEmpty(dungeonboard)
        dungeonboard[traps[0]][traps[1]] = TRAP

    for i in range(treasures):  # places random number of treasures randomly on the board
        treasures = findEmpty(dungeonboard)
        dungeonboard[treasures[0]][treasures[1]] = TREASURE

    return playerlocation


def displayDungeon(dungeonboard):
    """Displays the dungeon"""
    # how to add exterior walls??
    print("[-----------------------------]")
    for row in range(MAX_SIZE):
        # print("|")
        for col in range(MAX_SIZE):
            print(" " + dungeonboard[row][col], end=" ")
        print("|")
    print("[-----------------------------]")
    print("\n")


def getMove(playerlocation, dungeonboard):
    """Gets and validates a move (L,R,U,D), returns player's new location"""
    isValid = False
    move = []

    # use while loop when getting userinput to validate userinput is either "L", "R", "U", or "D"
    while not isValid:
        playermove = input("Enter your move: ").upper()
        # *ODD BUG* every once in a while my input is ignored??
        if playermove != "U" and playermove != "D" and playermove != "L" and playermove != "R" and playermove != "Q":
            print("Please enter 'U', 'D', 'L', 'R', or 'Q' to quit")
        else:
            if playermove == "U":
                move = 1, 0
            elif playermove == "D":
                move = -1, 0
            elif playermove == "L":
                move = 0, -1
            elif playermove == "R":
                move = 0, 1
            elif playermove == "Q":
                move = 0, 0
            # verifies if move isLegal
            # print("MOVE :" + str(move))  # test trash
            isLegal = legal(dungeonboard, playerlocation, move)
            # verifies if move isValid
            if isLegal:
                isValid = True
    # can not find any information how to do add the values at the same indexes together without zip?
    # zipped_lists = zip(playerlocation, move) #reference for what I need to do but w/o the function
    # move = [x + y for (x, y) in zipped_lists]
    move = (playerlocation[0] + move[0], playerlocation[1] + move[1])
    print("your location: " + str(move))
    return move


def checkMove(dungeonboard, playerlocation, trap, treasure, exit):
    """Checks to verify if a move is onto a space where a game element exists returns return a bool"""
    isOpen = True  # local bool to flag if a space is open or occupied by another game element
    row = playerlocation[0]
    col = playerlocation[1]

    if dungeonboard[row][col] == trap or dungeonboard[row][col] == treasure or dungeonboard[row][col] == exit:
        isOpen = False
        if not isOpen:
            findTrap(dungeonboard, playerlocation)
            findTreasure(dungeonboard, playerlocation)
    # print("isOPen: " + str(isOpen)) # test trash
    return isOpen


def updateDungeon(dungeonboard, currentlocation, newlocation):
    """Moves player to new location, clears previous location"""
    # currentlocation(old location) is cleared
    dungeonboard[currentlocation[0]][currentlocation[1]] = "."

    # Player location is updated with newlocation
    dungeonboard[newlocation[0]][newlocation[1]] = PLAYER

    return newlocation


def findEnd(dungeonboard, row, col):
    """Finds the exit"""
    found = False
    while not found:
        for row in range(row):
            for col in range(col):
                if dungeonboard[row][col] != EXIT:
                    found = False
                else:
                    return row, col


def playAgain():
    """Asks the player if they would like to play again, returns a bool"""
    playagain = False
    yes = "yes"
    no = "no"

    play = input("Do you want to play again?" + "\n" + "Please enter 'yes' or 'no.' ").lower()

    while play != yes and play != no:
        play = input("Enter " + yes + " or " + no + " please ")
    if play == yes:
        playagain = True
    return playagain


# helper functions
def findEmpty(dungeonboard):
    """Finds an empty location for the starting positions of the game elements"""
    isEmpty = False
    while not isEmpty:
        row = randint(0, 9)
        col = randint(0, 9)
        if dungeonboard[row][col] != ".":
            isEmpty = False
        else:
            return row, col


def legal(dungeonboard, playerlocation, move):
    """Checks to see if a player's move is within the indices of the lists"""
    isLegal = False
    if not isLegal:
        if playerlocation[0] + move[0] < 0 or playerlocation[1] + move[1] < 0 or playerlocation[0] + \
                move[0] > len(dungeonboard) - 1 or playerlocation[1] + move[1] > len(dungeonboard) - 1:
            isLegal = False
            print("Out of bounds")
        else:
            isLegal = True
    return isLegal


def findTrap(dungeonboard, newlocation):
    """Finds traps"""
    if dungeonboard[newlocation[0]][newlocation[1]] == TRAP:
        print("ZOIKS!! You fell into a trap")


def findTreasure(dungeonboard, newlocation):
    """Finds traps"""
    if dungeonboard[newlocation[0]][newlocation[1]] == TREASURE:
        print("EUREKA! YOU FOUND TREASURE")
