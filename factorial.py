#logic of Factorial

# 0! = 1
# 1!= 1*0! =1
# 2!=2*1!=2
# 3!=3*2!=6
# 4!=4*3!=24

def factorial(n):
    if(n<2):  # enter 2 check
        return 1
    else:
        return n* factorial(n-1)  # 2*2-1=> 2*1 => 2


ans=factorial(int(input("Enter the Number => ")))

print("Factorial Of Number =>"  , ans)
