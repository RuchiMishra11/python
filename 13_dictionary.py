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

