#type of collection
#unordered
#unique elements
#{}

Set1={1, 2, 3, 5, 4,7 ,2}  # Set not repeat same element
#print(Set1)

Set1.add(9)
#print(Set1)

Set1.remove(2)
#print(Set1)
print(2 in Set1) # finding element


set2={1 ,3 ,4}
print(Set1 & set2) #intersection

print(Set1.union(set2)) #union

print(set2.issubset(Set1))  #subset


