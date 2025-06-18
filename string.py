from tkinter.scrolledtext import example

a="RahuL"
print(a.capitalize())

print(a.upper())

print(a.lower())

b='7'
#print(b.isnumeric()) # Check number or Not

#print(b.isalpha())  # Check alphabet or Not

c= 'python is slow language'
print(c.startswith('Hello'))
print(c.endswith('language'))
print(c.replace('python' , 'Go'))

print(c.find('is')) # index value
print(c.lstrip()) #remove space
print(c.rstrip())  #remove space

print(c.splitlines())

d='Rahul' , 'Mahto'
print(d)
e=','
print(e.join(d))

#Concept

#Example 1
name='Rahul'
number=len(name)*4  #length Calculate in name word 5*4--->20
print("Hello ! {} , Your Lucky Number is {} ." .format(name , number))

# example 2
example=  "format () Method"
string="This is an example of {} on a string." .format(example)
print(string)

#Example 3
first = "Monkey"
second = "eat"
third ="Banana"
str = ' {}  {}  {} ' .format(first  , second  , third)
print(str)
str = ' {0}  {2}  {1} ' .format(first  , second  , third)
print(str)

# Example 4
price =150
with_tax= 150+60
print(price ,with_tax)  #2f mean Contain 2 digit float or decimal number
print("Price: Rs{:.2f} . with tax: Rs{:.3f} " .format(price , with_tax))