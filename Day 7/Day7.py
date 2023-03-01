#grocery list, each time i buy something, replace the grocery item with an x
#array list
grocery_list=["egg","apple","avacado","crackers","tomatoes","potatoes","bread","milk","cookies"]
buyanything=input("what did you remember to buy today? Input here: ")

for item in range(len(grocery_list)):
  acquired=grocery_list[item]
#acquired is just the item in grocery list being checked by loop at a given time through
  if acquired==buyanything:
#if the item currently being checked by the for loop matches its bought
    grocery_list[item]="X"
#the item will be replaced with an X
#the brackets around the loop variable is exactly that, a variable that only applies while inside the loop, applies to one particular thing in a list in a loop
print(grocery_list)

#hangman
import hangman_art
import random
import hangman_words
from replit import clear

print(hangman_art.logo)

word_list=hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

stages=hangman_art.stages
end_of_game = False
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
#display is all of the letters guessed, can go back in it to check and see if a guess has already been made or not
guessed=str()
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    guessed+= guess
    if guess in display:
        print(f"You input {guess}. You have already guessed that letter.")
    print(f"Your guesses: {guessed}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        #the above comment is strictly for debugging purposes 
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word.")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}.")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    #goes from list to string 

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
    