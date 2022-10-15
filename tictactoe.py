"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # raise NotImplementedError
    countx = 0
    counto = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == O:
                counto += 1
            elif board[i][j] == X:
                countx += 1
    if countx > counto:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError

    action = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action.add((i, j))

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    if action not in actions(board):
        raise Exception("Not a valid action")

    newBoard = copy.deepcopy(board)
    # newBoard[action[0], action[1]] = player(board)

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    def check1(board, player):
        for i in range(len(board)):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                return True
        return False

    def check2(board, player):
        for j in range(len(board)):
            if board[0][j] == player and board[1][j] == player and board[2][j] == player:
                return True
        return False

    def check3(board, player):
        w = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == j and board[i][j] == player:
                    w += 1
        if w == 3:
            return True
        return False

    def check4(board, player):
        w = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == j and board[i][len(board)-i-1] == player:
                    w += 1
        if w == 3:
            return True
        return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError

    if winner(board) == X:
        return True
    if winner(board) == O:
        return True

    for i in range(len(board)):
        for j in range(len(board(i))):
            if board[i][j] == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError

    def min(board):
        w = math.inf
        if terminal(board):
            return utility(board)
        for action in actions(board):
            w = min(w, max(result(board, action)))

    if terminal(board):
        return None
    elif player(board) == X:
        game = []
        for action in actions(board):
