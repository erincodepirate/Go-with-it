from weightothello import *
from othelloplayers import *
from math import exp
import random

# a function to determine the energy that will be used in the simulated
# annealing function
def energy(weights):
    playerList = [FancyTable2, Straight2]

    E = 0
    
    for player in playerList:
        E -= play_othello(Othello(), 86400,
			  player("THANG_B"),
			  WeightPlayer("WP_W"),
			  weights)
	E += play_othello(Othello(), 86400,
			  WeightPlayer("WP_B"),
			  player("THANG_W"),
			  weights)
    return E

# a function that uses a simulated annealing technique to calculate the optimal
# weight values for the othello player
def simulated_annealing(temperature, emax, kmax):
    initial_state = randomstate()
    e_best = e = energy(initial_state)
    s_best = s = initial_state

    k = 0.0
    while k < kmax and e > emax:
        T = temperature(k/kmax)
        s_new = randomstate()
        e_new = energy(s_new)
        delta_energy = e_new - e

        f = open("simulated_annealing.log", 'a')
        f.write(time.strftime("%I:%M %p %A %d %B %Y") \
                + " %d" % k \
                + " " + stateToString(s_new)
		+ " %d" % e_new \
		+ " " + stateToString(s) \
		+ " %d" % e \
                + " " + stateToString(s_best) \
                + " %d" % e_best \
                + "\n")
        f.close()

        if random.random() < exp(-delta_energy/T):
             e = e_new
             s = s_new
        if e < e_best:
            s_best = s_new
            e_best = e_new
        k += 1.0

    return s_best

# temperature schedule for the simulated annealing algorithm
def temperature_unit_linear(t):
    return 1.0 - t

# a function to calculate a random state, to be used in the simulated annealing
# function
def randomstate():
    return (random.random(), random.random(), random.random())

# converts the returned state into a string that can be printed
def stateToString(tup3):
    return "( %f, %f, %f )" % tup3

