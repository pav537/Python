from random import randint
from art import guess_number
easy_level = 10
hard_level = 5

turns = 0

def check_answer(guess,answer,turns):
    """Checks answers againt guess. Return the number of remaining."""
    if guess > answer:
        print("Too.High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
       print(f"You got it! The answer was {answer}")


#Make function to set difficulty.
def set_diff():
   level = input("Choose difficulty. Type 'easy' or 'hard' : ")
   if level == "easy":
       return easy_level
   else:
       return hard_level
       
def game():      
# Choosing random Number between 1 and 100        
    print(f"{guess_number}")
    print("Welcome to Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    
    answer =randint(1, 100)
    
    turns = set_diff()
    guess = 0
    #repeatin the guessing function if they get wrong
    while guess != answer:
        
        print(f"You have {turns} attempts reamining to guess the number")
        
    # Let the users guess a number
        guess = int(input("Make a guess : "))
        
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You run out of guesses. You lose")
            return
        elif guess != answer:
            print("Guess again.")
        
    # function to check users' guess with actual answer


#track tye number of turns and reduce by 1 if they get wrong

game()
