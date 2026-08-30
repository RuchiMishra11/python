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
