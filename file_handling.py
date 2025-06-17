#File Handling



#2 way
'''
with open('Document.txt' ,'r') as file2:
    reading_file=file2.read()
    print(reading_file)
'''

# Write Mode
file2=open('Document.txt' ,'w')
writing_file=file2.write("Thanks You")
print(writing_file)
file2.close()

# Append Mode
file2=open('Document.txt' ,'a')
append_file=file2.write(" ! Hii , Welcome to Python World")
print(append_file)
file2.close()

# Read Mode

file2=open('Document.txt' ,'r')
#directory = specify the location
#mode= r read , w write , r+
reading_file=file2.read()
#read=file2.readline()
#print(read)
print(reading_file)
file2.close()

#r+ ==>  Write and read both
file2=open('Document.txt' ,'r+')
readwrite_file=file2.write(" I'm Happy")
print(readwrite_file)
file2.close()

file2=open('Document.txt' ,'r+')
read_file=file2.read()
print(read_file)
file2.close()