#task 1

x=int(input("Enter the Number "))
if(x%2==0):
    print( x ,"is an Even Number")
else:
    print(x , "is an odd Number")

    #Task 2
x=0
for i in  range(1 , 51):
    x +=i
print(' The Sum of number from 1 to 50 => ' , x)