from constants import MAX_SIZE, TRAP, TREASURE, EXIT
from random import randint
import dungeon


def main():
    # variables:
    traps = randint(5, 15)
    treasures = randint(3, 8)
    play = True

    # game board(10 rows, 10 columns)
    # dungeonboard = [["."] * MAX_SIZE for i in range(MAX_SIZE)]


    while play:
        dungeonboard = []
        for index in range(MAX_SIZE):
            dungeonboard.append(["."] * MAX_SIZE)
        playerlocation = -1, -1
        newlocation = -1, -1
        win = lose = False

        currentlocation = dungeon.createDungeon(dungeonboard, traps, treasures)  # create dungeon
        dungeon.displayInstructions()

        while not win and not lose:
            dungeon.displayDungeon(dungeonboard)  # display the board
            newlocation = dungeon.getMove(currentlocation, dungeonboard)  # checks to see if move is valid
            if newlocation == currentlocation:  # if playerlocation has not moved player has chosen to quit the game
                lose = True
            dungeon.checkMove(dungeonboard, newlocation, TRAP, TREASURE, EXIT)
            endLocation = dungeon.findEnd(dungeonboard, MAX_SIZE, MAX_SIZE)
            if newlocation == endLocation:
                print("You have found the exit!")
                win = True
            newlocation = dungeon.updateDungeon(dungeonboard, currentlocation, newlocation)  # updates player move
            currentlocation = newlocation

        play = dungeon.playAgain()


if __name__ == '__main__':
    main()
