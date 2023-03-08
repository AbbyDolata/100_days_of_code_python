#student scores
#create a code that changes student scores into grades
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades={}
for student in student_scores:
    score=student_scores[student]
    if score >90:

        student_grades[student]="Outstanding"
    if score > 80 and score < 91:
        student_grades[student]="Exceeds Expectations"
    if score > 70 and score < 81:
        student_grades[student]="Acceptable"
    if score < 71:
        student_grades[student]="Fail"

print(student_grades)

#travel log
#create a code that adds new entries to a pre existing dictionary that contains places that have been traveled to
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited,times_visited,cities_visited):
    new_entry={}
    new_entry["country"]=country_visited
    new_entry["visits"]=times_visited
    new_entry["cities"]=cities_visited   
    travel_log.append(new_entry)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#annon auction
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