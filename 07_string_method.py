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
