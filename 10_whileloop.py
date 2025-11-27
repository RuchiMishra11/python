#while loop = perform some code WHILE some condition remains true
#----------------Example:1---------------
name=input("Enter your name:")
while name =="":
    print("You did not enter your name:")
    name=input("Enter your name:")
print(f"wellcome {name}.")

#-------------Example:2------------------
age = int(input("Enter your age: "))

while age < 0:
   print("Age can't be negative")
   age = int(input("Enter your age: "))

print(f"You are {age} years old")
 
#-------------Example:3------------------
food=input("Enter food you like ! (q to quit):")
while not food=="q":
    print(f" ohh ! you  like {food}.")
    food=input("Enter another food you like (q to quit ):")
print("Thanks for your opinion!")

#-----------Example:4---------------------
num=int(input("Enter a number between 1 to 10:"))
while num>10 or num<1:
    print("Number you have enter is not valid!")
    num=int(input("Enter a number between 1 to 10:"))
print(f" Your number is {num}")

#------------Example :5--------------------
date_of_birth=int(input("Enter your date of birth:"))
while not (date_of_birth >= 1 and date_of_birth<=31):
    print("Date of birth you have entered is not valid !")
    date_of_birth=int(input("Enter your date of birth:"))
print(f"you are born on {date_of_birth}")

# GENERAL PATTERNS OF WHILE LOOPS
"There are 3 main patterns you will use again and again while using 'while loop'."

# Pattern 1 — VALIDATION WHILE LOOP

"""value = input("Enter something: ")
while value == "":        # condition for invalid input
    print("Invalid! Please try again.")
    value = input("Enter something: ")

print("You entered:", value)"""

"""Use when:
 You must *force correct input
 Keep asking until user enters valid data
Validation happens **before allowing code to continue**"""

### 5 Practice Problems (Validation Loop)

#1.Ask age, but allow only 1–120
"Keep asking until user enters a correct age."
age=int(input("Enter your age: "))
while not(age>=1 and age<=120):
    print("You have not entered a valid age!")
    age=int(input("Enter your age: "))
print(f"okay! You are {age} years old.")

#2. Ask for a positive number only
"Reject zero and negative numbers."
num=int(input("Enter a positive number: "))
while not(num>0):
    if num==0:
        print("You have entered Zero.")
    elif num<0:
        print("You have entered a negative number.")
    num=int(input("Enter a positive number only: "))
print(f"You have entered {num}")

#3. Ask for a password at least 6 characters
"If less than 6, ask again."
password=input("Enter your password: ")
while not(len(password)>=6):
    print("The password you have entered is not valid.")
    password=input("Enter your password again: ")
print("welcome!")

#4. Ask for a non-empty sentence
"User must enter something containing at least 1 non-space character."
sentence=input("Enter a  no-empty sentence: ")
while not any( ch.isalnum() for ch in sentence):
    print("YOU have entered a empty string.")
    sentence=input("Enter a  no-empty sentence: ")
print(f"Sentence you have Entered is '{sentence}.'")

#5. Ask for marks (0–100 only)
"If user enters marks outside this range, ask again."
marks=int(input("Enter your marks: "))
while not(marks>=0 and  marks<=100):
    print("You have not entered marks within the range 0-100.")
    marks=int(input("Enter your marks: "))
print(f"You have scored {marks}.")
     


# Pattern 2 — COUNTING LOOP (while loop that runs FIXED number of times)
"""i = 1
while i <= 10:            # loop runs a fixed number of times
    print("Count:", i)
    i += 1"""



"""Use when:
You know EXACT number of repetitions
Example: print table 10 times, run loop 5 times, count until N"""

#5 Practice Problems (Counting Loop)

#1.Print numbers 1 to 20 using while loop
i=1
while i<=20:
    print(i, end=" ")
    i+=1

#2.Print even numbers from 2 to 50
i=1
while i<=50:
    if i%2==0:
        print(i,end=" ")
    i+=1

#3.Take a number N → print its multiplication table up to 10
num=int(input("Enter a numbere: "))
i=1
while i<=10:
    print(f"{num}x{i}={num*i}")
    i+=1


#4.Print squares of numbers from 1–15
i=1
while i<=15:
    print(f"{i}²={pow(i,2)}")
    i+=1


#5. Ask user for 5 numbers and print their sum
"Loop runs **exactly 5 times**, not more / not less."
total=0
count=1
while count<=5:
    num=int(input("Enter a number:"))
    total+=num
    count+=1
print(f"Sum of the all number is :{total}")

#Pattern 3 — SENTINEL LOOP (run UNTIL condition met)
"""while True:               # infinite loop
    text = input("Enter something (type 'stop' to exit): ")
    if text.lower() == "stop":   # sentinel condition
        break
    print("You typed:", text)"""

"""Use when:
1. You do NOT know how many times loop will run
2.Loop ends only when a STOP value appears
3.Example: keep entering numbers until user enters 0"""

# 5 Practice Problems (Sentinel Loop):
#1. Keep taking numbers until user enters 0 → print sum of all
"Stop only when sentinel (`0`) arrives."
num=int(input("Enter a number:"))
total=0
while True:
    if num==0:
        break
    total+=num
    num=int(input("Enter a number again:  "))
print(f"Sum of the number you have entered is {total}")

    
#2. Keep taking input until user types “stop” (case insensitive)
text=input("Enter something: ")
while True:
    if text=="stop":
        break
    text=input("Enter something: ")
print("Okay!")

#3. Keep reading marks until user enters a negative number → print average
total=0
count=0
marks=int(input("Enter your marks: "))
while True:
    if marks<0:
        break
    total+=marks 
    count+=1
    marks=int(input("Enter your marks: "))
print(f"Average={total/count}")

#4. Keep asking for names until user enters “end” → print all names
name=input("Enter your name: ")
total=""
while True:
    if name=="end":
        break
    total+=name+" "
    name=input("Enter your name: ")
print(f"The names you have entered : {total}")

#5.Keep asking numbers until user enters number > 100
"As soon as number > 100 appears → stop."
num=int(input("Enter a number: "))
while True:
    if num>100:
        break
    num=int(input("Enter a number: "))

# chat gpt practice problems:
# Problem 1 (New): Username Without Spaces
"""Ask the user for a username.
Keep asking until they enter a username that does not contain spaces and is not empty.
Finally, print "Welcome, <username>!"."""
username = input("Enter your username: ")

while username == "" or " " in username:
    print("Username you have entered is not valid.")
    username = input("Enter your username: ")

print(f"Welcome {username}!")

# Problem 2 (New): Even Number Checker
"""Ask the user to enter a number.
Keep asking until they enter a valid even number (no text, no odd numbers).
When they finally do, print "Thank you! You entered an even number: X"."""
number=input("Enter a number:")
while not ( number.isdigit() and int(number)%2==0):
    print("Enter a valid even number.")
    number=input("Enter a number:")
print(f"Thankyou! you have entered a even number {int(number)}.")


# Problem 3: Only Y/N
"""Ask the user a yes/no question:
Do you want to continue? (y/n):
Keep asking until they enter only "y" or "n" (lowercase).
Print "Continuing..." if "y", "Exiting..." if "n"."""
validation=input("Do you wanna continue?(y/n):")
while not(validation=="y" or validation=="n"):
    print(f"{validation} is not vlid .")
    validation=input("Do you wanna continue?(y/n):")

if validation=="y":
        print("Continuing.....")
elif validation=="n":
        print("Exiting...")


# Problem 4: Password with Conditions
"""Ask for a password.
Keep asking until the password:
Is at least 8 characters long
Contains at least 1 digit
Contains at least 1 letter
When valid, print "Password accepted!"."""
password=input("Enter your password:")
while True:
     if len(password)<8:
          print("your password must contain at least 8 characters.")
     elif not any (ch.isdigit() for ch in password):
          print("your password must contain a digit.")
     elif not any (ch.isalpha()for ch in password ):
          print("your password must contain a letter.")
     else:
          break
     password=input("Enter your password:")
print("wellcome!")

# Problem 5: Sum of Positive Numbers
"""Ask the user for a number.
Keep asking until they enter 0.
Add up all the positive numbers they entered and print the total at the end.
Ignore negative numbers (but don't stop the program if they enter them — just don't add them)."""
total=0
num=int(input("Enter a number:"))
while num!=0:
     if num >0:
        total+= num

     num=int(input("Enter a number:"))
print(f"sum of the positive number you have entered:{total}.")

# Practice Problems 7 - Fix the Logic
"""Problem : Valid Color
Ask the user to enter a favorite color.
Keep asking until they type "red", "blue", or "green".
After getting a valid color, print You chose <color>!."""
color=input("Enter your favorite color:")
while not (color=="red"or color=="blue"or color=="green"):
     print(f"{color}  is not a valid color!")
     color=input("Enter your favorite color:")

print(f"You chose {color}!")
# Problem 8: Positive Number
"""Ask the user to enter a positive number.
Keep asking until the number is strictly greater than 0.
After that, print Thank you for entering <number>."""
number=int(input("Enter a positive number:"))
while number<=0:
     print(f"Number {number}is not a positive number.")
     number=int(input("Enter a positive number:"))
print(f"Positive number you have entered is {number}")

# Problem 4: Secret Word
"""There is a secret word "python".
Keep asking the user to guess until they type "python".
When they guess correctly, print Correct! You guessed the secret word."""
secret_word=input("Enter the secret word:")
while secret_word!="python":
     print(f"{secret_word} is not a secret word.")
     secret_word=input("Enter the secret word:")
print("Correct! you guessed the secret word.")

#excercise for while loop 
#compound interest calculator 
principle=0
rate=0
time =0
while True:
     principle=float(input("Enter the  principle amount:"))
     if principle<0:
          print("principle amount can't be neagative.")
     else:
          break
while True:
     rate=float(input("Enter interest rate :"))
     if rate <0:
          print("Interest rate can't be neagative.")
     else:
          break
while True:
     time=int(input("Enter time in years :"))
     if time <0:
          print("Time can't be neagative.")
     else:
          break
total=principle* pow(1+rate/100 , time)
print(f"Balance after {time} years  will be : ${total}.")

principle=0
rate=0
time=0
principle=float(input("Enter the principle amount: "))
while principle<=0:
    print("principle  amount cannot be less than or equal to zero !")
    principle=float(input("Enter the principle amount: "))
print(principle)
rate=float(input("Enter the  rate of increment: "))
while rate<=0:
    print("rate cannot be less than or equal to zero !")
    rate=float(input("Enter the  rate of increment: "))
print(rate)
time=int(input("Enter the time in years: "))
while time<=0:
    print("time  cannot be less than or equal to zero !")
    time=int(input("Enter the time in years: "))
print( time)

total=principle*pow(1+rate/100,time)
print(f"Total ammount you will get after {time} year is {total} ")

#while loop excersise 2 (while loop with logical operator)

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
while not (len(password)>8 and any(ch.isdigit() for ch in password)):
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
Repeat until valid.
10. Ask the user to type “yes” or “no”.
Accept uppercase or lowercase versions (YES, Yes, no, etc.) —
Use .lower() to simplify your condition."""
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
while not (len(password)>8 and password.isalnum() and any(ch.isupper() for ch in password)):
    print("Your password is invalid.")
    password=input("Enter your password again : ")
print("wellcome!")

#10
response=input("Enter your response (yes/no):")
while not ( response.lower()=="yes" or "no"):
    print("Response is not valid.")
    response=input("Enter your response again: ")
if response.lower()=="yes":
    print("Continueing....")
elif response.lower()=="no":
    print("Exiting....")



