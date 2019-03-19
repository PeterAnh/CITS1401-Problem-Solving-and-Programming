from functools import reduce
import os

def factorialREC(n):
    if n == 0:
        return 1
    else:
        return n * factorialREC (n - 1)

def gcdREC(m, n):
    if n == 0:
        return m
    else:
        return gcdREC(n, m % n)

def newtonREC(x, z):
    if abs(x - z ** 2) < 10e-6:
        return z
    else:
        return newtonREC(x, (z + x/z)/2)

def newton(x):
    return newtonREC(x, 1)

def isSortedREC(xs):
    if len(xs) <= 1:
        return True
    else:
        return xs[0] <= xs[1] and isSortedREC(xs[1:])

def binarySearch(x, xs):
    l = 0
    u = len(xs) - 1
    while l <= u:
        k = (u + l) // 2
        if x == xs[k]:
            return True
        elif x < xs[k]:
            u = k-1
        else:
            l = k+1
    return False

def binarySearchREC(x, xs, l, u):
    if l > u:
        return False
    else:
        k = (l + u) // 2
        if x == xs[k]:
            return True
        elif x < xs[k]:
            return binarySearchREC(x, xs, l, k-1)
        else:
            return binarySearchREC(x, xs, k+1, u)

def lengths(ss):
    return list(map(len, ss))

def nonempties(ss):
    return list(filter(lambda s: s != "", ss))

def concat(ss):
    return reduce(lambda xs, ys: xs + ys, ss)

def printAverage(f):
    if os.path.exists(f):
        y = []
        for l in open(f):
            y += l.split()
        print(reduce(lambda x, y: x + y, [float(x) for x in y]) / len(y))
    else:
        print(f + " doesn't exist")

def merge(xs, ys):
    if xs == [] or ys == []:
        return xs + ys
    elif xs[0] < ys[0]:
        return [xs[0]] + merge(xs[1:], ys)
    else:
        return [ys[0]] + merge(xs, ys[1:])

def mergesort(xs):
    if len(xs) <= 1:
        return xs
    else:
        k = len(xs) // 2
        return merge(mergesort(xs[:k]), mergesort(xs[k:]))

def partition(xs, pivot):
    if xs == []:
        return ([], [])
    else:
        (ys, zs) = partition(xs[1:], pivot)
        if xs[0] < pivot:
            return ([xs[0]] + ys ,zs)
        else:
            return (ys, [xs[0]] + zs)

def quicksort(xs):
    if len(xs) <= 1:
        return xs
    else:
        (ys, zs) = partition(xs[1:], xs[0])
        return quicksort(ys) + [xs[0]] + quicksort(zs)
