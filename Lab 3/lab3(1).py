from graphics import *
import math
import time

def lab3_1():
    r = eval(input("Enter the radius of sphere in meters : "))
    cost = eval(input("Enter the material cost per square meter : "))
    Area = 4*math.pi*pow(r,2)
    totalPrice = Area*cost
    print("The total price of material is %.2f dollars." %totalPrice)

#lab3_1()

def lab3_2():
    r = eval(input("Enter the circle radius : "))
    win = GraphWin("Circle",300,300)
    pt1 = Point(150,150)
    circ = Circle(pt1, r)
    circ.draw(win)
    pt2 = Point(100,250)
    
#lab3_2()

def lab3_3():
    r = eval(input("Enter the circle radius : "))
    win = GraphWin("Circle",300,300)
    pt1 = Point(150,150)
    circ = Circle(pt1, r)
    circ.draw(win)
    pt2 = Point(100,250)
    area = math.pi*pow(r,2)
    text1 = "Area is %.2f" %area # only two decimal spaces are sufficient
    Text(pt2, text1).draw(win)
    pt2 = Point(100, 280)
    circum = 2*math.pi*r
    text1 = "Circumference is %.2f" %circum
    Text(pt2, text1).draw(win)

#lab3_3()

def lab3_4():
    win = GraphWin("Moving Rectangle", 600,200)
    rect = Rectangle(Point(20,20), Point(50,50))
    rect.draw(win)
    for i in range(300):
        rect.move(1,0)
        time.sleep(0.05)

#lab3_4()

""" lab3_5 : give a bigger value in rect.move(dx,dy) or reduce the time.sleep"""

def lab3_6():
    winSize = 600
    win = GraphWin("Moving Circle", winSize, winSize)
    pt1 = Point(winSize/2,winSize/2)
    r1 = 2 # radius of the smallest circle to draw
    for i in range(20):
        r1 = r1*2
        circ = Circle(pt1, r1)
        circ.draw(win)

lab3_6()

def lab3_7(init, rate, hours, time):
    print(init * rate ** (time / hours))

#lab3_7()

def lab3_8(x):
    invest = 38000 # put any value here
    y = invest
    for i in range(200):
        y = y*(1+x)
        if y >= 2*invest:
            break
    else:
        print("This will need a very long time")
        return
    print(i, " years will double your investment")

#lab3_8(0.10)

def lab3_9(x, y):
    print("you entered ", x, " and ", y) 
    while y > 0:
        x, y = y, x % y
        print("new x = ", x, " and y = ", y)
    print("gcd =", x)

#lab3_9(124,240)


def lab3_10(b):
    #b = input("Enter a binary number: ")
    dec = 0
    n = len(b)-1
    for i in b:        
        if int(i):
            dec = dec + pow(2,n)
        n -= 1
    print("Decimal value is ", dec)
    
lab3_10('0000100')

def lab3_ex1a(n):
    for i in range(n,0,-1):
        for j in range(i):
            print('#', end='')
        print('')
#lab3_ex1a(5)
        
def lab3_ex1b(n):
    for i in range(1,n):
        for j in range(i):
            print('#', end='')
        print()
    lab3_ex1a(n)
        
#lab3_ex1b(5)

def lab3_ex2a():
    q = input("Did you use extra nitrogen-based fertiliser? (y/n) ") 
    q = q + input("Did you use extra phosphate-based fertiliser? (y/n) ")
    q = q + input("Did you allow early flooding of the field? (y/n) ")
    q = q + input("Was the field left fallow (empty) the previous season? (y/n) ")
    q = q + input("Did you harvest early? (y/n) ")
    q = q + input("Did you drain the field before harvest? (y/n) ")
    q = q + input("Were the grains dried in the sun before delivery? (y/n) ")
    q = q + input("Did you use the more expensive new variety? (y/n) ")
    # now see the similarity of the rest with lab3_10
    dec = 0
    n = len(q) - 1
    for i in q:
        if i == 'y':
            dec = dec + pow(2,n)
        n -= 1
    print("The treatment number is ", dec, "\n")

#lab3_ex2a()
    
def lab3_ex2b(treatNumber): 
    b =''
    while treatNumber > 0:
        if treatNumber%2 == 1:
            b = '1' + b
        else:
            b = '0' + b
        treatNumber = treatNumber//2
    print("Your answers to the 8 questions were ", end ='')
    for i in range(8-len(b)):
        print("n, ", end='')
    for i in b:
        if int(i):
            print("y, ", end="")
        else:
            print("n, ", end='')

#lab3_ex2b(132)           
    

