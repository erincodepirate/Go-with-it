# cwothello.py
#
#     A decent Othello player with some limited adaptability to adapt to
# various hardware speeds. Evaluates board states based on mobility and
# a simple table associating a value with each square. I tried a few more
# complicated evaluation functions, but these simple ones consistently beat
# them (it appears having fancy evaluation functions isn't very helpful if
# they take too long to allow deep searches -- not to mention that they're
# exceedingly difficult to debug).
#
#  Chad Williamson
#  23 March 2012

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
            return len(boardstate.legal_moves())
        else:
            return -len(boardstate.legal_moves())
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))
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
        return result
# CS 480
# Programming Assignment 2
# Othello Player
#
# Erin Clark
# Andrea Dunn

class AEPlayer(othello_player):
    #  This will be called once at the beginning of the game, after
    #  a few random moves have been made.  Boardstate is the initial
    #  boardstate for the game, totalTime is the total amount of time
    #  (in seconds) in the range 60-1800 that your player will get for
    #  the game.  For our tournament, I will generally set this to 300.
    #  color is one of Black or White (which are just constants defined
    #  in the othello.py file) saying what color the player will be
    #  playing.
    def initialize(self, boardstate, totalTime, color):
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
	if remainingTime > 100:
	       	return (4, None, None)
	# check depth 2 if you are running out of time
	else:
		return (2, None, None)
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))

def count_difference(boardstate):
    return (boardstate._board.count(boardstate.to_move)
            - boardstate._board.count(opponent(boardstate.to_move)))


class MyPlayer(othello_player):
    #  This will be called once at the beginning of the game, after
    #  a few random moves have been made.  Boardstate is the initial
    #  boardstate for the game, totalTime is the total amount of time
    #  (in seconds) in the range 60-1800 that your player will get for
    #  the game.  For our tournament, I will generally set this to 300.
    #  color is one of Black or White (which are just constants defined
    #  in the othello.py file) saying what color the player will be
    #  playing.
    def initialize(self, boardstate, totalTime, color):
        print "Initializing", self.name
        self.mycolor = color
	if color == 1:
		self.opcolor = 2
	else:
		self.opcolor = 1
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
        return (2, None, None)
    def mycount_difference(self,boardstate):
        return (boardstate._board.count(self.mycolor) -
                boardstate._board.count(opponent(self.mycolor)))
