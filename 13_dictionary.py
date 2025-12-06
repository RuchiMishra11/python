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
