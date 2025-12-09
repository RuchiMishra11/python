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
