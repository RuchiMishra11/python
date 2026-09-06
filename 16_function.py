#Calling Function  def function_name(arg1,arg2) here arg1 and arg2 are arguments 
#Postional argument (x,y)

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
def count(end , start=0):  #here start  value is set to be 0 and when we are calling function
                           # we don't neccessary have to give start argument but if we want something other as starting point we can give .
     for x in range(start,end+1): 
          print(x)
          time.sleep(1)
     print("Done!")
   


end=int(input("Enter the count:")) 
count(end) #without any starting argument it will start from 0 cuz it's default value
count(end,1)#here starting  value is set to be  1 

#KEYWORD ARGUMENT  
"""keyword arguments = arguments prefixed with the names of parameters
order of the arguments doesn't matter
helps with readability
"""

def greet(greeting,title,firstname, lastname):
     print(f"{greeting.capitalize()}, {title.capitalize()}.{firstname.capitalize()} {lastname.capitalize()}")
greet("hello",title="mr",firstname="jame",lastname="john") #Hello, Mr.Jame John
greet("hello",firstname="jame", title="mr",lastname="john") #Hello, Mr.Jame John (will print the same order doen't matter when we use keyword argument)
#Note
# greet(lastname="john",title="mr",firstname="jame","hello")  #give syntax error cuz positional argument always come before keyword argument

#Built in keyword argument of print() function in python 
sep="some value"
print("1","2","3","4",sep="-")
print("a","b","c","d", sep="-") # it control what's between multiple string 
end=" " #a keyword argument of print() function
print("Hello",end=",")
print("Your work is done!")

print("a","b","c","d", end="-") # it decides what come after we finish print statement

#
def table(*args):  #(*args) this argument can take upto multiple value and store it in a tuple
    total=0
    for arg in args:  #when we iterate over it it give value that we pass into a function later on
        # print(arg,end=",") # this will print the value that we pass into function
        total+=arg
    print(total)
        
table(2,3,4,5) # since function consist of **args this will create a tuple of  these value then iterate over it 
table

#practice set 
"calculating  sum and average "
def stats(*numbers):
    total=0
    for number in numbers:
        total+=number
    print(f"Sum of all the number is :{total}")
    print(f"Average of all the number is:{total/len(numbers)}")

stats(1,2,3,4)

numbers = [12, 45, 2, 89, 34, 67]
max_value=numbers[0]
for num in numbers:
    if num>max_value:
        max_value=num
print(f"The maximum value is {max_value}")

#creating max function 
def max(*numbers):
    max_value=numbers[0]
    for number in numbers:
        if number> max_value:
            max_value=number
    print(f"The maximum value is {max_value} ")

max(1,2,3,4,57,60)

" Count how many arguments were passed"
def count(*args):
    print(f"{len(args)} argument is being received.")
count(2,3,"k","p") 

#**kwarg argument take multiple keyword=value pair and store the into dictionary
def address(**kwargs):  #this will take value and store it in dictionary take keyword as key and assigned value as value
    print(type(kwargs)) #it will print >>dict
    for key,value in kwargs.items():
        print(f"{key:6}: {value:}")

address(street="123 Fake St.",
        pobox="P.O Box 777",
        city="Detroit",
        state="MI",
        zip="54321")

#PRACTICE SET
"1. Print a formatted profile"
def profile(**kwargs):
    for key ,value in kwargs.items():
        print(f"{key.capitalize():6}:{value.capitalize()if isinstance(value,str) else value}")
profile(name="ruchi",
        age=18,
        city="Mumbai")


"2. Check if a specific key was provided"
def email_check(**emails):
    print(emails.get("email","Email not found!"))
email_check(name="Ruchi",city="Mumbai")
email_check(name="Ruchi",city="Mumbai",email="iam@gmail.com")

"3. Sum only the numeric values"
def scorecard(**marksheet):
    total=0
    print("-----Marksheet-----")
    for k,v in  marksheet.items():
        print(f"{k.capitalize():8}:{v}")
        total+=marksheet.get(k)
    print(f"{"Total":8}:{total}")

scorecard(maths=60,science=80,english=90)

"4. Combine *args and **kwargs in the same function"
def fun(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    for k,v in kwargs.items():
        print(f"{k.capitalize()}:{v.capitalize()}")

fun("hello,","the details are:",name="ruchi",age="18")

#programs of  calling function 

# 1. Positional arguments — a shipping cost calculator 
def shipping_cost( weight, distance):
    cost=weight*distance *4 #4 is made rate per km 
    return print(f"As per the data provided cost is {cost}.")
shipping_cost(45,5)



# 2. Keyword arguments — booking a flight seat, order shouldn't matter
def book_seat(passenger, seat_number, class_type):
    return passenger , seat_number, class_type
print(book_seat(class_type="Bussiness",passenger="kei",seat_number="13A"))
# 3. Default arguments — a coffee shop order
def order_coffee(size="Medium", sugar=True):
    return print(f"Size:{size},Sugar:{sugar}")
order_coffee("Large")



    
# 4. Default + required mixed — a discount calculator
def apply_discount(price,discount_percent=10):
    total=price -(discount_percent*price)/100
    print(total)
apply_discount(500)
apply_discount(500,25)
# 5. *args — a grocery bill total
# Write  that sums up any number of item prices handed to it, since a shopping cart could have 2 items or 20. Call it with a few different-length carts to prove it's flexible.
def bill_total(*items_prices):
    total=0
    for price in items_prices:
        total+=price
    print(total)
# 6. **kwargs — a customizable user profile
print("-------Information--------")
def create_profile(**details):
    for k,v in details.items():
        print(f"{k.capitalize():7}:{v.capitalize()}")
create_profile(name="Ruchi", age="18")
create_profile(name="kei",email="kei@gmail.com")



# 7. Combining *args and **kwargs — a restaurant order system
# Write  — table_number is required, *dishes captures any number of ordered items, and **preferences captures optional notes like . Call it with a realistic order.
def place_order(table_number, *dishes, **preferences):
    print("======New Order======")
    print(f"{"Table No.":9}:{table_number}")
    for dish in dishes:
        print(f"-{dish.capitalize()}")

    for k,v in preferences.items():
        print(f"{k}={v}")
    print("=======================")

place_order(3,"pizza","Nachos","coke",spice_level="Mild",Onlion=True)






