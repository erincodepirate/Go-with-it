#!/bin/env python

# Some simple unit tests for go.py

from go import *

# Run all tests. Be sure to add new tests to this...
def test_all():
    test_1()
    test_2()
    print "All tests passed!"
    
# Check whether BoardState defaults are correctly initialized
def test_1():
    print "\t1. BoardState Initialization Tests...",
    
    s = BoardState()
    s.stat_gen()
    
    assert s.size == 19
    assert s.to_move == Black
    assert len(s.legal_move_list) == 19**2
    assert s.white_stone_list == []
    assert s.black_stone_list == []
    
    print "PASSED."

# Check whether Go's cycle-finding functions are working properly (incomplete)
def test_2():
    print "\t2. Go Cycle-finding Tests (incomplete)...",
    
    g = Go()
    s = BoardState()
    s.stat_gen()
    
    assert g.neighbors(s, (5,5)) == \
           ((4,4),(4,5),(4,6),(5,6),(6,6),(6,5),(6,4),(5,4))
           
    assert g.neighbors(s, (0,0)) == ((0,1),(1,1),(1,0))
    
    assert g.neighbors(s, (7,20)) == ((6,19),(6,20),(8,20),(8,19),(7,19))
    
    print "PASSED."
    

# Run the tests...
test_all()
