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
    x_count = 0
    y_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                y_count += 1
            else:
                continue
    if x_count > y_count:
        return O
    elif y_count > x_count:
        return X
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set() ## {(,)}
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is EMPTY:
                actions.add((i, j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action")

    result = copy.deepcopy(board)
    row, col = action
    result[row][col] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    x_places = set()
    o_places = set()

    solutions = [
        {(0, 0), (0, 1), (0, 2)},
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},
        {(0, 0), (1, 0), (2, 0)},
        {(0, 1), (1, 1), (2, 1)},
        {(0, 2), (1, 2), (2, 2)},
        {(0, 0), (1, 1), (2, 2)},
        {(0, 2), (1, 1), (2, 0)}
    ]

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is X:
                x_places.add((i, j))
            elif cell is O:
                o_places.add((i, j))

    for solution in solutions:
        if solution.issubset(x_places):
            return X
        elif solution.issubset(o_places):
            return O


    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    elif winner(board) == O:
        return True

    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False

    return True





def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board, alpha, beta):

    v = -math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)

    return v

def min_value(board, alpha, beta):

    v = math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board, action), -math.inf, math.inf), action])
        return sorted(plays, key=lambda x: x[0], reverse = True)[0][1]

    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board, action), -math.inf, math.inf), action])
        return sorted(plays, key=lambda x: x[0])[0][1]


'''
with no alpha-beta puring: 

def max_value(board):

    v = -math.inf

    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):

    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0], reverse = True)[0][1]

    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board, action)), action])
        return sorted(plays, key=lambda x: x[0])[0][1]

'''

