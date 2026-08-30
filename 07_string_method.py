#String formating :
# 1. STRING CONCATENATION  (+):
"Example:"
greet="Hello"
name="echii"
result= greet+","+" "+"i am"+" "+name
print(result)

#PRACTICE PROBLEM 
#1. Ask user for first name and last name → print full name using "+".
first_name="echii"
last_name="universe"
result=first_name+" "+last_name
print(result)

#2.Take two strings "Python" and "Rocks" → print Python-Rocks using "+".
a="Python"
b="Rock"
result=a+"-"+b
print(result)

#3.Ask user for a word and repeat it 3 times using only "+" (no *).
word=input("Enter a word: ")
result=word+" "+word+" "+word
print(result)

#4.Create a sentence: "My age is " and user's age (converted to string) → concatenate.
name="Echii"
age=18
result="My name is "+name+"."+"I am "+str(age)+" "+"years old."
print(result)

#5.Input two numbers → print "Sum is X" using concatenation.
first_num=int(input("Enter first number: "))
second_num=int(input("Enter second number: "))
sum= first_num+second_num
result="Sum is "+ str(sum)
print(result)

#2..format() METHOD.
"Example:"
print("i am {}! i am {} years old.".format("echii",18))

# PRACTICE PROBLEM 
# 1.Ask user for two numbers → print "{} + {} = {}" using .format().
first_num=int(input("Enter first number: "))
second_num=int(input("Enter second number: "))
sum=first_num+second_num
print("{}+{}={}".format(first_num,second_num,sum))

#2.Format output:
"Roll: 21, Name: John"
print("Roll:{},Name:{}".format(21,"John"))

#3.Ask temperature → print "Today's temperature is {}°C".
tem=input("Enter temperature in celcium: ")
print("Today's temperature is {}°C".format(tem))

#4.Print a table row like: "Item: {}, Price: {} Rs".
item=input("Enter the item's name: ")
price=input("Enter the item's price: ")
print("Item: {0},price:{1} Rs.".format(item, price))

#5.Use keyword arguments:
result="Name: {n}, Age: {a}".format(n="Sam", a=20)
print(result)
print("i like {a}. i want {b} {a}.".format(a="pizza",b=2))

#3. PERCENTAGE FORMATTING(%):
"Examples:"
name="echii"
age=18
print("My name is %s.I am %d years old."%(name, age))

#PRACTICE PROBLEMS
#1.Print "X + Y = Z" using %d.
first_num=int(input("Enter first number: "))
second_num=int(input("Enter second number: "))
sum=first_num+second_num
print("%d+%d=%d"%(first_num,second_num,sum))

#2.Print "Name: ___" using %s.
print("Name: %s."%("echii"))

#3.Print floating number with 2 decimals using %0.2f.
print("%.2f"%(2.434))
num1=float(input("Enter a number: "))
num2=float(input("Enter a number: "))
sum=num1+num2
print("%.2f+%.2f=%.2f"%(num1,num2,sum))

#4.Ask user for marks → print "Percentage: %.2f".
marks=float(input("Enter a marks: "))
total=float(input("Enter  the total marks: "))
percentage=marks/total*100
print("You have scored %.2f  marks out of %.2f so your percentage is %.2f ." %(marks, total ,percentage))

#5.Display: "Item: %s, Quantity: %d".
print("Item: %s, Quantity: %d"%("Pizza",3))

#4. " ".join(list/string):
"examples:"
words = ["I", "love", "Python"]
print(" ".join(words))
r=["miow","miow","miow","...."]
print(" ".join(r))
a="MIOW"
print("-".join(a))


# 1.Ask user for 3 words → store in list → join with space.
word1=input("Enter word1: ")
word2=input("Enter word2: ")
word3=input("Enter word3: ")
words=[word1,word2,word3]
print(" ".join(words))

# 2.Join digits ["1","2","3","4"] into "1234".
digits = ["1", "2", "3", "4"]
result = "".join(digits)
print(result)

# 3.Join words with comma: "a,b,c,d".
words = ["a", "b", "c", "d"]
result = ",".join(words)
print(result)

# 4.Join characters of a string into "H-E-L-L-O".
text = "HELLO"
result = "-".join(text)
print(result)

# 5.Input a sentence → split into words → join using " | ".
sentence = input("Enter a sentence: ")
words = sentence.split()        # splits by spaces
result = " | ".join(words)
print(result)

#5.f-string METHOD:
"Example:"
name="Echii"
age=17
print(f"Hi! i am {name}.i am {age} years old.")

#PRACTICE PROBLEMS:
#1.Ask user’s name & city → print "Name: ___, City: ___" using f-string.
name=input("Enter your name: ")
city=input("Provide me with  your city name: ")
print(f"Name: {name}, City:{city}")

#2.Input a number → print Square: ___ using f-string.
num=int(input("Enter a number: "))
result=pow(num,2)
print(f"Square: {result}")

# 3.Format output as:
"Value: 10, Double: 20, Triple: 30"
num=int(input("Enter a number:"))
double_num=2*num
triple_num=3*num
print(f"Value: {num}, Double: {double_num}, Triple: {triple_num} ")

#4.Ask for 3 marks → print total and percentage using f-string.
eng_marks=int(input("Enter how much marks you scored in English: "))
maths_marks=int(input("Enter how much marks you scored in Mathematics: "))
sci_marks=int(input("Enter how much marks you scored in Science: "))
total=int(input("Enter the total marks : "))
marks_scored=eng_marks+maths_marks+sci_marks
percentage=marks_scored/total*100
print(f"Your scored {percentage}% in your exam.")


#STRING METHOD  [function  we can use for string]

greet="hello world"
phone_number="78-456-432"
 #length function : for checking the length of a variable it counts the number of character in  variable .
print(len(greet))

#find function : use to find a specific character of the string
print(greet.find("r"))
print(greet.find("o"))
print(greet.rfind("o")) # find the last occurance of the character 
print(greet.find("f")) # a character which is not in the given string then this function will print -1
print(greet.find("e"))

# For changing the case of the  variable 
print(greet.upper())
print(greet.lower())
print(greet.capitalize())

# isdigit function: we use it to check whether a variable's character is all digit or not 
#  it return value in boolean(return true when all the character(also the if there's no space ) of the variable is ONLY digit).
print(greet.isdigit())
print(phone_number.isdigit())

#isalpha function : use to check whether all the charater of a variable is ONLY STRINGS or not 
# it returns boolean output (returns true if all the chracter is ONLY string and there is no space only string character)

print(greet.isalpha())
#count function:  for counting  a specific charater of the variable 
print(greet.count("o"))
print(greet.count(" "))
print(greet.count("h"))
#replace function: replace a  specific chracter of the variable but for that you need to create or restore that variable again.
greet=greet.replace("hello","hey")
print(greet)
phone_number=phone_number.replace("-"," ")
print(phone_number)

greeting="  Hello world   "
greeting.strip() #remove uneccessary spaces from both end of the string   , will print:"Hello world"
print(greeting)
greeting.lstrip() #remove spaces from left  , will print:"Hello world  "
greeting.rstrip() #remove spaces from right  will print : "  Hello world"
greeting.title() # will print : "Hello World"
greeting.swapcase() # will print : "hELLO wORLD"
#.endwith(x)/.startwith(x) :use to check the file type  eg:
"To check proper website ,document type etc"
website="https://www.youtube.com/"
print(website.endswith(".com/")) #True
print(website.startswith("https://")) #True
password="123miowmiowABC"
print(password.endswith("ABC"))# True
print(password.startswith("123")) #True
print(password.endswith("3434"))#False
print(password.startswith('ade') )#False
#islower() and isupper() : to check the case of  letter 
a="MIOW"
b="bow"
print(a.isupper()) #True
print(a.islower()) #False
print(b.isupper()) #False
print(b.islower()) #True
#isspace() : wheck whether the whole string  contain only spaces or not 
"   ".isspace()   # True
"".isspace()      # False — empty string is NOT considered "all whitespace"
" a ".isspace()   # False — has a non-space character
#zfill(n) : Pads a string with leading zeros until it reaches length n.
print("7".zfill(3))
print("67".zfill(4))


#help function :
# print(help(str)) # tell us in DETAIL about each mthod we can use for the string 
# print(dir(str)) # list all the method we can use on string simplarly we can do for other data type.
# print(help(len(greet))) 
#overall method learned:
name=input("Enter your name: ")
letter=input("Enter a letter you wanna find: ")
print(name.find(letter))
print(name.rfind(letter))
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.count(letter))
print(name.replace(letter,"o"))
 # excercise
 #validate user input 
 # username must only contain 12  character
 # there should be no spaces 
 #there must be no digit 
username=input("Enter a username:")
if len(username)<12 or len(username)>12:
    print("Your user name must contain 12 character.")
elif  not username.find(" ")==-1:
    print("Your username should not contain any spaces!.")
elif any( ch.isdigit() for ch in username):
    print("Your username must only contain alphabates.")
else:
    print(f"Wellocome {username}!")

#chat gpt practice problem:
# practice problem 1: Name Formatter
"""Ask the user for their full name in lowercase.
Print it back with the first letter capitalized (use .capitalize())."""
name=input("Enter your name in lowercase:")
print(name.capitalize())

# practice problem 2:Word Counter
"""Ask the user to enter a sentence.
Ask the user for a word to search.
Print how many times the word appears in the sentence (use .count())."""

sentence=input("Enter a sentence:")
word=input("Enter a word which you wanna seach in your sentence:")
print(sentence.count(word))

#practice problem 3:Password Validator
"""Ask the user to enter a password.
Check:
At least 8 characters long (len)
Contains only letters and digits (isalnum())
Has at least one digit (isdigit() inside a loop or trick)
Print "Valid password" or "Invalid password"."""
password=input("Enter the password: ")
if len(password)<8:
    print("Your password must contain atleast 8  character.")
elif not password.isalnum():
    print("Your password must contain alphabates and number")
elif not any(ch.isdigit() for ch in password):
    print("Your password must contain a digit.")
else:
    print("Valid password!")


#1. bais combo 
name=input("Enter your name: ")
salary=int(input("Enter the salary: "))
annual_income=salary*12
print(f"{name} earn ${salary:,.2f} a month.That's make upto {annual_income:,.2f}")
# 2. List + string methods
"""Take a sentence as input. Split it into words, then print each word capitalized, one per line, along with its length. 
Example: for "the quick fox", print something like The - 3 letters."""
sentence=input("Enter a sentence: ")
sentence=sentence.title()
words=sentence.split()
for word in words:
    print(f"{word}→{len(word)}letters.")

"""3. Set operations
You have two lists of student names who attended Monday's class and Tuesday's class. 
Using sets, find: students who attended both days, students who attended only Monday,
 and students who attended either day but not both."""
mon_lec=["ria","sia","zack","hennah"]
tue_lec=["tia","ria","hennah","biu","joe","tac"]
a=set(mon_lec)
b=set(tue_lec)
print(f"""==========Student Attendance==========
Student who attended both day    :{a.intersection(b)}
Student who attended only monday :{a.difference(b)}
Student who attended attended either but not both :{a.symmetric_difference(b)}""")

"""4. Nested loop + condition — no string multiplication
Print a diamond pattern (pyramid + upside-down pyramid combined) for a given number of rows, 
without using * string multiplication (i.e., use loops for spaces and stars, like your earlier pyramid)."""
row=5
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("-",end="")
    print()
for i in reversed(range(1,row+1)):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("-",end="")
    print()

"""5. While loop + logical operators
Write a simple number-guessing game: pick a fixed secret number, let the user keep guessing with input() 
in a while loop, and print "Too high", "Too low", or "Correct!" each time, stopping the loop when they get it right. 
Also count and print how many attempts it took."""
num =int(input("Enter the number: "))
i=1
while num!=7:
    if 8<= num <=10:
        print("close!")
    elif 11<= num <=20:
        print("High!")
    elif num>20:
        print("too high!")
    elif 6<= num >=5:
        print("close!")
    elif 5> num >=1:
        print("low!")
    elif num<1:
        print("too low!")

    num=int(input("Enter the number: "))
    i+=1
print(f"The attempt u took the guess correct is {i}")

"""6. Tuple + indexing/slicing
Given a tuple of 10 numbers, print: the first 3 numbers, the last 3 numbers,
 every 2nd number, and the tuple reversed — all using slicing (no loops)."""
a=(5,15,25,35,45,55,65,75,85,95)
print(a[:3])
print(a[-3:])
print(a[::2])
print(a[::-1])

"""7. Combine everything — FizzBuzz variant
Loop from 1 to 50. For multiples of 3, print "Fizz"; multiples of 5, 
print "Buzz"; multiples of both, print "FizzBuzz"; otherwise print the number. Then, 
separately, store all the "FizzBuzz" numbers in a list and print that list at the end."""
fizzbuzz_no=[]
for i in range(1,51):
    if i%3==0 and i%5==0:
        print(f"{i}→FizzBuzz",end=", ")
        fizzbuzz_no.append(i)
    elif i%5==0:
        print(f"{i}→Buzz",end=", ")
    elif i%3==0 :
        print(f"{i}→Fizz",end=", ")
        

print(f"FizzBuzz Numbers are :{fizzbuzz_no}")
