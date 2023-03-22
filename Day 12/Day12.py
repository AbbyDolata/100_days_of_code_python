enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#practice with scope 
player_health=10
#this has global scope
def increase_health():
  player_health=10
  potion_strength=2
  player_health+=potion_strength
  print(player_health)
#everything inside of the function has local scope 
  
increase_health()
#when you run the function, player health will equal 12
print(player_health)
#when you print player health outside of the function, it equals 10

#python does not have block scope 
game_level=4
enemies=["skeleton", "slime", "mosquito","bat","ghost"]
if game_level<5:
  new_enemy=enemies[0]
print(new_enemy)
#if statements have global scope unless embedded inside of a function. this means they are accessable to code outside of their indentation or block of code 

#Number Guessing Game
from random import randint
from replit import clear

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

logo=("""   ______                        __  __            _   __                __             
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
""")

def set_difficulty():
  difficulty=input("Choose a difficulty.Type in 'easy' or 'hard': ")
  if difficulty=="easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS
  
  
def game():
  clear()
  print(logo)
  print("Hello and welcome to the number guessing game!\nI'm thinking of a number between 1 and 100")
  turns=set_difficulty()
  print(f"You have {turns} attempts left.")
   
  randnum=randint(1,100)
  guess=int(input("Make a guess: "))
  
  contgame=True
  while contgame==True:
    if turns==0:
        print("You lose")
        print(randnum)
        contgame=False
        again=input("would you like to play again? types 'y' for yes or 'n' for no: ") 
        if again=="y":
          game()
        if again=="n":
          clear()
          print("Goodbye")
    if guess==randnum:
      print("You win!")
      print(guess)
      contgame=False
      again=input("would you like to play again? types 'y' for yes or 'n' for no: ") 
      if again=="y":
        game()
      if again=="n":
        clear()
        print("Goodbye")
        
    if guess < randnum and turns>=1:
      turns-=1
      print("Your guess is too low.")
      print(f"you have {turns} lives left")
      guess=int(input("guess again: "))
      contgame=True
 
    if guess > randnum and turns>=1:
      turns-=1
      print("Your guess is too high.")
      print(f"you have {turns} lives left")
      guess=int(input("guess again: "))
      contgame=True
 
game()