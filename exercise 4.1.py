count = 0
sum_of_numbers = 0.0
print("This program calculates the average of a series of numbers entered.")
while True:
    user_input = float(input("Please enter a number.Enter 0 to stop:\n"))
    if user_input == 0:
        break
    sum_of_numbers += user_input
    count += 1
if count > 0:
    average = sum_of_numbers / count
    print("The avarage of the number entered is", average)    
else:
    print("No number entered")








