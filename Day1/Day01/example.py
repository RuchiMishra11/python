#day1
print("hello world")
print("my name is  echii")
name='echii'
age=27
marks=67.5
print("my name is " , name ,",","i am ",age,"years old" , ".","I got ", marks ,"%" )
#data type
print(type(name))
print(type(age))
print(type(marks))
#types of  overator in python
# Arithmetic operator(+,-,*,/,**,%)
a=4
b=2
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a%b)
#relational operator (==,!=,>=,<=,<,>)
print(a==b) #False
print(a!=b) #True
print(a>=b) #True
print(a>b) #True
print(a<=b) #False
print(a<b) #False 
#assigment operator 
c=4
c+=2
print(c)  # 6
c-=2   
print(c) # 4 
c*=2
print(c) # 8
c**=2
print(c)  #64
c/=16
print(c)    #4
c%=2  
print(c)  #0
#note  
# (a>=b) - True 
# (a!=b)- True 
# (a==b) - False 
# (a<=b) - False
# logical operator 
print(not(True)) #False
print(not(False)) #True
print("And operator:", True and  True) #True
print("And operator:", True and  False) #False 
print("And operator:", False and  False) #False 
print("Or operator :", True or True) # True
print("Or operator :", True or False) #True
print("Or operator :", False or False) # False
"""  Practice of logical operators  with some variables """
print(not(a!=b)) #False
print(not(a==b)) #True
print("And operator :", (a!=b)and (a>=b)) #True
print("And operator :",(a==b)and (a<=b) ) #False
print("And operator:", (a>=b)and (a<=b)) # False 
print("Or operator :", (a!=b) or (a>=b)) #True
print("Or operator :",(a==b) or (a<=b) ) #False
print("Or operator:", (a>=b)or (a<=b)) # True 
# type conversion 
"""automatically"""
x=2.4
y=4
print(x+y) # 6.4
#type casting
e=3
f="4"
g=int(f)
print(e+g)
# taking input in python 
name1 = input("Enter your name:")
agE = int(input("Enter your age: "))
mark= float(input("Enter your marks:"))
print("wellcome", name1,",","you age:",agE,".","your marks:", mark)















