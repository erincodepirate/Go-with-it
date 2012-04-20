# Othello Player list to be used against the weighted player

from othello import *

class Straight2(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
    def calculate_utility(self, boardstate):
        return self.mycount_difference(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (2, None, None)
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))

class Straight3(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
    def calculate_utility(self, boardstate):
        return self.mycount_difference(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (3, None, None)
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))

class Straight4(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
        pass;
    def calculate_utility(self, boardstate):
        return self.mycount_difference(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (4, None, None)
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))
                
class Straight6(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
        pass;
    def calculate_utility(self, boardstate):
        return self.mycount_difference(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (6, None, None)
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))

class TableStraight2(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
        self.value_table = [ 10, -1,  4,  2, \
                             -1, -1,  2,  1, \
                              4,  2,  2,  1, \
                              2,  1,  1,  1  ]
    def calculate_utility(self, boardstate):
        return self.table_eval(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (2, None, None)
    def table_eval(self, boardstate):
        piecemap = boardstate.getPieces()
        presence_table = [0] * 16
        for entry in piecemap:
            row = 7 - entry[0] if entry[0] > 3 else entry[0]
            col = 7 - entry[1] if entry[1] > 3 else entry[1]
            niceness = 1 if piecemap[entry] == self.mycolor else -1
            presence_table[4*row + col] += niceness
        result = 0
        for i in range(16):
            result += self.value_table[i] * presence_table[i];
        return result

    
class FastTableStraight2(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
        self.table = [ 10, -1,  4,  2, \
                       -1, -1,  2,  1, \
                        4,  2,  2,  1, \
                        2,  1,  1,  1  ]
    def calculate_utility(self, boardstate):
        return self.table_eval(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (2, None, None)
    def table_eval(self, boardstate):
        piecemap, result = boardstate.getPieces(), 0
        for entry in piecemap:
            row = 7 - entry[0] if entry[0] > 3 else entry[0]
            col = 7 - entry[1] if entry[1] > 3 else entry[1]
            niceness = 1 if piecemap[entry] == self.mycolor else -1
            result += self.table[4*row + col] * niceness
        return result
        
class FastTableStraight4(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
        self.table = [ 10, -1,  4,  2, \
                       -1, -1,  2,  1, \
                        4,  2,  2,  1, \
                        2,  1,  1,  1  ]
    def calculate_utility(self, boardstate):
        return self.table_eval(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (4, None, None)
    def table_eval(self, boardstate):
        piecemap, result = boardstate.getPieces(), 0
        for entry in piecemap:
            row = 7 - entry[0] if entry[0] > 3 else entry[0]
            col = 7 - entry[1] if entry[1] > 3 else entry[1]
            niceness = 1 if piecemap[entry] == self.mycolor else -1
            result += self.table[4*row + col] * niceness
        return result

class FancyTable2(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
        self.table_1 = [ 10, -1,  4,  2, \
                         -1, -1,  2,  1, \
                          4,  2,  2,  1, \
                          2,  1,  1,  1  ]
        self.table_2 = [ 10,  3,  3,  3, \
                          3,  1,  2,  1, \
                          3,  2,  1,  1, \
                          3,  1,  1,  1  ]
    def calculate_utility(self, boardstate):
        return self.table_eval(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (2, None, None)
    def table_eval(self, boardstate):
        piecemap = boardstate.getPieces()
        cornerlist = []
        if (0,0) in piecemap: cornerlist.append(0)
        if (0,7) in piecemap: cornerlist.append(1)
        if (7,0) in piecemap: cornerlist.append(2)
        if (7,7) in piecemap: cornerlist.append(3)
        result = 0
        for entry in piecemap:
            niceness = 1 if piecemap[entry] == self.mycolor else -1
            quadrant = 0
            if entry[0] > 3:
                row = 7 - entry[0]
                quadrant += 2
            else:
                row = entry[0]
            if entry[1] > 3:
                col = 7 - entry[1]
                quadrant += 1
            else:
                col = entry[1]
            if quadrant in cornerlist:
                result += self.table_2[4*row + col] * niceness
            else:
                result += self.table_1[4*row + col] * niceness
        return result
        
class FancyTable4(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
        self.table_1 = [ 10, -1,  4,  2, \
                         -1, -1,  2,  1, \
                          4,  2,  2,  1, \
                          2,  1,  1,  1  ]
        self.table_2 = [ 10,  3,  3,  3, \
                          3,  1,  2,  1, \
                          3,  2,  1,  1, \
                          3,  1,  1,  1  ]
    def calculate_utility(self, boardstate):
        return self.table_eval(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (4, None, None)
    def table_eval(self, boardstate):
        piecemap = boardstate.getPieces()
        cornerlist = []
        if (0,0) in piecemap: cornerlist.append(0)
        if (0,7) in piecemap: cornerlist.append(1)
        if (7,0) in piecemap: cornerlist.append(2)
        if (7,7) in piecemap: cornerlist.append(3)
        result = 0
        for entry in piecemap:
            niceness = 1 if piecemap[entry] == self.mycolor else -1
            quadrant = 0
            if entry[0] > 3:
                row = 7 - entry[0]
                quadrant += 2
            else:
                row = entry[0]
            if entry[1] > 3:
                col = 7 - entry[1]
                quadrant += 1
            else:
                col = entry[1]
            if quadrant in cornerlist:
                result += self.table_2[4*row + col] * niceness
            else:
                result += self.table_1[4*row + col] * niceness
        return result
        
class Mobility2(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        self.mycolor = color
                          
    def calculate_utility(self, boardstate):
        return self.friendly_mobility(boardstate)       
             
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (2, None, None)
        
    def friendly_mobility(self, boardstate):
        # Simply returns the number of available moves (negative when it's
        # our opponent's turn)...
        if boardstate.getPlayer() == self.mycolor:
            return len(boardstate.legal_moves())
        else:
            return -len(boardstate.legal_moves())
            
class OpheliaX2(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing..."
        self.mycolor = color
        self.table = [ 10, -1,  4,  2, \
                       -1, -1,  2,  1, \
                        4,  2,  2,  1, \
                        2,  1,  1,  1  ]              
    def calculate_utility(self, boardstate):
        return     self.utility_table(boardstate) \
             + 3 * self.friendly_mobility(boardstate)       
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (2, None, None)
    def friendly_mobility(self, boardstate):
        if boardstate.getPlayer() == self.mycolor:
            return len(boardstate.legal_moves())
        else:
            return -len(boardstate.legal_moves())
    def utility_table(self, boardstate):
        piecemap, result = boardstate.getPieces(), 0
        for entry in piecemap:
            row = 7 - entry[0] if entry[0] > 3 else entry[0]
            col = 7 - entry[1] if entry[1] > 3 else entry[1]
            niceness = 1 if piecemap[entry] == self.mycolor else -1
            result += self.table[4 * row + col] * niceness
        return result

class AEPlayer2(othello_player):
    #  This will be called once at the beginning of the game, after
    #  a few random moves have been made.  Boardstate is the initial
    #  boardstate for the game, totalTime is the total amount of time
    #  (in seconds) in the range 60-1800 that your player will get for
    #  the game.  For our tournament, I will generally set this to 300.
    #  color is one of Black or White (which are just constants defined
    #  in the othello.py file) saying what color the player will be
    #  playing.
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
        # get the other player's color for use in heuristics
        if color == 1:
            self.opcolor = 2
        else:
            self.opcolor = 1
        # store the positions of the corners of the board for use
        # in our heuristics
        self.corners = [11, 18, 81, 88]

        pass;
    # This should return the utility of the given boardstate.
    # It can access (but not modify) the to_move and _board fields.
    def calculate_utility(self, boardstate):
        value = self.mycount_difference(boardstate)
        
        for i in self.corners:
            # even values of i check back one step, odd
            # values check forward one step
            if i%2 == 1:
                j = i + 1
            else:
                j = i - 1
                # if its at the top of the board go down 10 and check
                # otherwise go up 10
                if i < 80:
                    k = 10
                else:
                    k = -10
                # if a corner is taken then add to value
                if boardstate._board[i] == self.mycolor:
                    value = value + 20
                else:
                    # if an oponent takes a corner then you have bad news
                    if boardstate._board[i] == self.opcolor:
                        value = value - 20
                    # otherwise being near that corner subtracts from value
                    if boardstate._board[j] == self.mycolor:
                        value = value - 10
                    if boardstate._board[i+k] == self.mycolor:
                        value = value - 10
                    if boardstate._board[j+k] == self.mycolor:
                        value = value - 10
                # an opponent being near a corner does a body good
                if boardstate._board[j] == self.opcolor:
                    value = value + 10
                if boardstate._board[i+k] == self.opcolor:
                    value = value + 10
                if boardstate._board[j+k] == self.opcolor:
                    value = value + 10
        return value
    def alphabeta_parameters(self, boardstate, remainingTime):
        # This should return a tuple of (cutoffDepth, cutoffTest, evalFn)
        # where any (or all) of the values can be None, in which case the
        # default values are used:
        #        cutoffDepth default is 4
        #        cutoffTest default is None, which just uses cutoffDepth to
        #            determine whether to cutoff search
        #        evalFn default is None, which uses your boardstate_utility_fn
        #            to evaluate the utility of board states.
        # check to depth 4 as long as there is more than 45 seconds left
#       if remainingTime > 100:
#               return (4, None, None)
        # check depth 2 if you are running out of time
#       else:
        return (2, None, None)
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))

def count_difference(boardstate):
    return (boardstate._board.count(boardstate.to_move)
            - boardstate._board.count(opponent(boardstate.to_move)))

