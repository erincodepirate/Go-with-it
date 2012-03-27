# Some simple unit tests for go.py

from go import *

# Run all tests. Be sure to add new tests to this...
def test_all():
    test_1()
    test_2()
    print "All tests passed!"
    
# Check whether BoardState defaults are correctly initialized
def test_1():
    print "\t1. BoardState Initialization Test...",
    s = BoardState()
    s.stat_gen()
    
    assert s.size == 19
    assert s.to_move == Black
    assert len(s.legal_move_list) == 19**2
    assert s.white_stone_list == []
    assert s.black_stone_list == []
    
    print "PASSED."
    
def test_2():
    pass