import os

data = 'myprogram.exe'

print(data[5:9])
print(data[:-4])
print(data[len(data) // 2])

"""
lab4_2: 
Decode the msg with each of the 25 possible shifts: 
for one of them, the decoded msg should look like English 
"""

def octalToDecimal(n):
    print(n, end = " ")
    p = 1
    z = 0
    while n > 0:
        z += n % 10 * p
        p *= 8
        n //= 10
    print(z)


def decimalToOctal(n):
    print(n, end = " ")
    p = 1
    z = 0
    while n > 0: 
        z += n % 8 * p
        p *= 10
        n //= 8
    print(z)

data = 'Python rules!'

print(data.split())
print(data.upper())
print(data.find('rules'))
print(data.replace('!', '?'))

def lab4_5():
    f = input("Input file name: ")
    z = 0
    for l in open(f):
        for w in l.split():
            if len(w) == 4:
                z += 1
                print(w)
    print(f, "contains", z, "four-letter words")

def lab4_6(s, k, b):
    k %= len(s)
    if not b:
        k *= -1 
    print(s[k:] + s[:k])

def lab4_7(s):
    print(s.replace('ten', 'ten (10)').replace('Ten', 'Ten (10)'))

def lab4_8():
    for f in os.listdir("."):
        print(f)

def lab4_9():
    f1 = input("Source file? ")
    if not os.path.exists(f1):
        print(f1, "does not exist")
    else:
        f2 = input("Target file? ")
        if os.path.exists(f2):
            print(f2, "already exists")
        else:
            f2o = open(f2, 'w')
            for l in open(f1):
                f2o.write(l)

# enumeration and search
def birthdays_exact(n):
    days = 365
    z = 1
    for k in range(1, n):
        z *= (days - k) / days
    return 1 - z

def birthdays_simulated(n):
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

def fetch(k):
    if k.isdigit():
        return ord(k) - ord('0')
    else:
        return ord(k) - ord('A') + 10

def repToDecimal(s, b):
    z = 0
    for k in s:
        z = b * z + fetch(s[0])
        s = s[1:]
    return z


""" Basic list operations
Q1. String is a special type of list on which you can perform string operations
such as find and replace. Such operations can not be performed on a sequence of
characters which is basically a list. On the other hand, on a sequence of
characters, it is possible to perform list operations such as assign values
to any location in the sequence. This operation can not be performed on a String."""

def lab4_fib(n):
    fib = [1,1]
    for i in range(2,n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

