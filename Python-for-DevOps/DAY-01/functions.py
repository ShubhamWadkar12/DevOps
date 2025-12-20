
def sum_of_nums():                                                  #definition of function (Kaam Karycha sthaan)
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is:", sum)
    
    
    env = input("Enter the environment: ")             #Taking input from user
    print("The current environment is:", env)          #Printing the environment

    if env == "prd":                                   
        print("Don't deploy on friday")
sum_of_nums()                                                       #function call (Kaam Karycha aadesh)

def take_backup():
    print("Backup script :")
    day = input("Enter the day: ")
    if day == "sunday":
        print("Full backup")