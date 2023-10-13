#Operator // With Variable use 
#Arithmetic - Operators
x =10
y= 5
print(x+y)
x= 2
y= 10
print(x+y)
print(10-3)
print(3-10)
print(3*10)
print(10*3)
print(10**3)
print(3**10)
print(10/3)
print(10//3)
print(10%3)
# Operator precedence With Example - PEMDAS
#only power right To left 

x= 2*3-1
print(x)
y=2**3-1
print(y)
#WAP to Print avg marks of 3subject 
a = 80
b= 85
c = 90
print((a+b+c)/3)
#Wap to print Area of Circle 
pi = 3.14
r=4.5
area = pi*r**2
print(area)
#Wap to print  to convert f to c
f = 102
c = (f-32)*5/9
print(c)
#Wap to print to Dollor to INR
Dollar = 80
INR = Dollar**70
print(INR)
#Wap To print to INR TO Dollorrate = 70
inr = 500
dollar = inr / 70
print(dollar)
# Assigenmet Operator 
x = 10
y = 5
x += y
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
print(x)
x %= y
print(x)
x **= y
print(x)
x //= y
print(x)
#Multiple Assignment
x,y= 4,5
print(x,y)
#chained Assignment
a=b=c=5
print(a,b,c)

# Comparision Operator
print(10 == 10)
print(10 != 5)
print(10 > 5)
print(10 < 5)
print(10 >= 10)
print(10 <= 5)
#Logical  Operator 
# Logical Operator
x = True
y = False

print(x and y)
print(x or y)
print(not x)
# And  Operator 
print(10== 10and 5>7)
#logical Operator 
# Logical Operator
x = True
y = False

print(x and y)
print(x or y)
print(not x)
print(10 == 10 and 5 > 7)
# Logical notx = True
print(not x)
y = False
print(not y)
# sign operator
# sign operator
x = -10
print(+x)
#del Operator 
# Deleting variables
x = 10
y = 20
z = 30

del x, y, z

# Deleting elements from a list
my_list = [1, 2, 3, 4, 5]
del my_list[2]

# Deleting elements from a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
del my_dict["b"]

# Deleting elements from a set
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
