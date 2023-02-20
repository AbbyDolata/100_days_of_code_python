print('''
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
        Q3= input("Your patinece has paid off and across the water you can see a ferryman on a small boat approaching. He allows you to board and takes you across the murky depths. He leaves you at the other side with three doors in front of you and the vast expanse of water behind you. Which door will you choose, a red door,a green door, or a blue door?\n")
        Q3=Q3.lower()
        if Q3== "red":
            print("The red door leads to a dark room, lit by a few torches nearly burnt to their ashes. In the center of the room is the treasure. You can now take the teeasure and leave this adventure behind. Congratulations!")
        elif Q3== "green":
          print("The green door led to an empty room with spouts on the wall. once you step inside, the room quickly fills with water. There is no escape. Try again.")
        else:
            print("The blue door led to an arena, where at the center lies a dragon. You fought bravely but were ultimately roasted alive. Try again.")
    else:
        print("You were impatient and tried to swim in the murky water. Unknown to you, a very hungry and very large squid lives in the depths. You were quickly ensnared in its tenticles and had no chance to even fight before being plunged below the surface, never to be seen again. Try again.")
else: 
    print("The other passage lead to a massive trap. you were locked inside a box of four walls, slowly closing in. There is no escape. Try again.")



