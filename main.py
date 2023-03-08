from replit import clear
from art import logo
print(logo)
print("Hello and welcome to the python auction, lets start bidding!")
bidder=""
bidamount=""
listofbids={}

def highest_bidder(listofbids):
  #listofbids={Angela:123, Jack:345}
  highest_bid=0
  for bidder in listofbids:
    amount=int(listofbids[bidder])
    if amount>highest_bid:
      highest_bid=amount
      winner=bidder
  print(f"The winner is {winner} with a bid of {highest_bid}")
  #first time through for loop, bidder is angela and amount is 123. 123 is higher than 0 so the highest_bid will be 123.
  #the second time through the for loop, bidder is jack and amount is 345. since 345 is larger than 123, highest_bid will equal 345. 

cont=True
while cont==True:
  bidder=input("What is your name?: ")
  bidamount=input("How much do you wish to bid?: ")
  listofbids[bidder]=bidamount
  morebids=input("Do you wish to put in another bid? type 'yes' or 'no': ")
  clear()
  if morebids=="no":
    cont=False
    highest_bidder(listofbids)
    
      


  
