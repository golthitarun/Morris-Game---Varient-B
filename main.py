from MiniMaxOpening import MinMax as MinMaxOpen
from MiniMaxGame import MinMax as MinMaxGame
from ABOpening import AlphaBeta as ABOpen
from ABGame import AlphaBeta as ABGame
import sys
alpha = sys.maxsize
beta = -sys.maxsize-1
def AIvsAI():
    board = ["x" for _ in range(21)]

    print("*********** Stage - 1 ************")
    for i in range(9):

        evalBoard = MinMaxOpen(board, 6, True)

        print("AI Bot 1 Opening Move - ", evalBoard.board, " | Evaluator - ",evalBoard.evaluator)
        if evalBoard.evaluator == sys.maxsize:
            print("AI Bot 1 has won!")
            exit(0)
        else:
            board = evalBoard.board

        evalBoard = MinMaxOpen(board, 6, False)

        print("AI Bot 2 Opening Move - ",evalBoard.board," | Evaluator - ",evalBoard.evaluator)
        if evalBoard.evaluator == -sys.maxsize-1:
            print("AI Bot 2 has won!")
            exit(0)
        else:
            board = evalBoard.board

    print("*********** Stage - 2 ************")

    while(True):

        evalBoard = MinMaxGame(board, 6, True)
        print("AI Bot 1 Game Move - ", evalBoard.board," | Evaluator - ",evalBoard.evaluator)
        if evalBoard.evaluator == sys.maxsize:
            print("AI Bot 1 has won!")
            exit(0)
        else:
            board = evalBoard.board

        evalBoard = MinMaxGame(board, 6, False)

        print("AI Bot 2 Game Move - ",evalBoard.board," | Evaluator - ",evalBoard.evaluator)
        if evalBoard.evaluator == -sys.maxsize-1:
            print("AI Bot 2 has won!")
            exit(0)
        else:
            board = evalBoard.board


if __name__ == "__main__":
    AIvsAI()
