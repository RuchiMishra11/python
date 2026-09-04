def add(x,y):
     z=x+y
     return z
def subtract(x,y):
     z=x-y
     return z
def multiply(x,y):
     z=x*y
     return z
def divide(x,y):
     z=x/y
     return z

print(add(3,4)) #7
print(subtract(5,6)) #-1
print(multiply(9,8)) #72
print(divide(78,2)) #39
# creating caluculator using  above  defined function :
x=int(input("Enter the 1st number:"))
y=int(input("Enter the 2nd number:"))
operation=input("Enter the opration you wanna perform (add/subtract/multiply/divide):")
if operation=="add":
    print(f"{x}+{y}={add(x,y)}")
elif operation=="subtract":
    print(f"{x}-{y}={subtract(x,y)}")
elif operation=="multiply":
    print(f"{x}x{y}={multiply(x,y)}")
elif operation=="divide":
    print(f"{x}/{y}={divide(x,y)}")
else:
    print("The operation you have entered is not defined by our system.")

def name(first_name , last_name):
    first_name=first_name.capitalize()
    last_name=last_name.capitalize()
    return(first_name+" " +last_name)
list_of_name=[]
while True:
    choice=input("Do you wanna enter names?(y/n):").lower()
    if choice=="y":
            first_name=input("Enter first name :")
            last_name=input("Enter last name:")
            full_name=name(first_name,last_name)
            list_of_name.append(full_name)
    elif choice=="n":
         break
    else:
         print("Invalide choice,please enter your choice again!")
print("Thanks for your time!")
print(list_of_name)

def invoice(username,amount,due_date):
     print(f"Hello,{username.capitalize()}!")
     print(f"Your total amount is Rs{amount},")
     print(f"it should be paid by {due_date}.")


invoice("joe",300,"1/02")

#DEFAULT ARGUMENTS IN A FUNNCTION: Default arguments allow you to initialize a function parameter with a default value.
# ❌ SyntaxError: non-default argument follows default argument
# def invoice(currency="Rs", username, amount):
#     pass

# ✅ Correct: Required parameters first, optional/default parameters last
def invoice(username, amount, currency="Rs"):
    pass

import time
import os
def count(end , start=0):
     for x in range(start,end+1):
          os.system("cls")
          print(x)
          time.sleep(1)

end=int(input("Enter the count:"))
print(count(end))

