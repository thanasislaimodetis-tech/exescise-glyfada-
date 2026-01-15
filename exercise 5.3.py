def num_digits(n):
    count = 0
    while n >= 1:
        n = n / 10
        count += 1
    return count
def main():
    user_input = input("Please enter a positive whole number:\n")
    if user_input.isdigit() and int(user_input) > 0:
        number = int(user_input)
        digits = num_digits(number)
        if digits == 1:
            print(f"{number} has {digits} digit.")
        else:
            print(f"{number} has {digits} digits.")
    else:
        print("Invalid input.")
if __name__ == "__main__":
    main()            