#DICTIONARY
"""dictionary =  a collection of {key:value} pairs
   ordered and changeable. No duplicates"""
dictionary={"key":"value"}

#THREE WAYS OF CREATING A DICTIONARY:
"Normal way:"
info={"name":"miow",
      "age":"2"}
print(info)
"Empty dictionary:"
d={}
"Using dict():"
dic=dict(name="miow",age=2)
print(dic)

#DIFFERENT METHOD OF DICTIONARY:
capitals={"India":"New Delhi",
          "Usa":"Washington D.C.",
          "China":"Beijing",
          "Russia":"Moscow"}

"1. get() → Safe value access (Prevents crash if key doesn't exist)"
print(capitals.get("China"))
print(capitals.get("china")) #None (because China exits in list not china )
print(capitals.get("Usa"))
print(capitals.get("India"))
print(capitals.get("Japan")) #None (since Japan doen't exits in dictionary)

"2. keys() → Get all keys"
print(capitals.keys())
for keys in capitals.keys():
    print(keys)

"3. values() → Get all values"
print(capitals.values())
for values in capitals.values():
    print(values)

"4. items() → Get (key, value) pairs:"
print(capitals.items())
for x,y in capitals.items():
    print(f"{x:<2} → {y:<2}")

"5. update() → Add or modify multiple items:"
(capitals.update({"Germany":"Berlin"}))
capitals.update({"India":"Mumbai"})
print(capitals)

"6. pop() → Remove by key:"
capitals.pop("Germany")
print(capitals)

"7. popitem() → Remove last inserted item:"
capitals.popitem()
print(capitals)

"8. copy() → Duplicate dictionary:"
new_capital=capitals.copy()
print(new_capital)

"9. setdefault() → Set if key not exists:"
capitals.setdefault("Germany","Berlin")
print(capitals)

"10.clear()→ Delete everything"
capitals.clear()
print(capitals)

#ADD/UPDATE/DELETE
d = {"a": 10, "b": 20}
d["c"] = 30
d["a"] = 100
del d["b"]
print(d)

#PRACTICE PROBLEMS


# 1.Create a dictionary with 5 student names and marks.
student_info={"Rahul":"56",
              "Riya":"67",
              "kiki":"87",
              "Anita":"78"}
for students,marks in student_info.items():
    print(f"{students:<2}  → {marks:<2}")

info={"ruchi":"echii@gmail.com",
      "Kartikey":"kartikey@gmail.com",
      "tac":"tac@gmail.com"}

print(f"{"Student":^5}   {"Email":^20}")
for name,emails in info.items():
    print(f"{name:<5} → {emails:>20}")

# 2.Print only the keys.

for keys in student_info.keys():
    print(keys)

# 3.Print only the values.
for values in student_info.values():
    print(values)

# 4.Update a student’s marks.
student_info.update({"Rahul":"78"})
print(student_info)

# 5.Check if a key exists in a dictionary.
key=input("Enter what you wanna search in the dictionary: ")
if student_info.get("miow"):
    print("Exits")
else:
    print("Doesn't exits.")

# 6.Count frequency of each character in a string.
s=input("Enter a word: ")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

"Alternate Method"
s=input("Enter a word: ")
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)

# 7. Count frequency of words in a sentence.
sentence=input("Enter a sentence: ")
words=sentence.split()
freq={}
for word in  words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print(freq)

# 8.Merge two dictionaries.
a={"Dev":"23","Ruhi":"19"}
b={"sid":"20","Piya":"21"}
a.update(b)
print(a)
print("{:<5}  {:<5}".format("Name","Age"))
for x,y in a.items():
    print(f"{x:<5} → {y:<5}")

# 9.Find the key with maximum value.
d={"a":"12","b":"16","c":"23"}
x= max(d,key=d.get)
print(f"Key with maximum value:{x}.")

# 10.Delete all keys with value = 0.
d={"a":"12","b":"16","c":"23","d":"0"}
for key in list(d.keys()):
    if d[key]=="0":
        del d[key]

print(d)

#COMPREHENSION exercise

# 1.Create {1:1, 2:4, 3:9, ..., 10:100} using comprehension.
d={i:i*i for i in range(1,10) }
print(d)

# 2.convert a list of words into dictionary → key=word, value=length.
l=["miow","bow"]
d={k:len(k) for k in l}
print(d)

# 3.Convert a string into a dictionary counting each character.
string=input("Enter a word: ")
d={k:string.count(k)for k in string}
print(d)

# 4.Reverse key–value pairs in a dictionary.
d = {"a": 1, "b": 2, "c": 3}
reversed_dic={value:key for key,value in d.items()}
print(reversed_dic)

# 5.Filter out all items where value is less than 50.
scores = {"A": 80, "B": 45, "C": 30, "D": 95}
filtered_score={k:v for k  , v in scores.items()if v<50}
print(filtered_score)
#score where value is greater than 50
new_score={k:v for k,v in scores.items()if v>50}
print(new_score)

# 6.Convert two lists into a dictionary using comprehension.
a=[1,2,3]
b=[4,5,6]
d={k:v for k,v in zip(a,b)}
print(d)

# 7.Given: {"a":2,"b":5,"c":10} → make a dict where each value is squared.
d={"a":2,"b":5,"c":10}
new_d={k:v**2 for k , v in d.items()}
print(new_d)

# 8.Make a dictionary of vowels and their count in a string.
word=input("Enter a word: ")
vowel="aeiou"
d={v:word.count(v) for v in vowel if v in word }
print(d)

# 9.Create a dictionary where keys = words and values = frequency of words.
fruit=["apple","banna","mango","apple","mango","orange"]
d={v:fruit.count(v) for v in fruit}
print(d)

# 10.Given a 2D list of student marks, create a dictionary of student name → total marks.
l_2d=[["Riya",25,45],
      ["Sid",24,26],
      ["kira",20,35]]

d={v[0]:sum(v[1:] )for v in l_2d}
print(d)

# exercise:2
# 1 Create a dictionary from 1 to 20 where key = number, value = “even” or “odd”.
d={v:("even"if v%2==0 else "odd") for v in range(1,21) }
print(d)

# 2 Convert a list of tuples into a dictionary. Example: [("a",1),("b",2),("c",3)]
list_of_tuple=[("a",10),("b",20),("c",30)]
d={v[0]:v[1] for v in list_of_tuple}
print(d)

# 3 Given a dictionary of salaries, increase each salary by 10%.
d={"worker1":1000,"worker2":3000,"worker3":4000}
new_d={k:int(v+v*10/100) for k ,v in d.items()}
print(new_d)

# 4 Create a dictionary of word → length for a word in full sentence.
sentence=input("Enter a sentence: ")
words=sentence.split()
d={word:len(word) for word in words}
print(d)

# 5 From a dictionary of marks, filter out all students who scored 80 or above.
d={"Riya":89,"Ruhi":78,"komal":92,"Tripti":79}
new_d={k:v for k ,v in d.items()if v>=80}
print(new_d)

# 6 Given a list of numbers, create a dictionary where key = number and value = number of digits.
l=[1,34,345,5666,20000]
d={v:len(str(v))for v in l}
print(d)

#7. Convert Celsius values in a list to Fahrenheit using comprehension.
tem=(30,40,70,80)
new_tem={v:int((v*9/5)+32) for v in tem}
print(new_tem)

#8. Given a dictionary of name → age, create a dictionary of only adults (age ≥ 18).
details={"Riya":34,"sid":24,"Ruchi":18,"tripti":8}
new_details={k:v for k,v in details.items()if v>=18}
print(new_details)

#9. Count how many times each vowel appears in a full sentence.
sentence=input("Enter a sentence:")
vowel="aeiou"
d={v:sentence.count(v) for v in vowel if v in sentence}
print(d)

#10. From a list of names, create a dictionary of name → first letter.
l=["Ruchi","Piya","Komal"]
d={v:v[0] for v in l}
print(d)

# -------- LEVEL 2 — HARD --------

# 11 Reverse a dictionary but if multiple keys have same value, group them into lists.
#    Example: {"a":1,"b":2,"c":1} → {1:["a","c"],2:["b"]}
d={"a":1,"b":2,"c":1,"d":4,"c":2}
new_d={}
for k,v in d.items():
    new_d.setdefault(v,[]).append(k)
print(new_d)
    
#12. Extract only items where both key and value are even numbers.
d={2:4,3:4,4:6}
new_d={k:v for k,v in d.items()if k%2==0 and v%2==0}
print(new_d)

# 13 Create a dictionary mapping each word → frequency, ignoring case & punctuation.
sentense="SHE ,SHE and she  is Happy!"
sentense=sentense.lower()
sentense=sentense.replace("!","")
sentense=sentense.replace(",","")
words=sentense.split()
d={word:sentense.count(word) for word in words}
print(d)

# 14 Given a dictionary of populations, find the top 3 largest using comprehension + sorting.
d={"India":144,"USA":33,"China":140,"Russia":100}
sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
new_d=dict(sorted_items[:3])
print(new_d)

# 15 Create a dictionary where key = number (1–20), value = number of divisors.
d={n:sum(1 for i in range(1,n+1)if n%i==0)for n in range(1,20)}
print(d)

# 16 Create dictionary of character → ASCII value but only for alphabets.
import string
d={ch:ord(ch) for ch in string.ascii_letters}
print(d)

# 17 From a list of numbers, create {"even":[...], "odd":[...]}.
n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
d={"even":[i for i in n if i%2==0],
   "odd":[i for i in n if i%2!=0]}
print(d)

# 18 Convert a nested list into a dictionary of index → list_sum.
#    Example: [[1,2,3],[4,5,6],[7,8]] → {0:6,1:15,2:15}
l=[[2,3],[4,1,5],[3,4,2,6]]
d={l.index(i):sum(l[l.index(i)]) for i in l}
print(d)

# 19 Given a list of strings, create dictionary → string : number of vowels.
words=["hello","miow","bow"]
vowel="aeiou"
d={word:sum(1 for ch in word if ch in vowel) for word in words }
print(d)
# 20 Invert a dictionary but ensure the result is sorted by keys.
d = {"a": 3, "b": 1, "c": 2}
d_1={v:k for k,v in d.items()}
new_d=dict(sorted((d_1.items())))
print(new_d)

#USING setdefault() FUNCTIONS 
l=["dog", "cat", "deer", "cow", "duck"]
d={}
for word in l:
    first_letter=word[0]
    d.setdefault(first_letter,[]).append(word)
print(d)
numbers = [3, 8, 15, 22, 7, 4, 19, 6]
d={}
for num in numbers:
    key="Even"if num%2==0 else "Odd"
    d.setdefault(key,[]).append(num)
print(d)

items = [('fruit', 'apple'), ('veg', 'carrot'), ('fruit', 'banana'), ('dairy', 'milk'), ('fruit', 'mango')]
d={}
for category,item in items:
    d.setdefault(category,[]).append(item)
print(d)

enrollments = [('Math', 'Ria'), ('Science', 'Sam'), ('Math', 'Sam'), ('Math', 'Ria'), ('Science', 'Tia')]
info={}
for course ,student in enrollments:
    info.setdefault(course,set()).add(student)
print(info)

sales = [('Jan', 'apple', 10), ('Jan', 'banana', 5), ('Feb', 'apple', 8), ('Jan', 'apple', 3)]
data={}
for month,fruit,qty in sales:
    data.setdefault(month,{}).setdefault(fruit,0)
    data[month][fruit]+=qty
print(data)

words = ["cat", "dog", "tree", "sun", "moon", "ant", "star"]
d={}
for word in words:
    key=len(word)
    d.setdefault(key,[]).append(word)
print(d)

items = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "apple"), ("fruit", "mango"), ("veg", "carrot")]
a={}
for  category ,item in items:
    a.setdefault(category,set()).add(item)
print(a)

attempts = [("Ria", 45), ("Sam", 78), ("Ria", 60), ("Sam", 85), ("Ria", 55)]
info={}

for name ,marks in attempts:
    info.setdefault(name,[]).append(marks)
for name in info:
    info[name].sort()
    
print(info)

words = ["listen", "silent", "enlist", "banana", "cat", "act", "tac"]
d={}
for word in words:
    key="".join(sorted(word))
    d.setdefault(key,[]).append(word)
print(d)

contacts = [("Ria", "9990001"), ("Sam", "8887772"), ("Ria", "9990009"), ("Tia", "7776663")]
info={}
for name,number in contacts:
    info.setdefault(name,[]).append(number)
print(info)

records = [("10A", "Ria", "A"), ("10B", "Sam", "B"), ("10A", "Tia", "A"), ("10A", "Om", "B"), ("10B", "Zoe", "A")]
info={}
for classs ,name , grade in records:
    info.setdefault(classs,{}).setdefault(grade,[]).append(name)
print(info)

n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a={}
for i in  n :
    key="Even" if i%2==0 else "Odd"
    a.setdefault(key,[]).append(i)
print(a)
"""1. Counter basics
Given text = "to be or not to be that is the question",
 use Counter to find how many times each word appears,
   then print only the top 3 most common words."""


from collections import Counter

text = "to be or not to be that is the question"
count=Counter(text)
print(count)
print(type(count))
print(count.most_common(1))
print(count.most_common(2))
print(count.most_common(3))
"""2. Counter with strings directly
Given word = "mississippi", use Counter directly on the 
string (not split into words) to count how many times each letter appears.
 Then print the single most common letter."""

from collections import Counter

word = "mississippi"
repetation=Counter(word)
print(repetation)
print(repetation.most_common(1))

"""3. defaultdict grouping — by vowel count
Given words = ["cat", "elephant", "sky", "orange", "gym", "umbrella"], 
use defaultdict(list) to group words by how many vowels they contain (0, 1, 2, 3...)."""
from collections import defaultdict 
words = ["cat", "elephant", "sky", "orange", "gym", "umbrella"]
a=defaultdict(list)
vowels="aeiou"
for word in words:
    count=sum(1 for l in word if l in vowels)
    a[count].append(word)
print(dict(a))

"""4. defaultdict with int — a counting alternative defaultdict isn't just for lists — 
it works with int too (defaulting to 0 instead of []). 
Given text = "red blue red green blue red yellow", use defaultdict(int) to count color frequency 
without using Counter this time (to prove you understand what defaultdict(int) 
does differently from defaultdict(list))."""
text = "red blue red green blue red yellow"
colors=text.split()
a=defaultdict(int)
for color in colors:
    a[color]+=1
print(a)

"""5. Counter arithmetic — a neat trick
Counter objects can be added together with +.
 Given cart1 = Counter(["apple", "banana", "apple"]) 
and cart2 = Counter(["banana", "banana", "mango"]),
 add them together and print the combined counts. (Try predicting the output before running it.)"""
cart1 = Counter(["apple", "banana", "apple"])
cart2 = Counter(["banana", "banana", "mango"])
print(cart1+cart2)

"""6. Combine both — most frequent first letter, grouped
Given names = ["Ravi", "Rina", "Sam", "Sara", "Tia", "Ravi", "Sam"],
 first use defaultdict(list) to group the original name list (not unique) by first letter. 
 Then, separately, use Counter to find which first letter appears most often across all names."""
names = ["Ravi", "Rina", "Sam", "Sara", "Tia", "Ravi", "Sam"]
name=defaultdict(list) 
for i in names :
    first_letter=i[0]
    name[first_letter].append(i)
print(name )
first_letter=[i[0] for i in names]
count=Counter(first_letter)
print(count.most_common(1))

freq = {'d': 3, 'a': 2, 'c': 5, 'b': 1}
max_value=max(freq.items(),key=lambda k:k[1])
print(max_value)
sorted_dict= sorted(freq.items(),key=lambda k:k[1], reverse=True)
print(sorted_dict)

"""1. defaultdict — group even/odd numbers
Given numbers = [4, 7, 2, 9, 10, 3, 6, 15], use defaultdict(list) 
to group them into "even" and "odd" keys."""
numbers = [4, 7, 2, 9, 10, 3, 6, 15]
from collections import defaultdict
n=defaultdict(list)
for i in numbers:
    key="Even" if i%2==0 else "Odd"
    n[key].append(i)
print(n)

"""2. defaultdict — invert a list of words by length
Given words = ["cat", "at", "hat", "a", "sat", "it"], 
use defaultdict(list) to group them by length."""
a=defaultdict(list)
words = ["cat", "at", "hat", "a", "sat", "it"]
for word in words:
    key=len(word)
    a[key].append(word)
print(a)
"""3. defaultdict — nested grouping
Given sales = [("Jan", "apple"), ("Jan", "banana"), ("Feb", "apple"), ("Jan", "apple"), ("Feb", "mango")],
 use defaultdict(list) to group items sold per month."""
b=defaultdict(list)
sales = [("Jan", "apple"), ("Jan", "banana"), ("Feb", "apple"), ("Jan", "apple"), ("Feb", "mango")]
for month, fruit in  sales:
    b[month].append(fruit)
print(b)

"""4. defaultdict(int) — a new default type you haven't tried yet
Given text = "banana", use defaultdict(int) (instead of list) to count how many times each letter appears. 
Hint: int() with no arguments gives 0 — think about how that's useful here compared to defaultdict(list)."""
l=defaultdict(int)
text = "banana"
for i in text:
    l[i]+=1
print(l)

"""5. Sorting with key=lambda — by string length
Given words = ["apple", "fig", "banana", "kiwi", "watermelon"]"""
a={}
words = ["apple", "fig", "banana", "kiwi", "watermelon"]
v=sorted(words, key=lambda w: len(w))
print(v)
for word in words:
    value=len(word)
    a.setdefault(word,value)
print(a)
sorted_dict=sorted(a.items(),key=lambda k: k[1])
print(sorted_dict)

"""6. Sorting with key=lambda — by second character
Given names = ["Zoe", "Amy", "Bob", "Tia"]"""
names = ["Zoe", "Amy", "Bob", "Tia"]
sorted_dict=sorted(names,key=lambda k :k[1])
print(sorted_dict)

"""7. Combine both — most common word length using Counter + grouping via defaultdict
Given sentence = "the cat sat on the big red mat today"."""
sentence = "the cat sat on the big red mat today"
a=defaultdict(list)
words=sentence.split()
for word in words:
    key=len(word)
    a[key].append(word)
print(a)
length=[len(word) for word in words]
count=Counter(length)
print(count.most_common(1))

