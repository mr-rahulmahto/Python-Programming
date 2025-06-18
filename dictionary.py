#list ===> [] , Index Value
#list = [1 ,2 ,3 ,4 , 5 , 6]
#tuple ===> ()

#Dictionary ===> {} , Key
#dictionary = {key: value , key: value , Key : value ,  ...........}

# example Dictionary
my_dict = {'key1' : 3 , 'key2' : '34' , 'key3' : [4, 5, 6] , 'key4': (5674)}
print(my_dict)
print(my_dict['key3'])

#Example 2
dictionary= {1:"a" , 2: 'Rahul' , 3:[4,8, 9] , 4:(7849) }
print(dictionary)
print(dictionary[2])

#Example 3
dict={'a':"apple" , 'b': 'Ball' , 'c':"Cat" , 'd':'Dog'}
# ADD NEW KEY IN DICTIONARY
dict['e'] ="Elephant"
#print(dict)
# DELETE KEY IN DICTIONARY
del(dict['b'])
print(dict)

print('b' in dict) # Find the key in dictionary
print('c' in dict)
print(dict.keys()) # Find all the key
print(dict.values()) # Find all the value
print(dict.get('g' , "'g' Not Found")) # Find  the key