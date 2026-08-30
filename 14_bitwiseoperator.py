"Complement(~): use 2's complement "
"""eg : 00001100 :12
        11110011 :~12  now let's check whether ~12 ==-13 
         for -13 we need to find  2's complement of  13 
         00001101 :13
         11110010 :~13(1's complement of 13) 
               +1 :(to find 2's complement of any nummber we add 1 to 1's complement)
         11110011 :-13 , this is equal to ~12 
         therefore ~12=-13"""

print(~12) #-13
print(~13) #-14 
print(~46) #-47

"bitwise and : & (if both 1,1 then 1 )  "
""" how this works :
    00001100 :12
    00001101 :13
    00001100 :12 (by comparing 12&13(0,0=0, 1,0=0 , 1,1=1))"""

print(12&13) #12
print(32&64) #0
print(45&67) #1

"bitwise or :| (if one is 1 then 1 (1,0=1)(1,1=1)(0,0=0))"
"""how this works :
    00001100 :12
    00001101 :13
    00001101 :13 (by comparing  12|13)"""
print(12|13)#13
print(8|5) #13
print(45|67) # 111

 