from go import *

s = BoardState()
s.change(9,9,Black)
s.change(9,10,Black)
#s.change(9,11,Black)
s.change(8,11,Black)
s.change(7,11,Black)
s.change(6,11,Black)
s.change(5,10,Black)
s.change(8,9,Black)
s.change(5,9,Black)
s.change(5,8,Black)
s.change(6,8,Black)
s.change(7,8,Black)
s.change(8,8,Black)


s.stat_gen()

s.display_matrix()
for c in s.cycles((9,9)):
    print c, s.enclosed_nodes(c)
