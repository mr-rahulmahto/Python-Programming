#Recursion => Recursion are use same line of code again and again itself.....

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(30000)

n=0
def Fun1():
    global n
    n=n+1
    print("Hello , Rahul" , n)
    Fun1()
Fun1()