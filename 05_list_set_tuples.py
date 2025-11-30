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



