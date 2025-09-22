with open("11111.txt","w") as file:
    file.write("Name Harshit Gurjar\n")
    file.write("AccountNumber 11111\n")
    file.write("Pin 1111\n")
    file.write("BranchCode BOB1111\n")
    file.write("Balance 132.45\n")

with open("22222.txt","w") as file:
    file.write("Name Ravi Kumar\n")
    file.write("AccountNumber 22222\n")
    file.write("Pin 2222\n")
    file.write("BranchCode BOB2222\n")
    file.write("Balance 22225\n")

with open("33333.txt","w") as file:
    file.write("Name Tushar Kumar\n")
    file.write("AccountNumber 33333\n")
    file.write("Pin 3333\n")
    file.write("BranchCode BOB3333\n")
    file.write("Balance 333333\n")

with open("44444.txt","w") as file:
    file.write("Name Shivam Rajawat\n")
    file.write("AccountNumber 44444\n")
    file.write("Pin 4444\n")
    file.write("BranchCode BOB4444\n")
    file.write("Balance 14563\n")


import ast

# Read the data from the file

with open('data.txt', 'r') as file:
    data = file.read()

# Convert the string to a dictionary
dictionary = ast.literal_eval(data)

print(dictionary)
print(dictionary["Harshit Gurjar"]) 
