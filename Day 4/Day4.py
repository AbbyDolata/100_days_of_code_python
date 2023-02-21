#importing and using modules 
import mymod
print(mymod.rannum)

import random 
ranfloat=random.random()
print(ranfloat)

ranint=random.randint(0,5)
print(ranint)

#how do you get a random number between 0 and 5 if the ranfloat only goes from 0.00000000 and 0.9999999?
ranfloat*5
print(ranfloat)
#get a random number between 0.000000 and 4.99999999

#random number generator
import random 
rand_num=random.randint(0,1)
if rand_num == 0:
    print("Heads")
else:
    print ("Tails")

#random name picked from a list given 
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random 
numnames=len(names)
ranname=names[random.randint(0, numnames-1)]
#last number is the total number in the list -1 because we start counting at zero while len function starts counting at 1
print(f"{ranname} is going to buy the meal today!")

#put an x on the map

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position =input("Where do you want to put the treasure? ")

p1=int(position[0])
p2=int(position[1])

#given a coordinate 1-3
#use it to put an x on the map, using indicies from 0-2 

selected_row=map[p2-1]
selected_row[p1-1]="x"
#rewatch video explaining this b/c shes confusing me 
#choosing how far down you go before choosing hwo far left or right to move 
print(f"{row1}\n{row2}\n{row3}")
#see if there is another version of this i can do, i need more practice with this 

#rock, paper, scissors 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
chosen=int(input("what do you choose? Type 0 for rock, 1 for paper, or 2 for scissors\n"))
import random
comprand=random.randint(0,2)

if chosen>=3 or chosen<0:
  print("you typed in an invalid number, you lose.")
elif chosen==0:
  print(rock)
elif chosen==1:
  print(paper)
elif chosen==2:
  print(scissors)
elif comprand==0:
  print(rock)
elif comprand==1:
  print(paper)
elif comprand ==2:
  print(scissors)



if chosen==0 and comprand==0:
  print("It's a tie.")
elif chosen==0 and comprand==1:
  print("Computer wins.")
elif chosen==0 and comprand==2:
  print("You win!")
elif chosen==1 and comprand==0:
  print("You win!")
elif chosen==1 and comprand==1:
  print("It's a tie.")
elif chosen==1 and comprand==2:
  print("Computer wins.")
elif chosen==2 and comprand==0:
  print("Computer wins.")
elif chosen==2 and comprand==1:
  print("You win!")
elif chosen==2 and comprand==2:
  print("It's a tie.")

#if input is 0 and computer picks 0, its a tie
#if input is 0 and computer picks 1, computer wins
#if input is 0 and computer picks 2, computer loses
#if input is 1 and computer picks 0, you win
#if input is 1 and computer picks 1, tie
#if input is 1, and computer picks 2, computer wins
#if input is 2, and computer picks 0, computer wins
#if input is 2, and computer picks 1, computer loses
#if input is 2 and computer picks 2, its a tie

#other way of completing rock paper scissors exercise
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_choice=int(input("what do you choose? Type 0 for rock, 1 for paper, or 2 for scissors\n"))
computer_choice=random.randint(0,2)
game_images=[rock, paper, scissors]

if user_choice>=3 or user_choice <0:
  print("You have put in an invalid number, you lose.")
else:
  print(f"you chose: {game_images[user_choice]}") 
  print(f"The computer chose {game_images[computer_choice]}")
  if computer_choice==user_choice:
    print("It's a draw.")
  elif user_choice==0 and computer_choice==2:
    print("You win!!")
  elif user_choice==2 and computer_choice==0:
    print("You lose")
  elif user_choice> computer_choice:
    print("You win!")
  elif computer_choice> user_choice:
    print("You lose.")
  