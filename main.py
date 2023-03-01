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
  


  
