#String formating :
# 1. STRING CONCATENATION  (+)
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

#3. PERCENTAGE FORMATTING(%)
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

words = ["I", "love", "Python"]
print(" ".join(words))

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




#STRING METHOD

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
