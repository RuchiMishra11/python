#strings (texts)
name="echii"
fav_food= "pizza"
hobbie= 'coding'
print( "my name is ",name,".","my favourite food is ",fav_food,"," "my hobbie is ",hobbie,".")
#f string formating 
print(f"my name is {name}.my favourite food is {fav_food},my hobbie is {hobbie}.")
#integer(number)
age=18
contact_no= 892849
print(f"i am {age} years old. you can contact me on {contact_no}.")
#float(decimal)
marks=69.5
price=89.5
distance=7.4
print(f'i got {marks}% in my high school.')
print(f"The price of the food is ${price}.")
print(f'i ran {distance}km.')
#boolean(true,false)
bool_1=True
bool_2=False
print(f"am i doing my maximum ? {bool_2}.")
print(f"are you unstoppable ? {bool_1}.")
is_online= True
if is_online:
    print("you are online.")
else:
    print("you are not online.")
is_saling=False
if is_saling:
    print("This is for sale.")
else:
    print("This is not for sale.")
# type casting : is a process of converting variable from one data type to another
# (funtion use for this: str() , int() , float() , bool())
# explicit typcasting (externally instructed)
text="hello"
number=9
decimal=5.5
bool_3= True
print(type(text))
print(type(number))
print(type(decimal))
print(type(bool_3))
decimal=int(decimal)
number=float(number)
bool_3=str(bool_3)
text=bool(text)
""" text=bool(text) when we print variable which contain string  after type casting  it to bool we 
   get true if some strings written within the quote( double ,single ) we get true when we print(text) now  if there is  nothing written 
   withing the double quote then we get false whem we print( text ) """
print(text) #True
print(number)
print(bool_3)
print(decimal)
print(type(text))
print(type(number))
print(type(decimal))
print(type(bool_3))
print(type(float("5.4")))
# implicit type casting (automatically converts )
x=3
y=3.0
x=x/y
print (x)