from weightothello import *
from othelloplayers import *
from random import *

def energy(weights):
    playerList = [OpheliaA]

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

def simulated_annealing(temperature, emax, kmax):
    f = open("simulated_annealing.log", 'w+')

    f.write(time.strftime("%I:%M %p %A %d %B %Y") \
            + "Initializing simulated annealing...\n")

    initial_state = randomstate()
    e_best = e = energy(initial_state)
    s_best = initial_state

    f.write(time.strftime("%I:%M %p %A %d %B %Y") \
            + " init state: " + initial_state \
            + " e_best: " + e_best \
            + " s_best: " + s_best \
            + "\n")

    k = 0.0
    while k < kmax and e > emax:
        T = temperature(k/kmax)
        s_new = randomstate()
        e_new = energy(s_new)
        delta_energy = e_new - e
        if random.random() < exp(-delta_energy/T):
             e = e_new
             s = s_new
        if e < e_best:
            s_best = s_new
            e_best = e_new
        k += 1.0

        f.write(time.strftime("%I:%M %p %A %d %B %Y") \
                + " k: " + k
                + " state: " + s
                + " s_best: " + s_best
                + " energy: " + e
                + " e_best: " + e_best
                + "\n")

    return s_best
        
def temperature_unit_linear(t):
        return 1.0 - t
    
def randomstate:
    return (random.random(), random.random(), random.random())

 
