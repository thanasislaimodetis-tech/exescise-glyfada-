def test_input(user_input):
   
    if len(user_input) != 5:
        return False
    if not user_input.isalpha():
        return False
    return True

def get_input():
   
    while True:
        guess = input("Please enter your 5 letter guess: ")
        if test_input(guess):
            return guess
        else:
            print("You must enter a 5 letter word with no symbols or digits.")

def test_word(secret_word, user_guess):
   
    feedback_string = ""
    correct = True
    
   
    for i in range(5):
      
        if user_guess[i] == secret_word[i]:
            feedback_string += "G"
        else:
         
            correct = False 
            
          
            printed = False
            for char in secret_word:
                if user_guess[i] == char:
                    feedback_string += "Y"
                    printed = True
                    break 
            
            if not printed:
                feedback_string += "*"
    
    print(feedback_string)
    return correct

def start_game(secret_word):

    print("Welcome to Derble!")
    print("You have up to 6 attempts to guess the secret word!")
    
    attempts = 0
    running = True
    
    while running:
    
        guess = get_input()
        attempts += 1
        
     
        is_win = test_word(secret_word, guess)
        
   
        if is_win:
            print(f"Congrats! You took {attempts} attempts.")
            running = False
        elif attempts >= 6:
            print(f"Incorrect! You have {6 - attempts} attempts remaining.")
            print(f"The correct word was \"{secret_word}\". Better luck next time.")
            running = False
        else:
            print(f"Incorrect! You have {6 - attempts} attempts remaining.")


if __name__ == "__main__":
    start_game("error")