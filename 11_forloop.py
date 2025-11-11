#For loop  = execute a block of code a fixed number of times.
#        You can iterate over a range, string, sequence, etc.
#excercise:
# eg:1
for x in  range(1,11):
     print(x)
print("Done") #just to know that we escape out of the for loop and the block code has executed specific number of time.

#eg:2
for x in reversed(range(1,11)):
     print(x)

print("Done")
#eg:3
for x in range(1,11,2):
     print(x)
print("Done")

#eg:4
credit_card = "1234-5678-9012-3456"
for x in credit_card:
     print(x)
print("Done")

for x in credit_card[::3]:
     print(x)
print("done")
#eg:5
for x in (1,11):
     if x==13:
          continue
     else:
          print(x)

#eg:6
for x in (1,11):
     if x==13:
          break
     else:
          print(x)

#chat gpt practice problem for "For loop ":
# Problem 1: Print Squares
"""Ask the user for a number n.
Use a for loop to print the square of every number from 1 to n."""
n=int(input("Enter a number:"))
for x in range(1,n+1):
    square=x**2
    print(f"{x}²= {square} ")

# Problem 2: Sum of First N Numbers
"""Ask the user for a number n.
Use a for loop to calculate the sum of all numbers from 1 to n."""
total=0
n=int(input("Enter a number:"))
for x in range(1, n+1):
    total+=x
print(f"sum of all the number from 1 to {n}  is {total}")

# Problem 3: Even Numbers
"""Ask the user for a number n.
Print all even numbers from 1 to n."""
n=int(input("Enter a number:"))
for x in range(1 , n+1):
    if x%2==0:
        print(x)

# ''Problem 4: Factorial
"""Ask the user for a number n.
Use a for loop to calculate its factorial (n!)."""
n=int(input("Enter a number:"))
total=1
for x in   range(1,n+1):
    total*=x
print(f"{n}!={total}")
    
# Problem 5: Multiplication Table
"""Ask the user for a number n.
Print its multiplication table up to 10."""
n=int(input("Enter a number:"))
for x in range(1,11):
    result=n*x
    print(f"{n}x{x}={result}")

# """Problem 6: Count Vowels
"""Ask the user for a word.
Use a for loop to count how many vowels (a, e, i, o, u) it has.
Example: "hello" → 2 vowels."""
word=input("Enter a word :")
vowel=["a","e","i","o","u"]

count=0
for x in vowel:
    count+=word.count(x)
    
print(f"Your word  {word} have {count} vowels.")



# Problem 7: Reverse a String
"""Ask the user for a word.
Use a for loop to print it in reverse order.
(Hint: you can use range(len(word)-1, -1, -1)"""
word =input("Enter a word:")
reverse_word=""
for x in reversed(word):
    reverse_word+=x
print(f"Reversed word:{reverse_word}")



# Problem 8: Count Positives & Negatives
"""Ask the user how many numbers they want to enter.
Use a for loop to take input that many times.
Count how many were positive and how many were negative, then print the result."""
num=int(input("Enter how many numbers you want enter:"))
positive_num=0
negative_num=0
for x in num:
    num=int(input("Enter a number:"))
    if num>0:
        positive_num+=n


#chat gpt practice problem for "For loop ":
# Problem 1: Print Squares
"""Ask the user for a number n.
Use a for loop to print the square of every number from 1 to n."""
n=int(input("Enter a number:"))
for x in range(1,n+1):
    square=x**2
    print(f"{x}²= {square} ")

# Problem 2: Sum of First N Numbers
"""Ask the user for a number n.
Use a for loop to calculate the sum of all numbers from 1 to n."""
total=0
n=int(input("Enter a number:"))
for x in range(1, n+1):
    total+=x
print(f"sum of all the number from 1 to {n}  is {total}")

# Problem 3: Even Numbers
"""Ask the user for a number n.
Print all even numbers from 1 to n."""
n=int(input("Enter a number:"))
for x in range(1 , n+1):
    if x%2==0:
        print(x)

# ''Problem 4: Factorial
"""Ask the user for a number n.
Use a for loop to calculate its factorial (n!)."""
n=int(input("Enter a number:"))
total=1
for x in   range(1,n+1):
    total*=x
print(f"{n}!={total}")
    
# Problem 5: Multiplication Table
"""Ask the user for a number n.
Print its multiplication table up to 10."""
n=int(input("Enter a number:"))
for x in range(1,11):
    result=n*x
    print(f"{n}x{x}={result}")

# """Problem 6: Count Vowels
"""Ask the user for a word.
Use a for loop to count how many vowels (a, e, i, o, u) it has.
Example: "hello" → 2 vowels."""
word=input("Enter a word :")
vowel=["a","e","i","o","u"]

count=0
for x in vowel:
    count+=word.count(x)
    
print(f"Your word  {word} have {count} vowels.")



# Problem 7: Reverse a String
"""Ask the user for a word.
Use a for loop to print it in reverse order.
(Hint: you can use range(len(word)-1, -1, -1)"""
word =input("Enter a word:")
reverse_word=""
for x in reversed(word):
    reverse_word+=x
print(f"Reversed word:{reverse_word}")



# Problem 8: Count Positives & Negatives
"""Ask the user how many numbers they want to enter.
Use a for loop to take input that many times.
Count how many were positive and how many were negative, then print the result."""
n=int(input("Enter how many numbers you want enter:"))
positive_num=0
negative_num=0
for x in range(n):
    num=int(input(f"Enter the number{x+1}:"))
    if num>0:
        positive_num+=1
    elif num<0:
        negative_num-=1
print(f"Number og positive number and negative number you have entered is {positive_num} and {negative_num} respectively.")
    

# Problem 9: Character Search
"""Ask the user for a word and a character to search.
Use a for loop to check how many times the character appears in the word.
Print the count."""
word=input("Enter a word:")
character=input("Enter  a character you wanna search in word:")
count_char=0
for c in word:
    if c==character:
        count_char+=1
print(f"The character {character} is repeated {count_char} times in  word .")
# Problem 10: Sum of Digits
"""Ask the user for a number.
Use a for loop (or convert to string) to calculate the sum of its digits.
Example: 1234 → 1+2+3+4 = 10"""
digit=input("Enter a number ")
total=0
for x in digit:
    total+=int(x)
print(f"Sum of digit of the number {digit} is {total}")
