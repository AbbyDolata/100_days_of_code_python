#practice with output functions
#turning names into Title Strings

f_name= input("What is your first name?: ")
l_name=input("What is your last name?: ")
def format_name(f_name,l_name):
  """turns a given first and last name into the title version of the name. capitalizes the first character in first and last name"""
  titlenamef=f_name.title()
  titlenamel=l_name.title()
  return f"{titlenamef} {titlenamel}"

format_output=format_name(f_name=f_name,l_name=l_name)
print(format_output)


#Days in month function
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  if month> 12 or month<1:
      return "you have put in an invalid input"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month== 2:
      return 29
  return month_days[month-1]  
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#calculator
from art import logo 
from replit import clear

def add(n1, n2):
  return n1+n2
def subtract(n1, n2):
  return n1-n2
def multiply(n1, n2):
  return n1*n2
def divide(n1, n2):
  return n1/n2
def power(n1, n2):
  return n1**n2

operations= {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
  "**":power,
}

def calculator():
  print(logo)
  num1=float(input("what is the first number you would like to put in?: "))
  
  for symbol in operations:
    print(symbol)
    
  cont=True
  while cont==True:
    
    operation_symbol=input("Pick an operation: ")
  
    num2=float(input("What is the next number you would like to use?: "))
  
    calculation_function=operations[operation_symbol]
  
    answer= calculation_function(num1,num2)
  #answer vaariable is using the calculation_function variable, using inputs num1 and num2 and the input operation symbol to run whichever function is to be used based on picked operation on the two number inputs 
  
    print(f"{num1} {operation_symbol} {num2}= {answer}")
    
    yorn=input(f"would you like to continue your calculations with the number {answer}? type 'y' for yes and 'n' for starting a new calculation:  ")
    if yorn=="n":
      cont=False
      clear()
      calculator()
      #call function inside of function to create a recursion, or a function that can call itself, this way, you do not have to run again to get a repeat
      
    elif yorn=="y":
      num1=answer
      cont=True
    
calculator()
#call function after defining it so computer knows where to begin