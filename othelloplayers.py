
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

class TimeManaging(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
    def calculate_utility(self, boardstate):
        return self.mycount_difference(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        if remainingTime < 90:
                return (2, None, None)
        if remainingTime < 180:
                return (4, None, None)
        return (6, None, None)

    def mycount_difference(self, boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))

class ProgressManaging(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name
        self.mycolor = color
    def calculate_utility(self, boardstate):
        return self.mycount_difference(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        if len(boardstate.getPieces()) < 7:
            return (4, None, None)
        if remainingTime < 90:
            return (2, None, None)
        if remainingTime < 180:
            return (4, None, None)
        return (6, None, None)
    
    def mycount_difference(self, boardstate):
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
        
class SexyTable(othello_player):
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
        if len(boardstate.getPieces()) < 20 or len(boardstate.getPieces()) > 54:
            return (2, None, None)
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
                result += self.table_2[4 * row + col] * niceness
            else:
                result += self.table_1[4 * row + col] * niceness
        return result
        
class SexyTableA(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.sluggishness = timeit('for i in range(10): oct(i)') / 1.5
        print "  --> Determined hardware sluggishness factor:", self.sluggishness
        self.endurance = totalTime / 300.
        self.lastRemainingTime, self.peakTime = totalTime, 0
        self.mycolor = color
        self.table_A = [ 10, -1,  4,  2, \
                         -1, -1,  2,  1, \
                          4,  2,  2,  1, \
                          2,  1,  1,  1  ]
        self.table_B = [ 10,  3,  3,  3, \
                          3,  1,  1,  1, \
                          3,  1,  1,  1, \
                          3,  1,  1,  1  ]
    def calculate_utility(self, boardstate):
        return self.table_eval(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        
        # Force depth 2 if time is short...
        if self.lastRemainingTime - remainingTime > self.peakTime:
            self.peakTime = self.lastRemainingTime - remainingTime
        self.lastRemainingTime = remainingTime
        if self.peakTime > remainingTime:
            return (2, None, None)
        
        # Use depth 4 in the largest window the resources allow...
        if len(boardstate.getPieces()) < 22 * self.sluggishness / self.endurance \
        or len(boardstate.getPieces()) > 64 - 8 * self.sluggishness / self.endurance:
            return (2, None, None)
        return (4, None, None)
        
    def table_eval(self, boardstate):
        # For each quadrant of the board we note whether that corner has been taken.
        # If it has, we value pieces in that quadrant according to table_B, which
        # doesn't care about the immediate neighbors of the corner -- if not, we
        # value according to table_A, which doesn't like those dangerous neighbors.
        piecemap, cornerlist = boardstate.getPieces(), []
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
                result += self.table_B[4 * row + col] * niceness
            else:
                result += self.table_A[4 * row + col] * niceness
        return result
        
class SexyTableB(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.sluggishness = timeit('for i in range(10): oct(i)') / 1.5
        print "  --> Determined hardware sluggishness factor:", self.sluggishness
        self.endurance = totalTime / 300.
        self.lastRemainingTime, self.peakTime = totalTime, 0
        self.mycolor = color
        self.table_A = [ 10, -1,  4,  2, \
                         -1, -1,  2,  1, \
                          4,  2,  2,  1, \
                          2,  1,  1,  1  ]
        self.table_B = [ 10,  3,  3,  3, \
                          3,  1,  2,  1, \
                          3,  2,  1,  1, \
                          3,  1,  1,  1  ]
    def calculate_utility(self, boardstate):
        return self.table_eval(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        
        # Force depth 2 if time is short...
        if self.lastRemainingTime - remainingTime > self.peakTime:
            self.peakTime = self.lastRemainingTime - remainingTime
        self.lastRemainingTime = remainingTime
        if self.peakTime > remainingTime:
            return (2, None, None)
        
        # Use depth 4 in the largest window the resources allow...
        if len(boardstate.getPieces()) < 20 * self.sluggishness / self.endurance \
        or len(boardstate.getPieces()) > 64 - 10 * self.sluggishness / self.endurance:
            return (2, None, None)
        return (4, None, None)
        
    def table_eval(self, boardstate):
        # For each quadrant of the board we note whether that corner has been taken.
        # If it has, we value pieces in that quadrant according to table_B, which
        # doesn't care about the immediate neighbors of the corner -- if not, we
        # value according to table_A, which doesn't like those dangerous neighbors.
        piecemap, cornerlist = boardstate.getPieces(), []
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
                result += self.table_B[4 * row + col] * niceness
            else:
                result += self.table_A[4 * row + col] * niceness
        return result
        
class SexyTableC(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.sluggishness = timeit('for i in range(10): oct(i)') / 1.5
        print "  --> Determined hardware sluggishness factor:", self.sluggishness
        self.endurance = totalTime / 300.
        self.lastRemainingTime, self.peakTime = totalTime, 0
        self.mycolor = color
        self.table_A = [ 10, -1,  4,  2, \
                         -1, -1,  2,  1, \
                          4,  2,  2,  1, \
                          2,  1,  1,  1  ]
        self.table_B = [ 10,  3,  3,  3, \
                          3,  1,  2,  1, \
                          3,  2,  2,  1, \
                          3,  1,  1,  1  ]
    def calculate_utility(self, boardstate):
        return self.table_eval(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        
        # Force depth 2 if time is short...
        if self.lastRemainingTime - remainingTime > self.peakTime:
            self.peakTime = self.lastRemainingTime - remainingTime
        self.lastRemainingTime = remainingTime
        if self.peakTime > remainingTime:
            return (2, None, None)
        
        # Use depth 4 in the largest window the resources allow...
        if len(boardstate.getPieces()) < 20 * self.sluggishness / self.endurance \
        or len(boardstate.getPieces()) > 64 - 10 * self.sluggishness / self.endurance:
            return (2, None, None)
        return (4, None, None)
        
    def table_eval(self, boardstate):
        # For each quadrant of the board we note whether that corner has been taken.
        # If it has, we value pieces in that quadrant according to table_B, which
        # doesn't care about the immediate neighbors of the corner -- if not, we
        # value according to table_A, which doesn't like those dangerous neighbors.
        piecemap, cornerlist = boardstate.getPieces(), []
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
                result += self.table_B[4 * row + col] * niceness
            else:
                result += self.table_A[4 * row + col] * niceness
        return result
        
class OpheliaA(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.sluggishness = timeit('for i in range(10): oct(i)') / 1.6
        print "  --> Determined hardware sluggishness factor:", self.sluggishness
        self.endurance = totalTime / 300.
        self.lastRemainingTime, self.peakTime = totalTime, 0
        self.mycolor = color
        self.table_A = [ 10, -1,  4,  2, \
                         -1, -1,  2,  1, \
                          4,  2,  2,  1, \
                          2,  1,  1,  1  ]
        self.table_B = [ 10,  3,  3,  3, \
                          3,  1,  1,  1, \
                          3,  1,  1,  1, \
                          3,  1,  1,  1  ]
    def calculate_utility(self, boardstate):
        return self.table_eval(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        
        piecemap = boardstate.getPieces()

        # Use the simple difference utility function during the endgame
        # when it's all about the score...
        if len(piecemap) > 56:
            utility_function = self.count_difference
        else:
            utility_function = self.table_eval
        
        # Force depth 2 if time is short...
        if self.lastRemainingTime - remainingTime > self.peakTime:
            self.peakTime = self.lastRemainingTime - remainingTime
        self.lastRemainingTime = remainingTime
        if self.peakTime > remainingTime:
            return (2, None, utility_function)
        
        # Use depth 4 in the largest window the resources allow...
        if len(piecemap) < 22 * self.sluggishness / self.endurance \
        or len(piecemap) > 64 - 8 * self.sluggishness / self.endurance:
            return (2, None, utility_function)
        return (4, None, utility_function)
        
    def table_eval(self, boardstate):
        # For each quadrant of the board we note whether that corner has been taken.
        # If it has, we value pieces in that quadrant according to table_B, which
        # doesn't care about the immediate neighbors of the corner -- if not, we
        # value according to table_A, which doesn't like those dangerous neighbors.
        piecemap, cornerlist = boardstate.getPieces(), []
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
                result += self.table_B[4 * row + col] * niceness
            else:
                result += self.table_A[4 * row + col] * niceness
        return result
        
    def count_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))
                
      
class OpheliaB(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.performance = 1.6 / timeit('for i in range(10): oct(i)')
        print "  --> Determined hardware performance factor:", self.performance
        self.endurance = totalTime / 300.
        self.lastRemainingTime, self.peakTime = totalTime, 0
        self.mycolor = color
        self.table = [ 10, -1,  4,  2, \
                       -1, -1,  2,  1, \
                        4,  2,  2,  1, \
                        2,  1,  1,  1  ]
    def calculate_utility(self, boardstate):
        return self.table_eval(boardstate)
    def alphabeta_parameters(self, boardstate, remainingTime):
        
        piecemap = boardstate.getPieces()

        # Use the simple difference utility function during the endgame
        # when it's all about the score...
        if len(piecemap) > 57:
            utility_function = self.count_difference
        else:
            utility_function = self.table_eval
        
        # Force depth 2 if time is short...
        if self.lastRemainingTime - remainingTime > self.peakTime:
            self.peakTime = self.lastRemainingTime - remainingTime
        self.lastRemainingTime = remainingTime
        if self.peakTime > remainingTime:
            return (2, None, utility_function)
        
        # Use depth 4 in the largest window the resources allow...
        if len(piecemap) < 20 / (self.performance * self.endurance) \
        or len(piecemap) > 64 - 10 / (self.performance * self.endurance):
            return (2, None, utility_function)
        return (4, None, utility_function)
        
    def table_eval(self, boardstate):
        piecemap, result = boardstate.getPieces(), 0
        for entry in piecemap:
            row = 7 - entry[0] if entry[0] > 3 else entry[0]
            col = 7 - entry[1] if entry[1] > 3 else entry[1]
            niceness = 1 if piecemap[entry] == self.mycolor else -1
            result += self.table[4 * row + col] * niceness
        return result
        
    def count_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))
                
class OpheliaX(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.performance = 1.6 / timeit('for i in range(10): oct(i)')
        print "  --> Determined hardware performance factor:", self.performance
        self.endurance = totalTime / 300.
        self.lastRemainingTime, self.peakTime = totalTime, 0
        self.mycolor = color
        self.table = [ 10, -1,  4,  2, \
                       -1, -1,  2,  1, \
                        4,  2,  2,  1, \
                        2,  1,  1,  1  ]
                        
    def calculate_utility(self, boardstate):
        # The weighted functions below are not normalized in any way, so the
        # weights do not necessarily reflect their relative impact on the
        # utility returned.
        return     self.utility_table(boardstate) \
             + 3 * self.friendly_mobility(boardstate)
             
    def alphabeta_parameters(self, boardstate, remainingTime):

        # Force depth 2 if time is short...
        if self.lastRemainingTime - remainingTime > self.peakTime:
            self.peakTime = self.lastRemainingTime - remainingTime
        self.lastRemainingTime = remainingTime
        if self.peakTime > remainingTime:
            return (2, None, None)
        
        # Use depth 4 in the largest window the resources allow...
        piecemap = boardstate.getPieces()
        if len(piecemap) < 26 / (self.performance * self.endurance) \
        or len(piecemap) > 64 - 8 / (self.performance * self.endurance):
            return (2, None, None)
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
        
class itsybitsy(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.performance = 1.6 / timeit('for i in range(10): oct(i)')
        print "  --> Determined hardware performance factor:", self.performance
        self.endurance, self.mycolor = totalTime / 300., color
        self.table = [ 10, -1, 4, 2,  -1, -1, 2, 1,  4, 2, 2, 1,  2, 1, 1, 1 ]              
    def calculate_utility(self, boardstate):
        return     self.utility_table(boardstate) \
             + 3 * self.friendly_mobility(boardstate)       
    def alphabeta_parameters(self, boardstate, remainingTime):
        disks = len(boardstate.getPieces())
        if disks < 10 + 16 / (self.performance * self.endurance) \
        or disks > 64 -  8 / (self.performance * self.endurance) \
        or remainingTime < 180 / self.performance:
            return (2, None, None)
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

class PoloniusA(othello_player):
    
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.performance = 1.6 / timeit('for i in range(10): oct(i)')
        print "  --> Determined hardware performance factor:", self.performance
        self.endurance, self.mycolor = totalTime / 300., color
        self.table_A = [ 10, -1,  4,  2, \
                         -1, -1,  2,  1, \
                          4,  2,  2,  1, \
                          2,  1,  1,  1  ]
        self.table_B = [ 10,  3,  3,  3, \
                          3,  1,  1,  1, \
                          3,  1,  1,  1, \
                          3,  1,  1,  1  ]
                          
    def calculate_utility(self, boardstate):
        return     self.utility_tables(boardstate) \
             + 2 * self.friendly_mobility(boardstate)       
             
    def alphabeta_parameters(self, boardstate, remainingTime):
        # In the beginning or endgame or if time is short, don't search deep...
        disks = len(boardstate.getPieces())
        if disks < 10 + 16 / (self.performance * self.endurance) \
        or disks > 64 -  8 / (self.performance * self.endurance) \
        or remainingTime < 180 / self.performance:
            return (2, None, None)
        return (4, None, None)
        
    def friendly_mobility(self, boardstate):
        # Simply returns the number of available moves (negative when it's
        # our opponent's turn)...
        if boardstate.getPlayer() == self.mycolor:
            return len(boardstate.legal_moves())
        else:
            return -len(boardstate.legal_moves())
            
    def utility_tables(self, boardstate):
        # For each quadrant of the board we note whether that corner has been
        # taken. If it has, we value pieces in that quadrant according to
        # table_B, which doesn't care about the immediate neighbors of the
        # corner -- if not, we value according to table_A, which doesn't like
        # those dangerous neighbors.
        piecemap, cornerlist = boardstate.getPieces(), []
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
                result += self.table_B[4 * row + col] * niceness
            else:
                result += self.table_A[4 * row + col] * niceness
        return result
        
class PoloniusB(othello_player):
    
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.performance = 1.6 / timeit('for i in range(10): oct(i)')
        print "  --> Determined hardware performance factor:", self.performance
        self.endurance, self.mycolor = totalTime / 300., color
        self.table_A = [ 10, -1,  4,  2, \
                         -1, -1,  2,  1, \
                          4,  2,  2,  1, \
                          2,  1,  1,  1  ]
        self.table_B = [ 10,  3,  3,  3, \
                          3,  1,  1,  1, \
                          3,  1,  1,  1, \
                          3,  1,  1,  1  ]
                          
    def calculate_utility(self, boardstate):
        return     self.count_difference(boardstate) \
             +     self.utility_tables(boardstate) \
             + 2 * self.friendly_mobility(boardstate)       
             
    def alphabeta_parameters(self, boardstate, remainingTime):
        # In the beginning or endgame or if time is short, don't search deep...
        disks = len(boardstate.getPieces())
        if disks < 10 + 16 / (self.performance * self.endurance) \
        or disks > 64 -  8 / (self.performance * self.endurance) \
        or remainingTime < 180 / self.performance:
            return (2, None, None)
        return (4, None, None)
        
    def count_difference(self, boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))
            
    def utility_tables(self, boardstate):
        # For each quadrant of the board we note whether that corner has been
        # taken. If it has, we value pieces in that quadrant according to
        # table_B, which doesn't care about the immediate neighbors of the
        # corner -- if not, we value according to table_A, which doesn't like
        # those dangerous neighbors.
        piecemap, cornerlist = boardstate.getPieces(), []
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
                result += self.table_B[4 * row + col] * niceness
            else:
                result += self.table_A[4 * row + col] * niceness
        return result
        
    def friendly_mobility(self, boardstate):
        # Simply returns the number of available moves (negative when it's
        # our opponent's turn)...
        if boardstate.getPlayer() == self.mycolor:
            return len(boardstate.legal_moves())
        else:
            return -len(boardstate.legal_moves())
            
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
        # In the beginning or endgame or if time is short, don't search deep...
        disks = len(boardstate.getPieces())
        if disks < 10 + 16 / (self.performance * self.endurance) \
        or disks > 64 -  8 / (self.performance * self.endurance) \
        or remainingTime < 180 / self.performance:
            return (2, None, None)
        return (4, None, None)
        
    def friendly_mobility(self, boardstate):
        # Simply returns the number of available moves (negative when it's
        # our opponent's turn)...
        if boardstate.getPlayer() == self.mycolor:
            return len(boardstate.legal_moves())
        else:
            return -len(boardstate.legal_moves())
            
            
class ChadsPlayer(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        from timeit import timeit
        self.performance = 1.6 / timeit('for i in range(10): oct(i)')
        print "  --> Determined hardware performance factor:", self.performance
        self.endurance, self.mycolor = totalTime / 300., color
        self.table = [ 10, -1,  4,  2, \
                       -1, -1,  2,  1, \
                        4,  2,  2,  1, \
                        2,  1,  1,  1  ]              
    def calculate_utility(self, boardstate):
        return     self.utility_table(boardstate) \
             + 3 * self.friendly_mobility(boardstate)       
    def alphabeta_parameters(self, boardstate, remainingTime):
        if len(boardstate.getPieces()) \
            < 26 / (self.performance * self.endurance) \
        or remainingTime < 180 / self.performance:
            return (2, None, None)
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
