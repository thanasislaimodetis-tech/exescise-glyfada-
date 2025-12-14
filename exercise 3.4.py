product = 99
copies = int(input("Please enter number of copies purchased:\n"))

if copies >4 and copies < 10:
    print("You have been given a 10% discount on the normal price of 99$.\nThe total cost is", product * copies * 0.9, "$")
elif copies > 9 and copies < 20:
    print("You have been given a 20% discount on the normal price of 99$.\nThe total cost is", product * copies * 0.8, "$")
elif copies > 19 and copies < 50:
    print("You have been given a 30% discount on the normal price of 99$.\nThe total cost is", product * copies * 0.7, "$")
elif copies > 49 and copies < 100:
    print("You have been given a 40% discount on the normal price of 99$.\nThe total cost is", product * copies * 0.6, "$")
elif copies > 99:
    print("You have been given a 50% discount on the normal price of 99$.\nThe total cost is", product * copies * 0.5, "$")
else:
    print("The total cost is", product * copies, "$")

    