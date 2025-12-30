user_input = int(input("Please enter the size (no of rows) of the triangle you wish to display:\n"))

for i in range(1,user_input+1):
    for j in range(1,i+1):
        print("*",end="")
    print("")    