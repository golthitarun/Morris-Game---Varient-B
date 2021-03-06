from MorrisGame import *
from Utils import *
import sys

statesReached = 0


def MinMax(board, depth, player1):
    """
    :param board: a board position
    :param depth: maximum depth for min max search
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
            possiblePositions = generateMovesMidgameEndgame([i for i in board])
        else:
            v = sys.maxsize
            possiblePositions = generateMovesMidgameEndgame(InvertBoard([i for i in board]))

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
        finalEvaluator.evaluator = staticEstimationMidgameEndgame(board)
        statesReached += 1

    return finalEvaluator


if __name__ == '__main__':

    file1 = open(sys.argv[1], "r")
    file2 = open(sys.argv[2], "w")
    depth = int(sys.argv[3])

    inBoard = file1.read()
    val = MinMax(inBoard, depth, True)
    file2.write(val.board)

    print("Input Position: "+inBoard+" Output Position: "+val.board)
    print("Position Evaluated by static estimation: "+str(statesReached))
    print("MINMAX estimate: "+str(val.evaluator))