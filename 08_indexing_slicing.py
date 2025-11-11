# indexing = accessing elements of a sequence using () (indexing operator)
#[start: end: step]
credit_number = "1234-5678-9012-3456"
print(credit_number[0])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1]) #6 
print(credit_number[::3])
print(credit_number[:6])
print(credit_number[3:6])
print(credit_number[::5]) # print every fifth element of the squence
print(credit_number[::8])
credit_number="1234-4321-5678-8765"
print(credit_number[4],",",credit_number[3],",",credit_number[0],"," , credit_number[10])
print(credit_number[-1])
print(credit_number[-4])
print(credit_number[:9])
print(credit_number[:4])
print(credit_number[5:14])
print(credit_number[15:])
print(credit_number[::3])
print(credit_number[::-1])
print(credit_number[::-2])

#exercise
credit_number = "1234-5678-9012-3456"
last_digit=credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digit}")
print(credit_number[::-1])

# chat gpt practice problems on indexing:

## 📝 Practice Problems on Indexing

# Problem 1: First and Last Character
"""* Ask the user to enter a string.
* Print the **first character** and the **last character** using indexing"""
text=input("Enter a text:")
print(text[0],text[-1])

# Problem 2: Middle Character
"""* Ask the user for a word.
* If the length is odd → print the middle character.
* If even → print `"No exact middle"`."""
word=input("Enter a word:")
if len(word)%2 !=0 :
    middle_word=len(word)//2
    print(word[middle_word])
else:
    print("no exact middle.")

# Problem 3: Reverse a String
"""* Ask the user for a string.
* Print the string in reverse order using **slicing** (`[::-1]`)."""
text=input("Enter a text:")
print(text[::-1])


# Problem 4: Username Extractor
"""* Ask the user for their email (like `"john123@gmail.com"`).
* Print only the **username** part (before `@`)."""
email=input("Enter your email:")
userpart_index=email.find("@")
print(email[:userpart_index])

# Problem 5: Secret Code (Indexing Game)
"""* Ask the user for a word.
* Print a new string made of:
  * 1st character
  * 3rd character
  * last character
* Example: `"python"` → `"ptn"`"""
word=input("Enter a word:")
secret_code=word[0]+word[2]+word[-1]
print(secret_code)

# Problem 6: Replace Middle with 
"""* Ask the user for a word.
* Replace the middle character with `*` and print it.
* Example: `"hello"` → `"he*lo"`"""
word=input("Enter a word:")
middle_index=len(word)//2
middle_word=word[middle_index]
word=word[:middle_index] + "$" + word[middle_index+1:]
print(word)

# Problem 7: Index Finder**
"""* Ask the user for a string and a character.
* Print the index of the first occurrence of that character (using `.find()` or by manually looping with indexing)."""
string=input("Enter string:")
character=input("Enter a character:")
print(string.find(character))

# email slicer
email=input("Enter your email:")
index=email.find("@")
username=email[:index]
domain=email[index+1:]
print(f"Your username name is {username} and the domain is {domain}.")





