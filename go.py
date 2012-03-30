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

Open  = 0
Black  = 1
TBlack = 2
White  = 3
TWhite = 4
Outer  = 5

def opponent(player):
    """Return the opponent of player or None if player is not valid."""
    if player == White:
        return Black
    elif player == Black:
        return White
    else:
        return None

class BoardState:
    """Holds one state of the Go board as a list of lists, which is, for all
       intents and purposes, a 2d list. Dimensions extend one unit past the
       edge in each direction -- these outer nodes contain entries called Outer"""
    def __init__(self, to_move = Black, size = 19, existing_state = None):
        self.to_move = to_move
        self.size = size
        if existing_state == None:
            self.board = [Open]*((size+2)**2)
            for index in range(size + 2):
                self.change(index, 0, Outer)
                self.change(index, size + 1, Outer)
                self.change(0, index, Outer)
                self.change(size + 1, index, Outer)
            self.stat_gen()
        else:
            self.board = existing_state.board[:]
    
    # Return the value of the node at row, col
    def get(self, row, col):
        return self.board[row*(self.size + 2) + col]
    
    # Same as get() with row and col in a tuple
    def gett(self, pair):
        return self.board[pair[0]*(self.size + 2) + pair[1]]
    
    # Change the value at row, col to the given value
    # ("set" is a goddamn reserved word...)
    def change(self, row, col, val):
        self.board[row*(self.size + 2) + col] = val
        
    # Same as change() with row and col in a tuple
    def changet(self, pair, val):
        self.board[pair[0]*(self.size + 2) + pair[1]] = val
    
    # Gather legal moves and other potentially useful information in one pass.
    # The responsibility to call this method lies outside this class.
    # Fine-grained properties needed by heuristics should be determined here.
    def stat_gen(self):
        self.legal_move_list = []
        self.black_stone_list = []
        self.white_stone_list = []
        for i in range(self.size + 2):
            for j in range(self.size + 2):
                if self.get(i, j) == Open:
                    self.legal_move_list.append((i,j))
                elif self.get(i, j) == Black:
                    self.black_stone_list.append((i,j))
                elif self.get(i, j) == White:
                    self.white_stone_list.append((i,j))
    
    # Return a list of the stones captured by the given move
    def capture_list(self, move):
        player = self.gett(move)
        caplist = []
        for node in self.adjacent_nodes(move):
            if self.gett(node) != opponent(player):
                continue
            self.rcaplist = []
            self.capture_r(self.gett(move), node)
            for capnode in self.rcaplist:
                if capnode not in caplist:
                    caplist.append(capnode)
        return caplist
    
    # Recursive exploration function called by capture_list()
    def capture_r(self, player, current):
        if current in self.rcaplist:
            return
        self.rcaplist.append(current)
        for node in self.adjacent_nodes(current):
            if self.gett(node) == player:
                continue
            elif self.gett(node) == Outer:
                continue
            elif self.gett(node) == opponent(player):
                self.capture_r(player, node)
            else:
                self.rcaplist = []
                break
    
    # Return the four nodes sharing a side with the given node
    # --> Used by capture_list() and capture_r()
    def adjacent_nodes(self, node):
        return ((node[0]-1, node[1]), (node[0], node[1]-1), \
                (node[0]+1, node[1]), (node[0], node[1]+1))
        
    # Print the board in a more-or-less pretty way
    def display(self):
        letters = 'abcdefghjklmnopqrst'
        print "  ",
        for i in range(self.size):
            print letters[i],
        print ""
        for i in range(1, self.size + 1):
            print "%2d" % (self.size - i + 1),
            for j in range(1, self.size + 1):
                if self.get(i, j) == Black:
                    print 'B',
                elif self.get(i, j) == White:
                    print 'W',
                else:
                    print '.',
            print "" # Carriage return

    # Print the board as a matrix with row and column labels
    def display_matrix(self):
        print "  ",
        for i in range(1, self.size + 1):
            print i%10,
        print ""
        for i in range(1, self.size + 1):
            print "%2d" % i,
            for j in range(1, self.size + 1):
                if self.get(i, j) == Black:
                    print 'B',
                elif self.get(i, j) == White:
                    print 'W',
                else:
                    print '.',
            print "" # Carriage return
                     
    # Print the entire board as integers including the Outer nodes
    def display_debug(self):
        for i in range(self.size + 2):
            for j in range(self.size + 2):
                print self.get(i, j),
            print "" # Carriage return
                     
class Go(Game):
    def __init__(self):
        self.current_state = BoardState()

    # Return a list of legal moves as row-col integer 2-tuples.
    def legal_moves(self, state):
        return state.legal_move_list
    
    # Return a new board with the result of a given move (assumed to be legal).
    def make_move(self, move, state):
        new_state = BoardState(opponent(state.to_move), state.size, state)
        new_state.changet(move, state.to_move)
        for stone in new_state.capture_list(move):
            new_state.changet(stone, Open)
        new_state.stat_gen()
        return new_state
        
    def utility(self, state, player):
        # Something simple for now...
        if player == Black:
            return len(state.black_stone_list) - len(state.white_stone_list)
        else:
            return len(state.white_stone_list) - len(state.black_stone_list)
    
