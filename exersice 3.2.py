celsius = float(input("Please enter the temporature in Celsius:\n"))
fahrenheit = (celsius * 9/5) + 32

if celsius >= 0:
    print(f"{celsius} Celsius is equivalent to {fahrenheit} Fahrenheit.")
else:
    print("ERROR: You must enter a value of 0 or greater.")
        