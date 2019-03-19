def square(x):
        #returns the square of x
        return x * x

def fibs(x):
        #prints the first x Fibonacci numbers
        #each number is the sum of the previous two
        a,b = 0,1
        for i in range(x):
                print("fib(", i, ") = ", a)
                a,b = b,a+b

def lab1_1():
    print('CITS1401 Problem Solving and Prgoramming')

def lab1_2():
    print('8      = 8')
    print('8 *  2 = 16')
    print('8 ** 2 = 64')
    print('8 /  6 = 1.33')
    print('8 // 6 = 1')
    print('8 %  6 = 2')
    print('8 /  0 gives an error')

def lookandsay(x):
        #prints the first x numbers of a well-known sequence
        s = [1]
        for k in range(x):
                for j in s:
                        print(j, end="")
                print()
                t = []
                i = 0
                while i < len(s):
                        z = i
                        i += 1
                        while i < len(s) and s[i] == s[i-1]:
                                i += 1
                        t.extend([i - z, s[i-1]])
                s = t

"""
lookandsay(12) gives the following. 

1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211
11131221133112132113212221
3113112221232112111312211312113211

3-1. Each number is generated by reading aloud the digits from the
     previous number, grouping similar contiguous digits.

     1      is one 1,                             i.e. 11
     11     is two 1s,                            i.e. 21
     21     is one 2, then one 1,                 i.e. 1211
     1211   is one 1, then one 2, then two 1s,    i.e. 111221
     111221 is three 1s, then two 2s, then one 1, i.e. 312211
     etc. 

3-2. One example is 333, which gives the result 33. There are many others. 

3-3. Because the last digit in the first number is a 1.

     Thus the last two digits in every subsequent number will describe how many
     trailing 1s there are, i.e. they will always be n1 for some value of n.

3-4. The only (non-empty) initial value that loops is 22. Try it! 

3-5. Imagine the kth number contained the pair 41, representing "four 1s".
     This means the (k-1)th number contained 1111.
     This means the (k-2)th number contained "one 1, then one 1", i.e. 11,
     but of course that would be read as "two 1s", giving 21 (instead of 1111)
     in the (k-1)th number.
     So 41 is impossible!

     Basically the grouping means that a 4 (or a bigger digit) can never arise. 
"""