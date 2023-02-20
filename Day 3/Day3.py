#if/else functions 
print("hello, welcome to the rollercoaster")
height_in_cm=int(input("what is your height in cm?"))
if height_in_cm > 120:
  print("you can ride the rollercoaster")
else:
  print("you cannot ride the rollercoaster")

#is a number even or odd?
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
  
#nested if/else conditions
print("Hello welcome to the roller coaster")
height=int(input("what is your height in cm"))
if height >=120:
  print("you can ride the rollercoaster")
  age=int(input("what is your age?"))
  if age >=18:
    print("you pay 12$")
  else:
    print("you pay 7$")
else:
  print("you cannot ride this rollercoaster, you must get taller first.")
  
#if/elif/else statements
print("Hello welcome to the roller coaster")
height=int(input("what is your height in cm?"))
if height >=120:
  print("you can ride the rollercoaster")
  age=int(input("what is your age?"))
  if age <12:
    print("please pay 5$")
  elif age <= 18:
    print("please pay 7$")
  elif age <= 60:
    print("please pay 12$")
  else:
    print("please pay 5$")
else:
  print("you cannot ride this rollercoaster, you must get taller first.")
  
#updated BMI calculator 
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI= round(int(weight)/float(height)**2)
if BMI <18:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI <25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI <30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI <35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
  
#Leap year calculator 
year = int(input("Which year do you want to check? "))
if year%4 !=0:
    print("Not leap year.")
else:
    if year%100!=0:
        print("Leap year.")
    else:
        if year%400==0:
            print("Leap year.")
        else:
            print("Not a leap year.")
          
#other method of the leap year checker 
year=int(input("what year would you like to test?"))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print("Leap year.")
    else:
      print("Not a leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
#lets try to do multiple if statements by myself 
print("Hello, welcome to the movie theater.")
#how old are you?
#would you like some popcorn?
#would you like some candy? 
#final bill is_
age=int(input("How old are you?"))
if age <=12:
  bill=7
  print("Your ticket will be 7$.")
elif age <18:
  bill=12
  print("Your ticket will be 12$.")
else:
  bill=15
  print("Your ticket will be 15$.")
  
popcorn=input("Would you like to buy some popcorn? click y for yes and n for no. ")
if popcorn =="Y":
  bill+= 10
  
candy=input("Would you like to purchase some candy? click Y for yes and N for no. ")
if candy=="Y":
  bill+= 5

print(f"Your total is {bill} dollars. Enjoy the movie!")

#Pizza order simulator
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
  bill=15
  if add_pepperoni =="Y":
    bill+=2
if size == "M":
  bill=20
  if add_pepperoni == "Y":
    bill+=3
if size == "L":
  bill=25
  if add_pepperoni =="Y":
    bill+=3
if extra_cheese == "Y":
  bill+=1
  
print(f"your final bill is: ${bill}.")

#Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

notfalse= name1.lower()+name2.lower()
a=notfalse.count("t")
b=notfalse.count("r")
c=notfalse.count("u")
d=notfalse.count("e")
num1=a+b+c+d

e=notfalse.count("l")
f=notfalse.count("o")
g=notfalse.count("v")
h=notfalse.count("e")
num2=e+f+g+h

score=str(num1)+str(num2)
score2=int(score)

if score2 <10 or score2 >90:
    print(f"Your score is {score2}, you go together like coke and mentos.")
elif score2 >40 and score2 <50:
    print(f"Your score is {score2}, you are alright together.")
else:
    print(f"Your score is {score2}.")

#Treasure island 
('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************)
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
Q1=input("you begin your journey at a crossroad. Left or Right?\n")
Q1=Q1.lower()
if Q1 == "left":
    Q2=input('The tunnel on the left takes you down a long flight of stairs. As you descend into the darkness you can hear the faint sound of running water. Eventually you come across a large underground lake, the water is so dark that anything could be lurking just below the surface. chose to either "wait" or "swim"\n')
    Q2=Q2.lower()
    if Q2 == "wait":
        Q3= input("Your patinece has paid off and across the water you can see a ferryman on a small boat approaching. he allows you to board and takes you across the murky depths. He leaves you at the other side with two doors in front of you and the vast expanse of water behind you. Which door will you choose, a red door,a green door or a blue door?\n")
        Q3=Q3.lower()
        if Q3== "red":
            print("The red door leads to a dark room, lit by a few torches nearly burnt to their ashes. In the center of the room is the treasure. You can now take the teeasure and leave this adventure behind. Congratulations!")
        elif Q3== "green":
          print("The green door led to an empty room with spouts on the wall. once you step inside, the room quickly fills with water. There is no escape.")
        else:
            print("The blue door led to an arena, where at the center lies a dragon. You fought bravely but were ultimately roasted alive. Try again.")
    else:
        print("You were impatient and tried to swim in the murky water. Unknown to you, a very hungry and very large squid lives in the depths. You were quickly ensnared in its tenticles and had no chance to even fight before being plunged below the surface, never to be seen again. Try again.")
else: 
    print("The other passage lead to a massive trap. you were locked inswide a box of four walls, slowly closing in. There is no escape. Try again.")