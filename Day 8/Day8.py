def prime_checker(number):
    is_prime=True
    for num in range(2,number):
        if number % num ==0:
            is_prime=False
    # checking to see if the input number is divisible by each number in a range starting from 2 and ending at the number before the given input. if any of these numbers divide evenly, then it is NOT a prime number
    #at the end of the for loop, we check and see the standing of the variable is_prime. if it changed to false, not prime, if did not change, prime 
    if is_prime==True:
        print("It's a prime number")
    if is_prime==False:
        print("It's not a prime number.")
    
n = int(input("Check this number: "))
prime_checker(number=n)

#paint area calculator
import math

def paint_calc (height, width, cover):
    calc=((height*width)/(cover))
    print(f"You'll need {math.ceil(calc)} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#caesar cypher- what i initially had
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(plain_text, shift_amount,direction):  
  end_text="" 
  for letter in plain_text:
    position = alphabet.index(letter)
    if direction =="encode":
      new_position=position + shift_amount
      end_text += alphabet[new_position]        
    if direction =="decode":
      new_position=position - shift_amount
      end_text +=alphabet[new_position]
  print(f"Here's the {direction}d result: {end_text}")
  
ceasar(plain_text=text,shift_amount=shift, direction=direction)

#Caesar cypher complete
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  
  print(f"Here's the {cipher_direction}d result: {end_text}")

continuecypher=True
while continuecypher==True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 25:
    shift= shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  tocontinue=input("Do you wish to restart the program? type 'y' for yes and 'n' for no:")
  if tocontinue=="n":
    continuecypher=False
    print("Goodbye")