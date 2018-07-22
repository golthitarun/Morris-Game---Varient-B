import sys
from MorrisGame import *
from Utils import *

statesReached = 0


def MinMax(board, depth, player1):
    """
    :param board: a board position
    :param depth: depth to check using min max
    :param player1: player1 or not player 1
    :return: object with next board position and evalutor.
    """
    global statesReached
    finalEvaluator = evaluator()

    if depth != 0:

        depth -= 1
        currentEvaluator = evaluator()

        if player1:
            v = -sys.maxsize-1
            possiblePositions = generateAdd([i for i in board])
        else:
            v = sys.maxsize
            possiblePositions = generateAdd(InvertBoard([i for i in board]))

        for position in possiblePositions:

            if player1:
                currentEvaluator = MinMax(position, depth, False)
                if v < currentEvaluator.evaluator:
                    v = currentEvaluator.evaluator
                    finalEvaluator.board = position
            else:
                position = "".join(InvertBoard([i for i in position]))
                currentEvaluator = MinMax(position, depth, True)
                if v > currentEvaluator.evaluator:
                    v = currentEvaluator.evaluator
                    finalEvaluator.board = position

        finalEvaluator.evaluator = v
    else:
        finalEvaluator.evaluator = staticEstimationOpening(board)
        statesReached += 1

    return finalEvaluator


if __name__ == "__main__":

    file1 = open(sys.argv[1], "r")
    file2 = open(sys.argv[2], "w")
    depth = int(sys.argv[3])

    inBoard = file1.read()
    inBoardInverted = InvertBoard([i for i in inBoard])

    val = MinMax(inBoardInverted, depth, True)

    outBoard = "".join(InvertBoard([i for i in val.board]))

    print("Input Position: "+inBoard+" Output Position: "+outBoard)
    print("Position Evaluated by static estimation: "+str(statesReached))
    print("MINMAX estimate: "+str(val.evaluator))