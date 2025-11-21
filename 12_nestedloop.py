# nested loop = A loop within another loop (outer, inner)
#                          outer loop:
#                              inner loop:

# for-for nested loop
for i in range(1,4):
    for j in range(i):
      print(j,end="")
    print()

row=int(input("Enter the number of rows:"))
columns=int(input("Enter the number of columns: "))
symbole=input("Enter the symbole you wanna use: ")

for y in range(row):
    for x in range(columns):
        print(symbole, end="")
    print()

row=int(input("Enter numbers of rows: "))
symbole=input("Enter symbole: ")
for i in range( 1,row+1):
    for j in range(i):
        print(symbole , end="")
    print()

#EXERCISE 1 :FOR-FOR NESTED LOOP[basic to advance problems]

#level:1 easy
# 1. Print a 3x3 grid of stars
symbole="*"
for i in range(1,4):
    for j in range(1,4):
        print(symbole, end="")
    print()


#2. Print numbers in a 4×4 grid
for x in range(1,5):
    for y in range(1,5):
      print(x,end=" ")
    print()
    
# 3. Print each row like this
#0 1 2
#0 1 2
#0 1 2
for x in range(2):
    for y in range(3):
        print(y,end=" ")
    print()

# 4. Print a multiplication table up to 5
for x in range(1,11):
    for y in range(1,11):
        print(x*y , end=" ")
    print()

# level:2 Medium

#6. Print a table of coordinates (i, j)
"""For i from 0 to 3
For j from 0 to 2"""
for i in range(4):
    for j in range(3):
        print((i,j),end=" ")
    print()

# 7. Print a growing number triangle
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

#8. Print reversed number triangle
for i in reversed(range(1,6)):
    for j in range(1,i+1):
        print(j , end="")
    print()

# 9. Print this pattern
"""A
   BB
   CCC
   DDDD
   EEEEE"""
alphabates="ABCDE"
for i in range(len(alphabates)):
    for j in range(i+1):
        print(alphabates[i],end="")
    print()

# 10. Print prime numbers from 1–50 (nested loop required)
"""Outer → loop numbers 1 to 50
Inner → check divisors"""
for x in range(2,51):

    for y in range(2,x):
        if x%y==0:
            break

    else:
        print(x,end=" ")

# 11. Find all 2-digit numbers where the sum of digits is 10
"""Use nested loops:
Outer → tens digit (1-9)
Inner → ones digit (0-9)"""
for i in range(1,10):
    for j in range(0,10):
        if i+j==10:
            print(i,j,"→",i*10+j)
print()
     
#12. Print all 2-digit numbers whose digits multiply to 
for i in range(1,10):
    for j in range(0,10):
        if j*i==12:
           print(i,j,"→",i*j,"→",12)
print()

#13. Print all numbers from 10–99 where:
"""The first digit is even
The second digit is odd
The sum of digits is less than 10"""
for x in range(1,10):
    for y in range(0,10):
        if y%2==0 and x%2!=0 and y+x<10:
            print(x,y,end="")
print(x)