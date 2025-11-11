#if= do some code only if'if' condition is true 
#else print something  else
 #example
age=int(input("Enter your age :"))
if age >=100:
    print("you are too old to sign up !")
elif age>=18:
    print("you are signed up!")
elif age<=0:
    print("you are not born yet!")
else:
    print("You must me 18+ to sign up !")

#example 2 : Checking the responce 
responce=input("Would you like to have some food? (y/n):")
if responce=="y":
    print("Have it !")
else:
    print("okay,have a nice day!")

#example 3: asking users name 
name=input("what is your name ? :")
if name=="":
    print("You haven't entered your name!")
else:
    print(f"wellcom ,{name}.")

#Using if statement with  booleans 
# example 4:
is_online=True
if is_online:
    print("You are online!")
else:
    print("You are not online!")

#example 5:
a_teacher=False
if a_teacher:
    print("You are a teacher!")
elif a_teacher=="no":
    print("you are not teacher")
else:
    print("Are you a student?")

#example 6: python calculator
operator=input("Enter a arithmatic operator(+,-,/,*):")
num_1=float(input("Enter your first number:"))
num_2=float(input("Enter your second number:"))
if operator=="+":
    print(round(num_1+num_2))
elif operator=="*":
    print(round(num_1*num_2))
elif operator=="-":
    print(round(num_1 - num_2))
elif operator=="/":
    print(round(num_1/num_2))
else:
    print(f"Operator {operator} you have entered is not valid!")

#example 7:python weight convertor
weight=float(input("Enter your weight:"))
unit=input("Killograms or Pounds (K/L):")
if unit=="K":
    weight=weight*2.205
    unit="lbs"
    print(f"Your weight is:{round(weight)}{unit}.")
elif unit=="P":
    weight=weight/2.205
    unit="kg"
    print(f"Your weight is:{round(weight)}{unit}.")
else:
    print(f"{unit} is not valid.")

#example 8: temperature converter 
temperature=float(input("enter your temperature:"))
unit=input("Is this temperature is in celcius or farenheit? (C/F):")
if unit=="C":
    temperature=(round((temperature*9)/5 + 32))
    unit="Farenheit"
    print(f"your temperature is :{temperature}{unit}.")
elif unit=="F":
    temperature=(round((temperature-32)*5/9))
    unit="celcius"
    print(f"your temperature is :{temperature}{unit}.")
else:
    print(f"unit {unit} you have entered is not valid !")

#conditional expression= one line shortcuts for if else statement (ternary operator)
# print or assign one of the two value based on condition
# X if condition else Y

num=int(input("Enter your number:"))
print("Positive" if num>0 else "negative")
print("Even" if num%2==0 else "Odd")
a=8
b=4
print(a if a>b else b)
print(a if a<b else b )
age=int(input("Enter your age:"))
print("Adult" if age>=18 else "Child")
temperature=int(input("Enter temperature:"))
print("surrounding is hot" if temperature> 30 else " surrounding is cold")
user_role=input("Enter use role:")
print("Full access" if user_role=="admin" else "Limited access")

#chat gpt practice problem 
# practice problem 1: checking pass and fail based on the marks 
marks=int(input("Enter your marks :"))
print("Pass"if marks>=35 else "Fail")
#practice problem 2: printing absolute of a number
num=int(input("Enter your number:"))
print(-num if num<0 else num)