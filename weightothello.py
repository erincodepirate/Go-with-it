# Weighted othello player, uses weights on board placement table,
# difference and mobility to determine the best combination that
# for beating the players we assign to play against it

from othello import *

class WeightPlayer(othello_player):
    def initialize(self, boardstate, totalTime, color, weights):
        print "Initializing", self.name + '...'
        self.mycolor = color
        self.table = [ 10, -1,  4,  2, \
                       -1, -1,  2,  1, \
                        4,  2,  2,  1, \
                        2,  1,  1,  1  ]
        self.weights = weights
    def calculate_utility(self, boardstate):
        return self.weights[0] * self.mycount_difference(boardstate) + \
			self.weights[1] * self.utility_table(boardstate) + \
			self.weights[2] * self.friendly_mobility(boardstate)       
    def alphabeta_parameters(self, boardstate, remainingTime):
        return (2, None, None)
    def friendly_mobility(self, boardstate):
        if boardstate.getPlayer() == self.mycolor:
            return len(boardstate.legal_moves())/10.0
        else:
            return -len(boardstate.legal_moves())/10.0
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))/64.0
    def utility_table(self, boardstate):
        # Get the piecemap, fold it into quarters, add symmetrically
        # corresponding entries, and multiply that by the utility table above,
        # entry-by-entry. Add up the resulting numbers -- positively for
        # friendly pieces and negatively for the opponent. Return the result.
        piecemap, result = boardstate.getPieces(), 0
        for entry in piecemap:
            row = 7 - entry[0] if entry[0] > 3 else entry[0]
            col = 7 - entry[1] if entry[1] > 3 else entry[1]
            niceness = 1 if piecemap[entry] == self.mycolor else -1
            result += self.table[4 * row + col] * niceness
        return result/132.0
