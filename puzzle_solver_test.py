# s1 = {(3,3),[[0,1,0],[0,1,0],[1,1,1]]}

'''
table size 6x8


**blocks**
b0 : 1x1
o

b1 : 3x3
xox
xox
ooo

b2 : 3x3
xox
ooo
xox

b3 : 3x3
oxx
oox
xoo

b4 : 3x2
oo
ox
ox

b5 : 2x4
ooxx
xooo

b6 : 2x4
oooo
xoxx

b7 : 2x3
xxo
ooo

b8 : 3x3
xox
ooo
xxo

b9 :5x1
o
o
o
o
o

b10 : 3x2
oo
xo
xo


'''

size = (3,3)
for i in range(6):
    if i + size[0] > 6:
        continue
    for j in range(8):
        if j+size[1] > 8:
            continue
        print(i,j)
