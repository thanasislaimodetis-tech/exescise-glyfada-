print("This program calculates the largest number from a series of numbers entered.")
numbers = []
user_input = int(input("Please enter a number. Enter 0 to stop\n"))
if user_input != 0:
    while True:
        user_input = int(input("Please enter a number. Enter 0 to stop\n"))
        numbers.append(user_input)
        if user_input == 0:
            break
    
    numbers.sort()
    print("The largest of the numbers entered is "+ str(numbers[-1]))
else:
    print("No numbers entered.")    

