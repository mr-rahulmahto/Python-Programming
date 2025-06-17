#task 1
def factorial(n):
    if (n < 2):  # enter 2 check
        return 1
    else:
        return n * factorial(n - 1)  # 2*2-1=> 2*1 => 2


ans = factorial(int(input("Enter the Number => ")))

print("Factorial Of Number =>", ans)


#Task 2

import math
from  math import *
x=float(input('Enter the number => '))
result=sqrt(x)
ans=log(x )
answer=sin(x)

print('square root of the number => '  , result)
print('Logarithm of the number => '  , ans)
print('Sin of the number => '  , answer)