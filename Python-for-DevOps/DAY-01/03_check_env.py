# Get the Environment from User and print it

env = input("Enter the environment: ")             #Taking input from user
print("The current environment is:", env)          #Printing the environment

#conditional statements

if env == "prd":                                    #True or False
    print("Don't deploy on friday")
elif env =="stg":                                   #False      
    print("Take a backup")
else:                                               #False
    print("Deploy it is safe")
    
print("--------------------------------------------------")

#conditional statements based on trek input
trek = input("Enter the trek you want to go:")
if trek == "Kedarnath":
    print("Prepare for high altitude trek")
elif trek == "Valley of flowers":
    print("Prepare for beautiful flowers")
else:
    print("Enjoy your trek!")

print("--------------------------------------------------")

#type casting : conversion of one data type to another
#calculator

a = int(input("Enter first number"))
b = int(input("Enter second number"))
print("The sum of a and b is:", a + b)
print("The product of a and b is:", a * b)
print("The difference of a and b is:", a - b)
print("The division of a and b is:", a / b)

print("--------------------------------------------------")

#predicting age after 5 years
age = int(input("Enter your age: "))
print("Your age is: ",age)
print("Your age after 5 years will be ", int(5) + age)
    
print("--------------------------------------------------")

# ==, !=, >, <, >=, <= (Comparison Operators)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Is num1 equal to num2?", num1 == num2)
print("Is num1 not equal to num2?", num1 != num2)
print("Is num1 greater than num2?", num1 > num2)
print("Is num1 less than num2?", num1 < num2)
print("Is num1 greater than or equal to num2?", num1 >= num2)
print("Is num1 less than or equal to num2?", num1 <= num2)


