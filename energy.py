from weightothello import *
from othelloplayers import *
from random import *

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

def simulatedannealing(temperature, energy, emax, kmax):
    initial_state = randomstate()
    e = energy
    e_best = e
    s_best = initial_state
    k = 0
    while k < kmax and e > emax:
        t = temperature(k/kmax)
        s_new = randomstate()
        e_new = energy(s_new)
        delta_energy = e_new - e
        if random.random() < exp(-delta_energy/t):
             e = e_new
             s = s_new
        if e < e_best:
            s_best = s_new
            e_best = e_new
        k += 1
    return s_best
        
        
        
        
    
def randomstate:
    return (random.random(), random.random(), random.random())

 
