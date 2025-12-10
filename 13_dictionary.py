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

# 4 Create a dictionary of word → length for a full sentence.
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
details={"Riya":34,"sid":24,"Ruchi":18,"Mahesh":25,"tripti":8}
new_details={k:v for k,v in details.items()if v>=18}
print(new_details)

#9. Count how many times each vowel appears in a full sentence.
sentence=input("Enter a sentence:")
vowel="aeiou"
d={v:sentence.count(v) for v in vowel if v in sentence}
print(d)

#10. From a list of names, create a dictionary of name → first letter.
l=["Mahesh","Ruchi","Piya","Komal"]
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