import math 

# Welcoming User
print("------------------------------")
print("WELCOME TO SIMPLE CALCULATOR")
print("------------------------------")

# Taking User Input 
while True : 
    num_1 = int(input("Enter a Number : "))
    num_2 = int(input("Enter a Number: "))

# Taking Task to perform 
    operation = input("Enter Operation + , - , * , / , Exit: ")

#Applying condition 
    if operation == "+" :
        print(num_1 + num_2)
    elif operation == "-" :
        print(num_1 - num_2)
    elif operation == "*" :
        print(num_1 * num_2)
    elif operation == "/" :
        print(num_1 / num_2)
    elif operation == " " : 
        print("Invalid Input")

#Adding Exit 
    if operation == "Exit" :
        break

print("------------------------------")
print("THANKS FOR USING CALCULATOR , VISIT AGAIN")
print("------------------------------")