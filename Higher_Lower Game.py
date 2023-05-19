from  art import higher_lower,vs
from  game_data import data
import random
import os
#Display art

score = 0
game_continue = True

account_b = random.choice(data)
def format_data(account):
    """Takes the account data and return the printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_follower,b_follower):
    
  """ Take the user guess and follower count an dreturn if they got it right."""
  if a_follower > b_follower:
       return guess == "a"
  else:
       return guess == "b"
         
print(higher_lower)

#make the game repeatable
while game_continue:
#Generate random data
#Making the accounts at position B become the next positon A

    account_a = account_b
    account_b = random.choice(data)
    
    
    while account_a == account_b:
        account_b = random.choice(data)
    #Format the account data into printable format
    print(f"Comapre A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")
    
    
    #ask user guess
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
    
    
    #Check if user is correct.
    ## Get follower counr of each account.
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    
    is_correct = check_answer(guess, a_follower_account, b_follower_account)
    
    
    #Give user feedback on their guesss.
    #score keeping
    if is_correct:
        score += 1
        print(f"You are right! Current score : {score}")
    else:
        game_continue = False
        print(f"Sorry, that's wrong! Current score : {score}")
    




#clear the screen between rounds 