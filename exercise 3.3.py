convert = int(input("Enter 1 to convert Celsius to Fahrenheit or 2 to convert Fahrenheit to Celsius:\n"))


if convert == 1:
    celsius = float(input("Please enter the temporature in Celsius:\n"))
    fahrenheit = (celsius * 9/5) + 32
    if  celsius >= 0:
        print(f"{celsius} Celsius is euivalent to {fahrenheit} Fahrenheit.")
    else:
        print("ERROR: You must enter a value of 0  or greater.")

elif convert == 2:
    fahrenheit = float(input("Please enter the temporature in Fahrenheit:\n"))
    celsius = (fahrenheit - 32) * 5/9
    if fahrenheit >= 0:
        print(f"{fahrenheit} Fahrenheit is equivalent to {celsius} Celsius")
    else:
        print("ERROE: You must enter a value of 0 or greater.")

else:
    print("ERROR: Invalid option")


