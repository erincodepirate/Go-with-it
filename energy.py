from weightothello import *
from othelloplayers import *

def energy(weights):
    playerList = [OpheliaA]

    E = 0
    
    for player in playerList:
        E += play_othello(Othello(), 86400,
			  player("THANG_B"),
			  WeightPlayer("WP_W"),
			  weights)
	E -= play_othello(Othello(), 86400,
			  WeightPlayer("WP_B"),
			  player("THANG_W"),
			  weights)
    return E
