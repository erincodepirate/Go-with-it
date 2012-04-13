
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
        
class OpheliaM(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.performance = 1.6 / timeit('for i in range(10): oct(i)')
        print "  --> Determined hardware performance factor:", self.performance
        self.endurance, self.mycolor = totalTime / 300., color
                          
    def calculate_utility(self, boardstate):
        return self.friendly_mobility(boardstate)       
             
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (4, None, None)
        
    def friendly_mobility(self, boardstate):
        # Simply returns the number of available moves (negative when it's
        # our opponent's turn)...
        if boardstate.getPlayer() == self.mycolor:
            return len(boardstate.legal_moves())
        else:
            return -len(boardstate.legal_moves())
            
class OpheliaX(othello_player):
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
        return (4, None, None)
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
