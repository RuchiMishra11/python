#   List  = [] ordered and changeable. Duplicates OK
fruits=["apple","banana","graps","orange","watermelon"]
"len(): for counting the numbers of items of list"
print(len(fruits))#5
"help functions"
# print(dir(fruit))
# print(help(fruit))
"count() : for counting items  of list"
print(fruits.count("apple")) #1
"append() : to add a new item to the list"
fruits.append("pineapple")
print(fruits) #["apple","banana","graps","orange","watermelon","pineapple"]
"insert(index,item): for inserting  an item at specific place"
fruits.insert(1,"lichi")
print(fruits)  #["apple","lichi","banana","graps","orange","watermelon","pineapple"]
"extend(list): add multiple  items at once to list. "
fruits.extend(["strawberry","coconut"])
print(fruits) #["apple","lichi","banna","graps","orange","watermelon","pineapple","strawberry","coconut"]]
"remove():remove a specific first matching items from list"
fruits.remove("lichi")
print(fruits) #["apple","banana","graps","orange","watermelon","pineapple","strawberry","coconut"]
"pop(index): Remove the  item at specific index"
print(fruits.pop(-2)) 
print(fruits)#["apple","banana","graps","orange","watermelon","pineapple","coconut"]
print(fruits.pop()) #remove the last item if nothing is written on the index
print(fruits)  #["apple","banana","graps","orange","watermelon","pineapple"]
"index():Find out the index of the specific item"
print(fruits.index("pineapple")) #5
"sort(): list the items in accending order"
fruits.sort()
print(fruits)   #["apple","banana","graps","orange","pineapple","watermelon"]
fruits.sort(reverse=True)
print(fruits) #decending #["watermelon","pineapple","orange","graps","banana","apple"]
"reverse(): reverse the element of list "
fruits.reverse()
print(fruits) #["apple","banana","graps","orange","pineapple","watermelon"]
"clear(): clear every items of list"
fruits.clear()
print(fruits)  #[]

#PRACTICE PROBLEM
#1. Take 5 numbers from user → store in list → print the list
#using while loop
a=[]
while len(a)<5:
    num=input("Enter a number: ")
    a.append(num)
print(a)

# using for loop:
a=[]
for i in range(5):
    num=input("Enter a number: ")
    a.append(num)
print(a)

#easy and advance version :
a=[int(input("Enter a number: ")) for _ in range(5) ]
print(a)


#2. Ask user 10 numbers → print the largest and smallest
"(Hint: use max() and min())"
x=[input("Enter a number: ") for i in range(10)]
print(x)
print(max(x))
print(min(x))

#3. Insert an element at 2nd position in a list
a=['a','c','d']
a.insert(1,"b")
print(a)

#4. Remove all occurrences of a number from a list
"(e.g., remove all 2)"
a=[1,3,3,4,42,42,5,4,2,3,1]
while 3 in a:
    a.remove(3)
print(a)
#5. Count how many even and odd numbers are in a list
a=[1,3,2,42,4,42,5,6,7,78,34,3,9]
even_count=0
odd_count=0
for x in a :
    if x%2==0:
        even_count+=1
    elif x%2!=0:
        odd_count+=1
print(f"The list have {even_count} even numbers and {odd_count} odd numbers")
        

#6. Reverse a list WITHOUT using reverse()
"(Hint: slicing or loop)"
a=[1,3,2,42,4,42,5,6,7,78,34,3,9]
print(a[::-1])

#7. Ask user a sentence → convert it into words list
"(Hint: .split())"
sentence=input("Enter a sentence: ")
word=sentence.split()
print(word)

#8.Merge two lists into one WITHOUT using extend
"(Hint: loop)"
x=['a','b','c','d']
y=['e','f','g','h']

for j in y:
    x.append(j)
print(x)

#9.Given a list, create a second list containing only unique values
"(Hint: check if item not in new_list:)"
a=[1,3,2,42,4,42,5,6,7,78,34,3,9]
unique_list=[]
for x in a:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)


#10. Sort a list WITHOUT using sort()
"(Hint: implement bubble sort logic)"
a=['a','e','c','b','d']
b=len(a)
for i in range(b):
    for j in range(b-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)

#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
set={1,2,3}
"add():add a new element to the set"
set.add(4)
print(set)
"update() — Add multiple elements takes a list, tuple, set… anything iterable."
set.update({5,6},[7,8])
print(set) #{1,2,3,4,5,6,7,8}
"remove() — removes item but errors if not founds"
set.remove(7)
print(set) #{1,2,3,4,5,6,8}
"discard() — removes item but NO error if item not found"
set.discard(8)
print(set)
set.discard(9)
print(set)
"pop() — removes a random item"
set.pop()
print(set)
"len()- count the number element of set"
print(len(set))
# MATHEMATICAL SET OPERATIONS
"union() — join two sets (no duplicates)"
x={1,3,4}
y={2,4,3}
print(x.union(y))  #{1, 2, 3, 4}
"intersection() — common elements"
print(x.intersection(y)) #{3, 4}
"difference() — elements present in A but not in B"
print(x.difference(y)) #{1}
"symmetric_difference() Elements NOT common in both sets(everything except intersection)"
print(x.symmetric_difference(y))  #{1, 2}
"issubset() / issuperset(): "
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))#True
print(a.issuperset(b)) #False
print(b.issuperset(a)) #True
"isdisjoint():check whether two sets are disjoint or not "
a={5,6}
b={1,2,3,4}
print(a.isdisjoint(b))#True

#PRACTICE PROBLEMS 
# 1. Remove duplicates from a list using a set.
"""Input:
[1,2,3,2,4,1,5]
Output:
[1,2,3,4,5]""" 


# 2. Find common elements between two lists using sets.
"""Input:
List1 = [1,2,3,4]
List2 = [3,4,5,6]"""

# 3. Check if a list has all unique elements (use set).
# 4. Given two sets, find elements in A that are not in B.
# 5. Count unique words in a sentence using a set.
"""Example:
"apple orange apple banana orange" """

# 6. Convert a string into a set of characters.
# 7. Given two sets, check if one is subset of the other.
# 8. Create a set from user input values until user types 'stop'.
# 9. Find the symmetric difference between two lists.
# 10. Remove all items from a set except even numbers.

#PRACTICE PROBLEMS 
# 1. Remove duplicates from a list using a set.
"""Input:
[1,2,3,2,4,1,5]
Output:
[1,2,3,4,5]""" 
a=set()
a.update([1,2,3,2,4,1,5])
print(a)

# 2. Find common elements between two lists using sets.
"""Input:
List1 = [1,2,3,4]
List2 = [3,4,5,6]"""
List1 = [1,2,3,4]
List2 = [3,4,5,6]
a=set()
b=set()
a.update(List1)
b.update(List2)
print(a.intersection(b))

# 3. Check if a list has all unique elements (use set).
x=[1,2,3,2,4,1,5] 
if len(x)==len(set(x)):
    print("All unique!")
else:
    print("Not unique!")


# 4. Given two sets, find elements in A that are not in B.
A={1,3,4,5}
B={3,2,4,2}
print(A.difference(B))

# 5. Count unique words in a sentence using a set.
"""Example:
"apple orange apple banana orange" """
sentence=input("Enter a sentence: ")
word=sentence.split()
unique_word=set(word)
print(f"""unique words count: {len(unique_word)}.
          unique words:{unique_word}""")

# 6. Convert a string into a set of characters.
a="miow"
print(set(a))
# 7. Given two sets, check if one is subset of the other.
a={1,2}
b={1,35,2,5,2}
print(a.issubset(b)) #True
print(a.issuperset(b))  #False
print(b.issuperset(a)) #True

# 8. Create a set from user input values until user types 'stop'.

s=set()
while True:
    element=input("Enter the element of set: ")
    if element.lower()=="stop":
        break
    s.add(element)
    
print(s)

# 9. Find the symmetric difference between two lists.
List1 = [1,2,3,4]
List2 = [3,4,5,6]
a=set(List1)
b=set(List2)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

# 10. Remove all items from a set except even numbers.
a=set()
s={1,2,3,4,5,6,7,8,9 ,10}
for i in s:
    if i%2==0:
        a.add(i)
print(a)










#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER



