
import sys
from MorrisGame import *
from Utils import *

statesReached = 0


def AlphaBeta(board, depth, player1, alpha, beta):
    """
    :param board: a board position.
    :param depth: maximum depth for min max search.
    :param player1: player1 or not player1
    :param alpha: alpha
    :param beta: beta
    :return: object with next board position and evaluator
    """
    finalEvaluator = evaluator()

    global statesReached

    if depth != 0:
        depth -=1
        currentEvaluator = evaluator()

        if player1:
            v = -sys.maxsize-1
            possiblePositions = generateAdd([i for i in board])
        else:
            v = sys.maxsize
            possiblePositions = generateAdd(InvertBoard([i for i in board]))

        for position in possiblePositions:

            if player1:

                currentEvaluator = AlphaBeta(position, depth, False, alpha, beta)

                if v < currentEvaluator.evaluator:
                    v = currentEvaluator.evaluator
                    finalEvaluator.board = position

                if v >= beta:
                    finalEvaluator.evaluator = v
                    return finalEvaluator
                else:
                    alpha = max(v, alpha)

            else:

                position = "".join(InvertBoard([i for i in position]))
                currentEvaluator = AlphaBeta(position, depth, True, alpha, beta)

                if v > currentEvaluator.evaluator:
                    v = currentEvaluator.evaluator
                    finalEvaluator.board = position

                if v <= alpha:
                    finalEvaluator.evaluator = v
                    return finalEvaluator
                else:
                    beta = min(v, beta)

        finalEvaluator.evaluator = v

    else:
        finalEvaluator.evaluator = staticEstimationOpening(board)
        statesReached += 1

    return finalEvaluator


if __name__ == '__main__':

    file1 = open(sys.argv[1], "r")
    file2 = open(sys.argv[2], "w")
    depth = int(sys.argv[3])

    inBoard = file1.read()

    alpha = -sys.maxsize-1
    beta = sys.maxsize
    val = AlphaBeta(inBoard, depth, True, alpha, beta)

    print("Input Position: "+inBoard+" Output Position: "+val.board)
    print("Position Evaluated by static estimation: "+str(statesReached))
    print("AlphaBeta estimate: "+str(val.evaluator))

