cnt = 1
secret_guess = 3 
print("Welcome to the Number Guessing Game!") 
print("You need to try and guess the number between 1 and 10...") 
print("")
print("If you wish to exit the game enter 0...") 
print("")
guess = int(input("Please enter a guess:\n"))
if guess == 0:
    print(f"Program exited. The correct answer was {secret_guess}")
else:         
    while guess != secret_guess: 
        if guess >secret_guess and guess != 0:
            print("Your guess is too high, please try again.")
            guess = int(input("Please enter a guess:\n"))
            cnt +=1
            if guess == 0:
                print(f"Program exited. The correct answer was {secret_guess}")
                break
            elif guess == secret_guess:
                print(f"Well done the correct answer was {secret_guess}\nYou took {cnt} guesses.")
                break
        elif guess < secret_guess and guess != 0:
            print("Your guess is too low, please try again.")
            guess = int(input("Please enter a guess:\n"))
            cnt += 1
            if guess == 0:
                print(f"Program exited. The correct answer was {secret_guess}")
                break
            elif guess == secret_guess:
                print(f"Well done the correct answer was {secret_guess}\nYou took {cnt} guesses.")
                break