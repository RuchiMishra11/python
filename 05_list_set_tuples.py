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
a=(1,3,2,4)
#SOME METHOD OF TUPLES
print(a.index(3))
print(a.count(4))

# OTHER IMPORTANT TUPLE FEATURES (not the methods)
"1.Accessing items (indexing):"
A=(1,23,4,5,4,3)
print(A[-1])
print(A[1])
print(A[3])

"2. Slicing:"
A=(1,23,4,5,4,3)
print(A[:4])
print(A[:2])
print(A[1:5])

"3. Concatenation: "
a=(1,24,4,3,4,3)
b=(12,3,4,34,3)
print(a+b)

"4. Repetition"
a=(5,)
print(a*3)
b=(1,2,3,4)
print(b*2)

"5. Membership check (in)"
t=(1,3,4)
print(1 in t) #True
print(3 in t) #True
print(6 in t) #False
print(2 in t) #False

"6. Length of tuple"
x=(1,3,4,3)
print(len(x))

"7. Tuple unpacking"
t=(1,2,3)
a,b,c=t
print(a,b,c)

"8. Nested tuples"
t = (1, (2, 3), 4)
print(t[1][0])   # 2
a=(1,2,(3,4),9,"hello")
print(a[2][1])
print(a[4][2])
print(a[4][4])
print(a[4][1])

"9. Converting tuple → list (to modify)"
t={1,2,3}
l=list(t)
l.append(4)
t=tuple(l)
print(t)

#PRACTICE PROBLEM
# 1. Count how many times an item appears in a tuple
"""Input: (1,2,3,2,4,2,5)
Output: 2 appears 3 times"""
tup=tuple(input("Enter anything with spaces: ").split())
item=input("Enter item that you need to count in tuple: ")
print(f"Item {item} appears {tup.count(item)} times.")


# 2. Find the index of a value in a tuple
"""Input: (10,20,30,10,40)
Find index of 10"""
tup=tuple(input("Enter anything with spaces: ").split())
item=input("Enter item whose index you wanna find : ")
print(f"Item {item} index is  {tup.index(item)} .")
if tup.count(item)>1:
    last_index=len(tup) -1 - tup[::-1].index(item)
    print(f"And the last index of {item} is {last_index}")
 
# 3. Create a tuple from user inputs until they type stop
list=[]
while True:
    a=input("Enter  something: " )
    if a.lower()=="stop":
        break
    list.append(a)
t=tuple(list)  
print(t)

# 4. Check if a tuple contains a given element
tup=tuple(input("Enter something with spaces: ").split())
item=input("Enter the item  you wanna search in the tuple: ")
if item in tup:
    print("Found!")
else:
    print("Not Found!")

# 5. Reverse a tuple using slicing
"Output: (5,4,3,2,1) → (1,2,3,4,5)"
tup=(5,4,3,2,1)
reversed_tup=tup[::-1]
print(reversed_tup)

# 6. Concatenate two tuples and print the result
a=(1,2,3,4)
b=(5,6,7,8,9)
c=a+b
print(c)
# 7. Convert a list into a tuple
l=[1 ,3,4,4]
t=tuple(l)
print(t)

# 8. Convert a tuple into a list and add a new element
t=(1,2,3)
l=list(t)
l.append(4)
t=tuple(l)
print(t)

# 9. Given a tuple, print all even numbers from the tuple
tup=(1,2,3,4,5,6,7,8,9,10)
for i in tup:
    if i%2==0:
        print(i,end=",")
print()

# 10. Unpack a tuple of 3 elements into 3 variables
tup=(1,2,3)
a,b,c=tup
print(a,b,c)

#2D COLLECTION :A collection inside another collection.
"we can use the method of the collection which are used to create a 2d list for a given 2d collection"

# Here are a few different 2d collection combinations:

#printing 2D number pad using 2D collections:
# 2D list of lists
num_pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"]]
print(num_pad)

# 2D list of tuples
num_pad = [(1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")]
print(num_pad)
           
# 2D list of sets(unordered )
"""num_pad = [{1, 2, 3},
           {4, 5, 6},
           {7, 8, 9},
           {"*", 0, "#"}]
   print(num_pad)"""

# 2D tuple of lists
num_pad = ([1, 2, 3],
           [4, 5, 6],
           [7, 8, 9],
           ["*", 0, "#"])
print(num_pad)


# 2D tuple of tuples
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))
print(num_pad)
# 2D tuple of sets (unordered sets inside the collection)
"""num_pad = ({1, 2, 3},
           {4, 5, 6},
           {7, 8, 9},
           {"*", 0, "#"})
   print(num_pad)"""

# 2D set of lists (NOT VALID)
# num_pad = {[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9],
#            ["*", 0, "#"]}
# print(num_pad)

# 2D set of tuples (unordered)
"""num_pad = {(1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#")}
    print(num_pad)"""

# # 2D set of sets (NOT VALID)
# num_pad = {{1, 2, 3},
#            {4, 5, 6},
#            {7, 8, 9},
#            {"*", 0, "#"}}
# print(num_pad)

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

# 1. Create a 2D list of 3 students with 2 marks each
student_info=[("mimi",2),
              ("sid" ,2 ),
              ("dev",2)]
for row in student_info:
    for info in row:
        print(info,end=" ")
    print()

# 2. Print all elements in a 2D list
l=[(1,2,3),
   (4,5,6),
   (7,8,9)]
for row in l:
    for i in row:
        print(i ,end=" ")

    
# 3. Find the sum of all numbers in a 2D list
total=0
l=[(1,2,3),
   (4,5,6),
   (7,8,9)]
for row in l:
    for i in row:
        total+=i
print()
print(total)


# 4. Count total elements in a 2D list
count=0
l=[(1,2,3),
   (4,5,6),
   (7,8,9)]
for row in l:
    for i in row:
        count+=1
print(count)

# 5. Find the largest number in a 2D list
l=[(1,2,3),
   (4,5,6),
   (7,8,9)]
largest_num=l[0][0]
for row in l:
    for i in row:
        if i>largest_num:
            largest_num=i
print(f"Largest number: {i}")

# 6. Transpose a 2D list (rows → columns)
l=[(1,2,3,4),
   (5,6,7,8)]
transpose=list(zip(*l))

for i in transpose:
    print(f"{i},")

# 7.Find the sum of each row
row1=0
row2=0
l=[(1,2,3,4),
   (5,6,7,8)]
for i in range(len(l)):
    print(f"Row{i+1} → {sum(l[i])}")

# 8. Print only even numbers from a 2D list
l=[(1,2,3),
   (4,5,6),
   (7,8,9)]
for row in l:
    for i in row:
        if i%2==0:
           print(i,end=" ")
print()   

# 9. Check if a number exists in a 2D list
l=[(1,2,3),
   (4,5,6),
   (7,8,9)]

num=int(input("Enter the number you wanna check in: "))
found=False
for row in l:
    for i in row:
        if i==num:
            found=True
            break
if found:
    print(f"{num} is there in list.")
else:
    print(f"{num} is not  there in list.")



# 10. Flatten a 2D list into a 1D list
l=[(1,2,3),
   (4,5,6),
   (7,8,9)]
l1=[]
for row in l:
    for i in row:
        l1.append(i)
print(l1)


















