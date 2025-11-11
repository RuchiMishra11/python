# LEVEL 1 — Basic Input Validation
"""1. Ask the user to enter their age.
Keep asking until it's greater than 0 and less than 120.
2. Ask for a username.
Keep asking until it does not contain spaces and is not empty.
3. Ask the user for a number between 10 and 20.
Repeat until the number is in that range."""
#1
age= int(input("Enter your age: "))
while not(age>0 and age<120):
    print("Enter your valid age")
    age=int(input("Enter your age again: "))
print(f"okay ! you are {age}  years old.")
#2
username=input("Enter your username: ")
while username=="" or " " in username:
    print("Your username is not valid.")
    username=input("Enter your username again: ")
print(f"wellcome! {username}")
#3 
number=int(input("Enter a number:"))
while not (number>10 and number<20):
    print("This number is not valid.")
    number=int(input("Enter the  number between 10 and 20 : "))
print(f"You have entered {number}.")

# 2 — Using or and not

"""4. Ask for a favorite color.
Only accept "red", "blue", or "green".
Use while not (...).
5. Ask the user for a password.
Repeat until it's at least 8 characters and contains at least one digit.
6. Ask the user for a number.
Repeat until they enter a positive even number (use both % and and)."""
#4
color=input("Enter your favorite color: ")
while not (color=="red" or color=="blue" or color=="green"):
    print("Enter a valid color.")
    color=input("Enter your favorite color again: ")
print(f"You have entered {color}.")
#5
password=input("Enter your password: ")
while not (password>8 and any(ch.isdigit() for ch in password)):
    print("Your password is invalid.")
    password=input("Enter your password again : ")
print("wellcome!")
# 6
num=int(input("Enter a number:"))
while not(num>0 and num%2==0):
    print("Number is not valid!")
    num=int(input("Enter a number:"))
print(f"You have entered {num}.")

# 🧩 LEVEL 3 — Multiple Conditions

"""7. Ask for a temperature (in °C).
Keep asking until it's between -50 and 50 and not zero.
8. Ask the user for a mark (0-100).
If the user enters something outside that range, keep asking.

# 🧩 LEVEL 4 — Logical Traps (requires careful thinking)
9. Ask the user for a password again, but now it must:
Be at least 8 characters
Contain letters and digits only (isalnum())
Contain at least one uppercase letter
Repeat until valid."""
#7
temperature=int(input("Enter temperature in celcius: "))
while not(temperature>-15 and temperature <50 and temperature!=0):
    print("Temperature is not good !")
    temperature=int(input("Enter temperature again: "))
print(f"You have entered {temperature}°C.")
#8
marks=int(input("Enter your marks:"))
while not (marks>=0 and marks<=100):
    print("You have entered invalid marks.")
    marks=int(input("Enter your marks again :"))
print(f"okay! You got {marks} marks.")

#9
password=input("Enter your password: ")
while not (len(password)>8 and password.isalnum() and any(ch.upper() for ch in password)):
    print("Your password is invalid.")
    password=input("Enter your password again : ")
print("wellcome!")
