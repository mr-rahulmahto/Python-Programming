#Task 1
'''
try:
    # Open the file in read mode
    with open("sample.txt", "r") as file:
        # Read and print content line by line
        for line in file:
            print(line.strip())  # strip() removes unnecessary spaces and newline characters

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception:
    print("An error occurred:")
  '''
 #Task 2

 #Write Mode
file2 = open('output.txt', 'w')
writing_file = file2.write("Hello , Python !")
print(writing_file )
file2.close()

#Append Mode
file2=open('output.txt' ,'a')
append_file=file2.write(" \nThanks You ")
print(append_file )
file2.close()

# Read Mode
with open("output.txt", "r") as file2:
    print("Final Content of Output.txt: ")
    print(file2.read())