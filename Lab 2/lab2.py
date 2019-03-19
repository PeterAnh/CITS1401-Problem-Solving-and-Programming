from tri import tri
from math import pow

"""
1. Because for any remotely-interesting problem, trying to understand, 
   analyse, and solve the problem while simultaneously coding up the 
   solution will be far less efficient than separating those tasks. 

   See the text for a longer, more-complete answer. 
"""

def lab2_2a():
    return "'"

def lab2_2b():
    return '"'

def lab2_3a():
    return 3.5576e2

def lab2_3b():
    return 0.7832e-2

def lab2_3c():
    return 4.3212e0

def lab2_4(n ,s): # e.g. lab3_4(27, ' dresses')
    return str(n) + s

def lab2_5():
    print('8^2 =', pow(8, 2))
    print("5^4 =", pow(5, 4))

def lab2_6(n):
    print(-n)

def lab2_7():
    print(len("y\nb\x1f\000d"))

def testtri():
    print("all equal: equilateral")
    tri(3,3,3)

    print()
    print("two equal, other smaller: isosceles")
    tri(1,2,2)
    tri(2,1,2)
    tri(2,2,1)

    print()
    print("two equal, other bigger: isosceles")
    tri(3,2,2)
    tri(2,3,2)
    tri(2,2,3)

    print()
    print("two equal, other too big: no triangle")
    tri(6,2,2)
    tri(2,6,2)
    tri(2,2,6)

    print()
    print("all different: scalene")
    tri(6,5,2)
    tri(6,2,5)
    tri(5,6,2)
    tri(5,2,6)
    tri(2,6,5)
    tri(2,5,6)

    print()
    print("all different, straight line: no triangle")
    tri(6,4,2)
    tri(6,2,4)
    tri(4,6,2)
    tri(4,2,6)
    tri(2,6,4)
    tri(2,4,6)

    print()
    print("all different, one too big: no triangle")
    tri(6,3,2)
    tri(6,2,3)
    tri(3,6,2)
    tri(3,2,6)
    tri(2,6,3)
    tri(2,3,6)
