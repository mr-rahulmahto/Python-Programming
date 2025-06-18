#task 1

student={'Rahul' : 85 , 'Aditi' : 88 , 'Sonu':79 , 'Diya':72 , 'Sahil':73 , 'Sakshi' : 80 , 'Happy' : 70}
name=input("Enter the Student Name : ")
if name in student:
    print(f"{name} scored {student[name]} marks.\n")
else:
    print("student Not Found")


    #task 2
list1=[1,2,3,4,5,6,7,8,9,10]
print('\nOriginal list ' , list1)


print("\nExtract first Five Element"  ,  list1[:5])

reversed = list(reversed( list1[:5]))
print("\nReversed  Extract List:", reversed)

