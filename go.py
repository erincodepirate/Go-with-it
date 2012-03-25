"""Go, built on Norvig's Game class

"""

from utils import *
import random, time

count = 0
testing = 0

def alphabeta_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""
    global count
    global testing
    
    player = game.to_move(state)
    count = 0
    starttime = time.clock()

    def max_value(state, alpha, beta, depth):
        global count, testing
        if testing:
            print "  "* depth, "Max  alpha: ", alpha, " beta: ", beta, " depth: ", depth
        if cutoff_test(state, depth):
            if testing:
                print "  "* depth, "Max cutoff returning ", eval_fn(state)
            return eval_fn(state)
        v = -BigInitialValue
        succ = game.successors(state)
        count = count + len(succ)
        if testing:
            print "  "*depth, "maxDepth: ", depth, "Total:", count, "Successors: ", len(game.successors(state))
        for (a, s) in succ:
            v = max(v, min_value(s, alpha, beta, depth+1))
            if testing:
                print "  "* depth, "max best value:", v
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        global count
        if testing:
            print "  "*depth, "Min  alpha: ", alpha, " beta: ", beta, " depth: ", depth
        if cutoff_test(state, depth):
            if testing:
                print "  "*depth, "Min cutoff returning ", eval_fn(state)
            return eval_fn(state)
        v = BigInitialValue
        succ = game.successors(state)
        count = count + len(succ)
        if testing:
            print "  "*depth, "minDepth: ", depth, "Total:", count, "Successors: ", len(game.successors(state))
        for (a, s) in succ:
            v = min(v, max_value(s, alpha, beta, depth+1))
            if testing:
                print "  "*depth, "min best value:", v
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alphabeta_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or
                   (lambda state,depth: depth>d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state: game.utility(state, game.current_player))
    action, state = argmax(game.successors(state),
                           lambda ((a, s)): min_value(s, -BigInitialValue, BigInitialValue, 0))

    stoptime = time.clock()
    elapsed = stoptime - starttime
    print "Final count: ", count, "Time: ",
    print " %.5f seconds" % elapsed
    return action

class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement
    legal_moves, make_move, utility, and terminal_test. You may
    override display and successors or you can inherit their default
    methods. You will also need to set the .initial attribute to the
    initial state; this can be done in the constructor."""

    def legal_moves(self, state):
        "Return a list of the allowable moves at this point."
        abstract()

    def make_move(self, move, state):
        "Return the state that results from making a move from a state."
        abstract()
            
    def utility(self, state, player):
        "Return the value of this final state to player."
        abstract()

    def terminal_test(self, state):
        "Return True if this is a final state for the game."
        return not self.legal_moves(state)

    def to_move(self, state):
        "Return the player whose move it is in this state."
        return state.to_move

    def display(self, state):
        "Print or otherwise display the state."
        print state

    def successors(self, state):
        "Return a list of legal (move, state) pairs."
        return [(move, self.make_move(move, state))
                for move in self.legal_moves(state)]

    def __repr__(self):
        return '<%s>' % self.__class__.__name__

Blank = 0
Black = 1
White = 2

def opponent(player):
    """Return the opponent of player or None if player is not valid."""
    if player == White:
        return Black
    elif player == Black:
        return White
    else:
        return None

class BoardState:
    """Holds one state of the Go board as a tuple of tuples. Supports only odd
       board sizes greater than or equal to three."""
    def __init__(self, to_move = Black, size = 19, board = None):
        self.to_move = to_move
        if board == None:
            self.board = (Blank, Blank, Blank)
            while len(self.board) < size*size:
                self.board += (Blank, Blank)
        else:
            self.board = board

class Go(Game):
    def legal_moves(self, state):
        pass
    
    def make_move(self, move, state):
        new_board = BoardState(opponent(state.to_move), state.size, \
                    tuple(board[:move], state.to_move, board[move + 1:]))
        
    
    def utility(self, state, player)
        pass

