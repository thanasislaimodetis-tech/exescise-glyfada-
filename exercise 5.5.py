import random

def get_user_guess():
   
    while True:
        guess = input("Please enter a whole number between 1 and 10 or q to quit\n")
        
       
        if guess == 'q':
            return guess
        
 
        if guess.isdigit():
            val = int(guess)
            if 1 <= val <= 10:
                return guess 
       
        print("Invalid input")

def print_feedback(no_guesses, max_guesses, secret_num):
    """
    Τυπώνει το μήνυμα νίκης ή ήττας ανάλογα με τις προσπάθειες.
    """
    if no_guesses > max_guesses:
        print("Sorry, better luck next time.")
    else:
        print(f"Well done, you used {no_guesses}/{max_guesses} guesses to guess the secret number {secret_num}.")

def main():
    secret_num = random.randint(1, 10)
    keep_going = True
    max_guesses = 3
    no_guesses = 0
    
    while keep_going:
        if no_guesses < max_guesses:
            guess = get_user_guess()
            if guess == "q":
                keep_going = False
            else:
                if int(guess) == secret_num:
                    keep_going = False
                else:
                    print("Incorrect, please try again")
        else:
            keep_going = False
            
        no_guesses += 1
        
    if guess == "q":
        print("User exited the program.")
    else:
        print_feedback(no_guesses, max_guesses, secret_num)

if __name__ == "__main__":
    main()