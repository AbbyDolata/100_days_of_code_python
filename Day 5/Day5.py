#for loop
fruits=["Apple","Pear", "Banana", "Orange"]
for fruit in fruits:
  print(fruit)
  print(fruit + " pie")
  print(fruits)

#average height calculator(using only lists, not allowed to use sum or len function)
student_heights =input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] =int(student_heights[n])
sumofh=0
lengthoflist=0
for height in student_heights:
    sumofh+=height
    lengthoflist+=1
finalnum=sumofh/lengthoflist
print(round(finalnum))

#finding highest score without using the max function
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
  
highest_score=0
for score in student_scores:
    if score > highest_score:
        highest_score= score
print(f"The highest score in the class is: {highest_score} ")   

#adding only the even numbers 1-100, 2 different ways 
evenadd=0
for number in range (2,101,2):
    evenadd+= number
print(evenadd)

total=0
for number in range(1,101):
    if number%2==0:
        total+=number
print(total)

#FizzBuzz
for number in range(1,101):
    if number %3==0 and number %5==0:
       number="FizzBuzz"
       print(number)
    elif number %3==0:
        number="Fizz"
        print(number)
    elif number %5==0:
        number="Buzz"
        print(number)
    else:
        print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#use input to determine how many times a random choice is made
numb=int(nr_letters+nr_numbers+nr_symbols)
#have to put this first, otherwise, it gets messy

#empty variables so input can be recieved as output, turn into string, strings and integers can utilize the += function

password=str()
for letter in range(0,nr_letters):
  password+=random.choice(letters)

for symbol in range(0,nr_symbols):
  password+=random.choice(symbols) 
  
for number in range(0,nr_numbers):
  password+=random.choice(numbers)

print(password)
#end of easy way of creating a strong password, no randomization of order 

#hard way of generating password, shuffle password
epassword=random.sample(password, numb)
shuffpass=""
for char in epassword:
  shuffpass+=char
print(shuffpass)

#use for loop to move items from a list into a string
  