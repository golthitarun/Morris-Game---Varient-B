

def numOfPieces(board,player):
    """
    :param board:
    :param player:
    :return:
    """
    return board.count(player)

def InvertBoard(board):
    """
    :param board: the board b.
    :return: inverted board.
    """
    invertedBoard = board[:]
    for i in range(len(board)):
        if board[i] == "W":
            invertedBoard[i] = "B"
        elif board[i] == "B":
            invertedBoard[i] = "W"

    return invertedBoard

class evaluator():
    def __init__(self):
        self.evaluator = 0
        self.board = []