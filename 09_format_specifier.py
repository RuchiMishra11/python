# format specifiers = {value :flags) format a value based on what
#flags are inserted
price1=3.14159
price2=-987.53
price3=12.34
#.(number)f = round to that many decimal places (fixed point)
print(f"Price1 is ${price1:.2f}")
print(f"Price2 is ${price2:.2f}")
print(f"Price3 is ${price3:.2f}")
import math
price1=2.34
price2=34.5
price3=-6.3
print(f"Price1 is ${price1:.1f}.")
print(f"price2 is ${math.floor(price1)}")
print(f"price2 is ${math.ceil(price2)}")
print(f"price3 is ${price3:.0f}")
print(f"price3 is ${math.floor(price3)}")
print(f"price3 is ${math.ceil(price3)}")

#: (number) = allocate that many spaces
print(f"Price1 is ${price1:3}")
print(f"Price2 is ${price2:3}")
print(f"Price3 is ${price3:}")

#: 03 allocate and zero pad that many spaces
print(f"Price1 is ${price1:09}")
print(f"Price2 is ${price2:09}")
print(f"Price3 is ${price3:09}")

#: <= left justify
print(f"Price1 is {price1:<10}")
print(f"Price2 is {price2:<10}")
print(f"Price3 is {price3:<10}")

#: > = right justify
print(f"Price1 is {price1:>9}")
print(f"Price2 is {price2:>9}")
print(f"Price3 is {price3:>9}")

#: ^ = center align
print(f"Price1 is {price1:^10}")
print(f"Price2 is {price2:^10}")
print(f"Price3 is {price3:^10}")

#:+ = use a plus sign to indicate positive value
print(f"Price1 is ${price1:+}")
print(f"Price2 is ${price2:+}")
print(f"Price3 is ${price3:+}")

# : = = place sign to leftmost position
print(f"Price1 is ${price1:=}")
print(f"Price2 is ${price2:=}")
print(f"Price3 is ${price3:=}")

#: = insert a space before positive numbers
print(f"Price1 is ${price1: }")
print(f"Price2 is ${price2: }")
print(f"Price3 is ${price3: }")

#:, = comma separator
print(f"Price1 is ${price1:,}")
print(f"Price2 is ${price2:,}")
print(f"Price3 is ${price3:,}")





















