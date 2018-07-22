from Utils import *
import sys

def neighbors(location):
    """
    :param location: a location j in the array representing the board.
    :param board: the board b.
    :return: a list of locations in the array corresponding to j's neighbors
    """

    neighbors = {
        0: [1, 2, 6],
        1: [0, 11],
        2: [0, 4, 7, 3],
        3: [2, 10],
        4: [2, 8, 5],
        5: [4, 9],
        6: [0, 7, 18],
        7: [2, 6, 8, 15],
        8: [4, 7, 12],
        9: [5, 10, 14],
        10: [3, 9, 11, 17],
        11: [1, 10, 20],
        12: [8, 13],
        13: [12, 14, 16],
        14: [13, 9],
        15: [7, 16],
        16: [13, 15, 17, 11],
        17: [16, 10],
        18: [6, 19],
        19: [18, 16, 20],
        20: [11, 19],
    }[location]

    return neighbors


def closeMill(location, board):
    """
    :param location: a location j in the array representing the board.
    :param board: the board b.
    :return: true if the move to j closes a mill.
    """
    C = board[location]
    mill = {
        0: (board[6] == C and board[18] == C) or (board[2] == C and board[4] == C),
        6: (board[7] == C and board[8] == C) or (board[0] == C and board[18] == C),
        18: (board[0] == C and board[6] == C) or (board[19] == C and board[20] == C),
        2: (board[0] == C and board[4] == C) or (board[7] == C and board[15] == C),
        7: (board[2] == C and board[15] == C) or (board[6] == C and board[8] == C),
        15: (board[2] == C and board[7] == C) or (board[16] == C and board[17] == C),
        4: (board[2] == C and board[0] == C) or (board[8] == C and board[12] == C),
        8: (board[4] == C and board[12] == C) or (board[6] == C and board[7] == C),
        12: (board[8] == C and board[4] == C) or (board[13] == C and board[14] == C),
        13: (board[12] == C and board[14] == C) or (board[16] == C and board[19] == C),
        16: (board[13] == C and board[19] == C) or (board[15] == C and board[17] == C),
        19: (board[16] == C and board[13] == C) or (board[18] == C and board[20] == C),
        5: (board[9] == C and board[14] == C),
        9: (board[5] == C and board[14] == C) or (board[10] == C and board[11] == C),
        14: (board[9] == C and board[5] == C) or (board[12] == C and board[13] == C),
        3: (board[10] == C and board[17] == C),
        10: (board[3] == C and board[17] == C) or (board[9] == C and board[11] == C),
        17: (board[3] == C and board[10] == C) or (board[15] == C and board[16] == C),
        1: (board[11] == C and board[20] == C),
        11: (board[1] == C and board[20] == C) or (board[9] == C and board[10] == C),
        20: (board[1] == C and board[11] == C) or (board[18] == C and board[19] == C),
    }[location]

    return mill


def generateRemove(board, L):
    """
    :param board: a board position.
    :param L: a list L of board positions.
    :return: NIL.
    positions are added to L by removing black pieces.
    """
    for location in range(len(board)):
        if board[location] == "B":
            if not closeMill(location,board):
                b = board[:]
                b[location] = "x"
                L.append("".join(b))

    # TODO: If no positions were added (all black pieces are in mills) add b to L.


def generateAdd(board):
    """
    :param board: a board position.
    :return: a list L of board positions.
    """
    L = []
    for location in range(len(board)):
        if board[location] == "x":
            b = board[:]
            b[location] = "W"
            if closeMill(location, b):
                generateRemove(b, L)
            else:
                L.append("".join(b))
    return L


def generateMove(board):
    """
    :param board: a board position.
    :return: a list L of board positions.
    """
    L = []
    for location in range(len(board)):
        if board[location] == "W":
            n = neighbors(location)
            for j in n:
                if board[j] == "x":
                    b = board[:]
                    b[location] = "x"
                    b[j] = "W"
                    if closeMill(j, b):
                        generateRemove(b, L)
                    else:
                        L.append("".join(b))
    return L


def generateHopping( board):
    """
    :param board: a board position.
    :return: a list L of board positions.
    """
    L = []
    for location1 in range(len(board)):
        if board[location1] == "W":
            for location2 in range(len(board)):
                if board[location2] == "x":
                    b = board[:]
                    b[location1] = "x"
                    b[location2] = "W"
                    if closeMill(location2, b):
                        generateRemove(b, L)
                    else:
                        L.append("".join(b))
    return L


def generateMovesMidgameEndgame(board):
    """
    :param board: a board position.
    :return: a list L of board positions.
    """
    if numOfPieces(board, "W") == 3:
        return generateHopping(board)
    else:
        return generateMove(board)


def possibleMillCount(board, player):
    """
    :param board: a board position.
    :return:
    """
    count = 0

    for i in range(len(board)):
        if board[i] == "x":
            board[i] = player
            if closeMill(i, board):
                count += 1
            board[i] = "x"
    return count


def potentialMillInFormation(position, board, player):
    """
    :param position:
    :param board:
    :param player:
    :return:
    """
    adjacent_list = neighbors(position)

    for i in adjacent_list:
        if board[i] == player:
            tmp = board[position]
            board[position] = player
            if not closeMill(position, board):
                board[position] = tmp
                return True
            board[position] = tmp
    return False


def piecesInPotentialMillFormation(board, player):
    """
    :param board:
    :param player:
    :return:
    """
    count = 0

    for i in range(len(board)):
        if board[i] == player:
            adjacent_list = neighbors(i)
            for pos in adjacent_list:
                if player == "W":
                    if board[pos] == "B":
                        board[i] = "B"
                        if closeMill(i, board):
                            count += 1
                        board[i] = player
                else:
                    if board[pos] == "W" and potentialMillInFormation(pos, board, "W"):
                        count += 1
    return count


def staticEstimationOpening(board):
    """
    :param board: a board position.
    :return: static estimation for the opening.
    """
    return numOfPieces(board, "W") - numOfPieces(board, "B")


def staticEstimationMidgameEndgame(board):
    """
    :param board: a board position.
    :return: static estimation for the midgame endgame.
    """
    numBlackMoves = len(generateMovesMidgameEndgame(InvertBoard([i for i in board])))

    if numOfPieces(board, "B") <= 2:
        return 10000
    elif numOfPieces(board, "W") <= 2:
        return -10000
    elif numBlackMoves == 0:
        return 10000
    else:
        return 1000*(numOfPieces(board, "W") - numOfPieces(board, "B")) - numBlackMoves


def staticEstimationImprovedOpening(board):
    """
    :param board: a board position.
    :return: improved static estimate.

    This Looks at the number of pieces on the board and
    the potential mills that can be formed.
    """
    evaluation = 0

    whitePieces = numOfPieces(board, "W")
    blackPieces = numOfPieces(board, "B")

    numOfPossibleMillsWhite = possibleMillCount(board, "W")
    numOfPossibleMillsBlack = possibleMillCount(board, "B")

    movablePiecesWhite = 0
    movablePiecesBlack = 0

    potentialMillsWhite = piecesInPotentialMillFormation(board, "W")
    potentialMillsBlack = piecesInPotentialMillFormation(board, "B")

    if whitePieces < 4:
        evaluation += 100 * numOfPossibleMillsWhite
        evaluation += 200 * potentialMillsBlack
    else:
        evaluation += 200 * numOfPossibleMillsWhite
        evaluation += 100 * potentialMillsBlack

    evaluation -= 25 * movablePiecesBlack
    evaluation += 50 * (whitePieces - blackPieces)

    return evaluation


def staticEstimationImprovedMidgameEndgame(board):
    """
    :param board: a board position.
    :return: improved static estimate.

    This Looks at the number of pieces on the board and
    the potential mills that can be formed.
    """
    evaluation = 0

    whitePieces = numOfPieces(board, "W")
    blackPieces = numOfPieces(board, "B")

    numOfPossibleMillsWhite = possibleMillCount(board, "W")
    numOfPossibleMillsBlack = possibleMillCount(board, "B")

    movablePiecesWhite = 0
    movablePiecesBlack = 0

    movablePiecesBlack_2 = len(generateMovesMidgameEndgame(board))

    potentialMillsWhite = piecesInPotentialMillFormation(board, "W")
    potentialMillsBlack = piecesInPotentialMillFormation(board, "B")

    if blackPieces <= 2 or movablePiecesBlack_2 == 0:
        evaluation = sys.maxsize
    elif whitePieces <= 2:
        evaluation = -sys.maxsize-1
    else:
        if whitePieces < 4:
            evaluation += 100 * numOfPossibleMillsWhite
            evaluation += 200 * potentialMillsBlack
        else:
            evaluation += 200 * numOfPossibleMillsWhite
            evaluation += 100 * potentialMillsBlack
        evaluation -= 25 * movablePiecesBlack_2
        evaluation += 50 * (whitePieces - blackPieces)

    return evaluation
