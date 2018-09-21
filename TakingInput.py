import os

#We use the input function to take an input
#We have to have an assignment statement to store an input

fName = input ("What is your name: ")
lName = input ("What is your last name: ")

print("Hi, "+fName+" "+lName)

initialName = fName[0] + "." + lName #adding strings in concatination
print("Hi, "+initialName)

os.system("say "+fName+" "+lName)
