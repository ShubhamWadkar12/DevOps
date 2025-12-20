for i in range(5):
    print("Iteration number:", i)  #Printing the iteration number
    


for i in range(5):
    env = input("Enter the environment: ")             #Taking input from user
    print("The current environment is:", env)          #Printing the environment

    if env == "prd":                                    #True or False
        print("Don't deploy on friday")
    elif env =="stg":                                   #False      
        print("Take a backup")
    else:                                               #False
        print("Deploy it is safe")


count = 1

while count <= 3:
    print("Hello")
    count = count + 1