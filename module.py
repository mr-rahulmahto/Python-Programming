#using module or import libraries
'''
#1 Step
import  math
print(math.pi)

#step 2
from  math import  pi
print(pi)

#step 3
from  math import *  # * using all libraries  in math
print(pi)
'''
import math
from  math import *
x=float(input('Enter the number => '))
result=sqrt(x)
ans=log(x )
answer=sin(x)

print('square root of the number => '  , result)
print('Logarithm of the number => '  , ans)
print('Sin of the number => '  , answer)