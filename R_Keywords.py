"""#import keyword
#print(keyword.kwlist

#integer
x=143
print(type(x))

#binary form
y=0b111
print(type(y))
print(y)

#octal form
z=0o123
print(type(z))
print(z)

#hexadecimal from
hvar=0XFACE
print(type(hvar))
print(hvar)

print(bin(15))#binary
print(oct(15))#octal
print(hex(15))#hexa decimal

#Formatting a string:
#{}=Replacement operator
#f=formatting
#r=Raw
x="learn coding"
y=f"subscribe to our channel : {x}"
print(y)

print(f"sum of 2 and 6 is {2+6}")

#Methods Of Strings:
#1)split("pattern")
#2)("pattern").join(sequence)
#3)find("pattern","start","end")=-1
info="a quick brown fox jumps over the lazy dog"
print(info.find('fox'))
print(info.find('o',11))
#4)index("pattern","start","end")=Error
#5)count("pattern","start","end")
info="a quick brown fox jumps over the lazy dog"
print(info.count('o'))
print(info.count('o',16))
#6)strip()=remove all spaces
info="      a quick     brown fox jumps        over the lazy dog"
print(info.strip())
#7)replace("old pattern","new pattern")
info="a quick brown fox jumps over the lazy dog"
print(info.replace('o','*'))

#changing case:
1)upper()
2)title()
3)lower()
4)capitalize
5)isupper()
6)islower()
7)isalpha()
8)isalnum()
9)isspace()

#Range(datatype)
#range(begnining,ending,step)
x=range(10)
print(type(x))
for i in x:
    print(i)

#Type Casting:
a="123"
b=int(a)
c=float(a)
print(type(b))

#Operators:
#1)Arthematic operators;
a=10
b=20
print("addition:",a+b)
print("substraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)#float value
print("floor division:",a//b)#integer value
print("modulus division:",a%b)#remainder
print("power operator:",10**2)

#2)Relational /comparision operator
x=10
y=20
print(x>y)
print(x<y)
print(10==23)

#3)Logical operator:
print(0 and 10)
print(True or False)
print(not False)

#4)Betwise operator:
#i)betwise and
print(5 & 6)
#ii)betwise or
print(5 | 6)

print(5 ^ 6)
print( ~ 6)
print(15>>1)
print(15<<1)

#5)Assignment operator:
a=5
print(a)

#6)Special operator:
#a)Identity operator;
# is,is not

a=5
b=5
print(a is b)
print(a is not b)
print(id(a))
print(id(b))

#b)membership operator;
# in,not in

var="India is great"
print("great" in var)
print("hello" not in var)

#Iput and Output Functions:
user_input=eval(input("enter your name:"))
print(type(user_input))
print("good evening",user_input)

#eval=evaluate()=evaluate anything
print(eval("2+2*2"))

#print("hello world","you are too good",sep="-")
print("hello world",end="*")
print("you are too good")"""


