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
     
#12. Print all 2-digit numbers whose digits multiply to 12
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


#while - while nested loop 

# 1. Print all pairs (i, j)
# using for for  nested loop
for x in range(1,4):
    for y in range(1,3):
        print((x,y))
print()

# using while while nested loop
x=1
while x<=3:
    y=1
    while y<=2:
        print((x,y))
        y+=1
    x+=1

# 2. Print a rectangle of 
# using for-for nested loop
row=3
column=3
symbole="*"
for x in range(row) :
    for y in range(column):
        print(symbole,end=" ")
    print()

# using while-while nested loop:
symbole="*"
row=1
while row<=3:
    column=1
    while column<=3:
        print(symbole,end=" ")
        column+=1
    row+=1
    print()

# 3. Print numbers in a grid
"""1 2 3
   4 5 6
   7 8 9"""

# using for nested loop 
num=1
for x in  range(3):
    for y in range(3):
        print(num,end=" ")
        num+=1
    print()

# using while nested loop 
num=1
row=1 
while row<=3:
    column=1
    while column<=3:
        print(num,end=" ")
        column+=1
        num+=1
    print()
    row+=1

# 4. Print multiplication table (1 to 5)
#using for nested loop :
for x in range(1,6):
   for y in range(1,11):
      result=x*y
      print(f"{x}x{y}={result}" )
   print()

# using while nested loop 
i=1
while i <=5:
   j=1
   while j<=10:
      result=i*j
      print(f"{i}x{j}={result}")
      j+=1
   print()
   i+=1

#  5. Print this pattern using while–while
"""*
   * *
   * * *
   * * * * """
# using for nested loop 
symbole="*"
for i in range(1,5):
    for j in range(i):
        print(symbole,end=" ")
    print()
    
# using while nested loop
symbole="*"
row=1
while row<=4:
    col=1
    while col<=row:
       print(symbole,end=" ")
       col+=1
    print()
    row+=1


# 6. Print reverse pattern
"""
* * * *
* * *
* *
*"""
# using for nested loop 
symbole="*"
for i in reversed(range(1,5)):
    for j in range(i):
        print(symbole, end=" ")
    print()

# using  while nested loop
symbole="*"
row=4
while row>=1:
    col=1
    while col<=row:
       print(symbole,end=" ")
       col+=1
    print()
    row-=1

# 7. Count how many pairs (i, j) satisfy i + j is even
"""i → 1 to 5
j → 1 to 5
Print only the pairs where:
(i + j) % 2 == 0"""
#using for nested loop 
for i in range(1,6):
    for j in range(1,6):
        if (i+j)%2==0:
            print(f"{i}{j}", end=" " )
    print()

#using while nested loop 
i=1
while i<=5:
    j=1
    while j<=5:
        if (i+j)%2==0:
            print(f"{i}{j}", end=" ")
        j+=1
    print()
    i+=1

# 8. Print a number triangle
"""For example:
1
1 2
1 2 3
1 2 3 4"""
#using for nested loop
for x in range(1,5):
    for y in range(1,x+1):
        print(y,end=" ")
    print()

#using while nested loop 
x=1
while x<=4:
    y=1
    while y<=x:
        print(y, end =" ")
        y+=1
    print()
    x+=1


    # 9. Find the first pair (i, j) where i * j > 20
"""i → 1 to 10
j → 1 to 10
Stop loops immediately when you find the first pair satisfying product > 20"""
#using for nested loop
found=False
for i in range(1,11):
    for j in range(1,11):
        if i*j>20:
            print(f"First pair:{i}{j}",end=" ")
            found=True
            break
    if found:
        break

#using while nested loop
found=False
i=1
while i<=10:
    j=1
    while j<=10:
        if i*j>20:
            print(f"First pair:{i}{j}",end=" ")
            found=True
            break
        j+=1

    if found:
        break
    print()
    i+=1


# 10. Print this pattern WITHOUT using string multiplication
"""    *
      ***
     *****
    *******"""
#using for nested loop 
row=4
for i in range(1, row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i - 1):
        print("*",end="")
    print()

#using while nested loop
row=4
i=1
while i<=row:

    j=1
    while j<=row-i:
        print(" ",end="")
        j+=1
    k=1 

    while k<=2*i-1:
        print("*", end="")
        k+=1

    print()
    i+=1

# WHILE - FOR NESTED LOOP (exercise)

# 1. Print this pattern  using while-for nested loop
"""1 2 3
   1 2 3
   1 2 3"""
# Using while-for nested loop 
i=1
num=1
while i<=3:
    for j in range(1,4):
        print(j, end=" ")
        
    print()
    i+=1
    
#using  for nested loop
for i in range(3):
    for j in  range(1,4):
        print(j, end=" ")
    print()

#using while nested loop
i=1
while i<=3:
    j=1
    while j<=3:
        print(j, end=" ")
        j+=1

    print()
    i+=1

# 3. Find first pair (i, j) where i+j > 6
"""Stop both loops immediately."""
#using while-for nested loop
i=1
found=False
while i<=5:
    for j in range(1,6):
        if i+j>6:
            print(f"First pair:{i}{j}")
            found=True
            break
    if found:
        break
    print()
    i+=1

#using for for nested loop:
found=False
for i in range(1,6):
    for j in range(1,6):
        if i+j>6:
            print(f"First pair: {i}{j}")
            found=True
            break
    if found:
        break
    print()

#using while while nested loop:
found=False
i=1
while i<=5:
    j=1
    while j<=5:
        if i+j>6:
            print(f"First pair: {i}{j}")
            found=True
            break
        j+=1
    if found:
        break
    print()
    i+=1

# 4. Print stars in this pattern using while–for
"""*
   **
   ***
   ****"""
#using while for nested loop:
symbole="*"
i=1
while i<=4:
    for j in range(i):
        print(symbole, end="")
    print()
    i+=1

#using for for nested loop
symbole="*"
for i in range(5):
    for j in range(i):
        print(symbole,end="")
    print()

#using while while nested loop
symbole="*"
i=1
while i<=4:
    j=1
    while j<=i:
        print(symbole, end="")
        j+=1
    
    print()
    i+=1

# 5. Count how many pairs (i, j) have product < 10
#using while for nested loop
count=0
i=1
while i<=5:
    for j in range(1,6):
        if i*j<10:
            count+=1
            
    i+=1
print(f"Total pair:{count}")

#using for for nested loop
count=0
for i in range(1,6):
    for j in range(1,6):
        if i*j<10:
            count+=1
    i+=1
print(f"Total pairs:{count}")

#using while while nested loop
count=0
i=1
while i<=5:
    j=1
    while j<=5:
        if i*j<10:
            count+=1
        j+=1
    i+=1
print(f"Total pairs:{count}")

# 6. Print multiplication table (1 to 5) using while–for
#using while-for nested loop
i=1
while i<=5:
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()
    i+=1

#using for-for nested loop
for i in range(1,6):
    for j in range(1,11):
        print(f"{i}x{j}={i*j}")
    print()
    
#using while-while nested loop
i=1
while i<=5:
    j=1
    while j<=10:
        print(f"{i}x{j}={i*j}")
        j+=1
    print()
    i+=1

# 7. Print this pattern without using string multiplication
"""   *
      ***
     *****
    *******"""
#using while for nested loop
row=5
i=1
while i<row:
    for j  in range(row-i):
        print(" ",end="")
    
    for k in range(2*i-1):
        print("*",end="")
    
    print()
    i+=1

#using for for nested loop
row=4
for i in range(1,row+1):
    for j  in range(row-i):
        print(" ",end="")
    
    for k in range(2*i-1):
        print("*",end="")
    
    print()

#using while for nested loop
row=5
i=1
while i<row:
    j=1
    while j<=(row-i):
        print(" ",end="")
        j+=1
    
    k=1
    while k<=(2*i-1):
        print("*",end="")
        k+=1
    
    print()
    i+=1
  
