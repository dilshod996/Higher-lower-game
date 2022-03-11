from game_data import data
import random
from art import vs, logo
from replit import clear



def random_account():
  return random.choice(data)
  

def data_info(person):
  name = person['name']
  # number = person['follower_count']
  descrip = person['description']
  country = person['country']
  return f" {name}, {descrip}, from {country} "
def check_followers(guess, first_followers, second_followers):
  if first_followers> second_followers:
    return guess == "a"
  else:
    return guess == "b"
  
def game():
  print(logo)
  score = 0
  continue_game = True
  person_1 = random_account()
  person_2 = random_account()

  while continue_game:
    person_1 = person_2
    person_2 = random_account()
    while person_1 == person_2:
      person_2 = random_account()
    print(f"Compare A: {data_info(person_1)}.")
    print(vs)
    print(f"Against B: {data_info(person_2)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    person_1_follower = person_1["follower_count"]
    person_2_follower = person_2["follower_count"]
    right_all = check_followers(guess, person_1_follower, person_2_follower)
    
    
    clear()
    print(logo)
    if right_all:
      score+=1
      print(f"You're right! Current score: {score}")
    else:
      continue_game = False
      print(f"Sorry, that's wrong. Final score: {score}")
    
game()