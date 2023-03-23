#Describe Problem
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()
#the problem is in the first block of code, 20 is not included in the range that the for loop is running through, therefore it never prints the statement, have to change the range to 21 to include 20 (range goes from 1 up to 19, excluding 20)
def my_function():
  for i in range(1, 21):
    if i == 2:
      print("You got it")
my_function()
#above is the fixed function 

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num-1])
#the above error occurs because the integer chosen does not always correlate to an available number in the range of the list since randint includes both endpoints. when the integer 6 is chosen, the error is produced since there is not an item in the list that correlates to the number of 6. this is because, in programming, when assigning an integer to items in a list, we start at 0, so the dice image of 1 is actually at position 0 and the dice image of 6 is at position 5. by subtracting 1 from the chosen integer, the error is fixed. or, change the range to be between 0 and 5
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
#above it the fixed code, changing the range instead of subtracting 

# Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")
#the problem above is that the year of 1994 is excluded in both the millenial and Gen Z evaluation. so for millenials, years less thatn 1994 and above 1980 are millenial, not including 1994. for Gen Z, years above 1994 are Gen Z, not including 1994. when you have 1994 as the input for the above code, it prints out nothing since both if statements are evaluated as False.if you want to include 1994 in either statement, you need to add an equals sign to the right side of the greater than or less than sign, depending of iff you want 1994 to be the cut off for Gen Z or millenial. 
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")
#above is the code where 1994 is evaluated as Gen Z> an equals sign has been added to the right of the > sign. 

# Fix the Errors
age =input("How old are you?")
if age > 18:
print("You can drive at age {age}.")
#fix indent error at print statement
#change input into an integer so the < can evaluate as an int and int not a str and int
#change the print statement into an f string 
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")
#fixed code above :)

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
print(pages)
print(word_per_page)
total_words = pages * word_per_page
print(total_words)
#there is a second equals sign on line 61 that prevent the computer from storing the number of words on a page into the variable, so it comes out as 0(what it was set to in the original variable appearance)
#the print statements on lines 58 and 59 were added in by me to help visualize where the issue was coming from
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page =int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
#took out the second equal sign to fix the code 

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
#in the code above, the console just rpints out 26. this is because the append function to add the items to the list is outside of the for loop, so only the last number multiplied by 2 gets added to the list, which is why we get 26 instead of [2,4,6,10,18,26] like we want 
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
#above is the fixed code, i just indented the append function to be inside of the for loop 