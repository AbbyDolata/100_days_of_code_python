#goal of code is to take a two digit number input and add the two numbers together
#for example, the input is 21, 2+1=3
two_digit_number = input("Type a two digit number: ")
a=int(two_digit_number[0])
b=int(two_digit_number[1])
print(a+b)

#BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi=(int(weight)/float(height)**2)
bmi_as_int=int(bmi)
print(bmi_as_int)

#made a calculation to see how many days, weeks, and months left until one hits 90
age = input("What is your current age? ")
years=(90-int(age))
months=(years*12)
weeks=(years*52)
days=(years*365)
print(f"you have {days} days, {weeks} weeks, and {months} months left.")

#tip calculator 
bill=input("Hello, this is a tip calculator, how much was your bill?\n")
split=input("How many ways was the bill split?\n")
tip=input("How much would you like to tip; 15%, 18%, or 20%?\n")
amount1=int(bill)/int(split)
amount2=(int(tip)/(100))
amount3=amount1*amount2
final_amount=amount1+amount3
final_final_amount=round(final_amount,2)
print(f"each person should pay {final_amount}")