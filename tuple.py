#tuple ---> immutable (No changes)
tup1=(1,2,3,5,7)
#tup1[1]=4
#print(tup1) #show ERROR massage

tup2=(4,66,87,99 , 56 ,78,236,126)
tup_sort=sorted(tup2)
print(tup_sort)

print(tup1+tup2)

print(len(tup1+tup2))

print(tup2.index(236))




#List ---->  Mutable( here changes)
lis=[1,2,3,5,6]
lis[3]=4
print(lis)
