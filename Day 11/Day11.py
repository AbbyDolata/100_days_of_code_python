#creating a game of Blackjack

from art import logo 
from replit import clear
import random 

def deal_card():
  """Randomly choses cards from the list cards, the return function will replace where the function is called with the randomly chosen cards"""
  cards=[11, 2, 3, 4, 5, 6, 7,8, 9, 10,10,10,10]
  card=random.choice(cards)
  return card 

def calculate_score(cards):
  """ Takes a list of cards and returns the score calculated from the cards"""
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(player_score, computer_score):
  if player_score>21 and computer_score>21:
    return "You went over, you lose."
  elif player_score==computer_score:
    return "Draw"
  elif computer_score==0:
    return "You lost, computer won with a BlackJack"
  elif player_score==0:
    return "You win with a BlackJack"
  elif player_score>21:
    return "You went over, you lose"
  elif computer_score>21:
    return "Computer went over, you win"

  elif player_score >computer_score:
    return "You win"
  else:
    return "You lose"

def play_game():
  print(logo)
  player_cards=[]
  computer_cards=[]
  is_game_over=False

  for num in range(2):
  #will run through this loop twice, each time, the deal_card() function is replaced and then added to a list for both the player_cards and the computer_cards. the numbers will be different for both lists as they are called separate times 
    player_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_game_over:
    player_score=calculate_score(player_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards are {player_cards}, current score is {player_score}:")
    print(f"one of the computers cards is {computer_cards[0]}")
    if player_score==0 or computer_score==0 or player_score>21:
      is_game_over=True
    else:
      anothercard=input("would you like to draw another card? Type 'y' for yes and 'n' for no: ")
    if anothercard=="y":
      player_cards.append(deal_card())
    else:
      is_game_over=True
  
  while computer_score !=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score= calculate_score(computer_cards)
  print(f"   Your final hand: {player_cards}, final score: {player_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(player_score, computer_score))
 
while input("Do you want to play a game of BlackJack? Type 'y' for yes and 'n' for no: ")=="y":
  clear()
  play_game()