import random

winning_combinations = [[1,2,3],[4,5,6],[7,8,9],
                        [1,4,7],[2,5,8],[3,6,9],
                        [1,5,9],[3,5,7]]

occupied = []
positions = [i for i in range(1,10)]
def gameBoard():
    print("""
    {}  |  {}  |  {}
    --------------
    {}  |  {}  |  {}
    --------------
    {}  |  {}  |  {}
    """.format(positions[0], positions[1], positions[2],
               positions[3], positions[4], positions[5],
               positions[6], positions[7], positions[8]))

def checkWinner(ch, pos):
    pass

def userMove(ch):
    pass

def cpuMove(ch):
    pass

def main():
    gameBoard()
    # Take Choice from User as Input
    ch = input("Enter your choice : 0/X : ")
    if ch == "X":
        cpu = "0"
    else:
        cpu = "X"
    # Start while until we get a winner
        # Call UserMove
        # Call CpuMove
    while True:
        userMove(ch)
        gameBoard()
        cpuMove(cpu)

main()