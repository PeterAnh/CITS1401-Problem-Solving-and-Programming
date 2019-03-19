def lab5_1():
    print("(a) Looks like {1} and {0} for breakfast".format("eggs", "spam"))
    print("(b) There is {0} {1} {2} {3}".format(1,"spam", 4, "you"))
    print("(c) Hello {0}".format("Susan", "Computewell"))
    print("(d) {0:0.2f} {0:0.2f}".format(2.3, 2.3468))
    print("(e) IndexError. Index 7 is out of range. There are only 0 and 1 indices")
    print("(f) Time left {0:02}:{1:05.2f}".format(1, 37.374))
    print("(g) IndexError. Only index 0 is valid.")

def lab5_2(N):
    primes = [3]
    for i in range(5,N,2):
        for j in primes:
            if i%j == 0:
                break
        else:
            primes.append(i)
    primes = [2] + primes
    return primes

def lab5_3(N):
    primes = [2,3]
    t = primes[-1]
    while len(primes)<N:
        t += 2
        for i in primes:
            if t%i == 0:
                break
        else:
            primes.append(t)
    return primes

#Question 4
import math
def intersect(r1, x1, y1, r2, x2, y2):
    distance =  math.sqrt( math.pow((x1-x2),2) + math.pow((y1-y2),2))
    radiusDistance = abs(r1 + r2)
    if distance > radiusDistance:
        return False
    else:
        return True
    
def lab5_4():
    rad1,x1, y1, rad2, x2, y2 = eval(input('Enter the radius and centers of circles in this form radius1,x1, y1, radius2, x2, y2: '))
    result = intersect(rad1, x1, y1, rad2, x2, y2)
    return result

def lab5_5(inList):
    for i in range(0,len(inList)-1,2):
        inList[i], inList[i+1] = inList[i+1], inList[i]
     # no need to return check your input parameter inList, it will have changed

def lab5_6(fileName, e, n):
    inFile = open(fileName, 'r')
    plainTxt = inFile.read()
    #print(plainTxt)
    inFile.close()
    cypherTxt = ''
    for letter in plainTxt:
        m = ord(letter)
        c = pow(m,e)%n
        cypherTxt += ' ' + str(c) # NOTE that we need spacing between the numbers
    fileName2 = fileName[:-4] + "Encrypt" + fileName[-4:]
    #print(cypherTxt)
    outFile = open(fileName2, 'w')
    print(cypherTxt, file=outFile)
    outFile.close()

def lab5_7(fileName, d, n):
    inFile = open(fileName, 'r')
    cTxt = inFile.read()
    inFile.close()
    pTxt = ''
    for word in cTxt.split(): # every word is an integer written as string = one character
        c = int(word)
        m = pow(c,d)%n
        pTxt += chr(m)
    print(pTxt)

def birthdays_simulated(n):
    import random
    days = 365
    runs = 10000
    hits = 0
    for k in range(runs):
        dates = []
        j = 0
        while j < n:
            j += 1
            date = random.randint(1, days)
            if date in dates:
                hits += 1
                j = n #this terminates the while loop
            else:
                dates += [date]
    return hits / runs

# last problem solving question
def getValue(x):
    if ord(x) < 58:
        return int(x)
    else:
        return ord(x)-55
    

        
def decConverter(st, base):
    decVal = 0
    n = len(st)-1
    for i in st:
        decVal = decVal + getValue(i) * pow(base,n)
        n -= 1
    print("Decimal value is ", decVal)
