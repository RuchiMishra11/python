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
