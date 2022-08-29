"""
print("hello world")
print("hello ccvm")
print(" i know how to count .. 1 2 3 4 5 ..")

# single line comment
'''multline comment''' or """"""

# data_variable
name = "bablu"
age = 21
name ="mohit"
is_adult = True
print(age)
print(name)
person_name = "Tony_Stark"
Tony_age =51
print(person_name)
print(Tony_age)
print("Tony is a genius")
first_name = "Tony"
last_name = "Stark"
print(first_name + " " + last_name)
Tony_age =51
print(Tony_age)
is_adult = "Tony is a genius."
print(is_adult)


#taking input from  user
name = input("what is your name?")
print("hello" + name)  #Concatention (two sting concatention of one sentence)
hero = input("who are your superhero")
print(hero)

# type conversion
old_age = input("enter the old age : ")
new_age = int(old_age) + 10
print(new_age)
number = 23
print(float(23))
print(str(number))
print(bool(number))


# print sum of 2 numbers
r = 3
s = 2
t = r + s
print(t)

'''taking input value'''
x,y,ch = input("enter the number").split()  #one line many type input.
x = int(x)
y = float(y)
print("%d $ %.2f $ %c"%(x,y,ch)) # one line many type output.
n,m = map(float,input("enter the numbers").split())
print("%.2f %.2f"%(n,m))
a = input("enter the first  number for sum : ")
b = input("enter the second number for sum : ")
c = int(a)+int(b)
print("sum of two number is :" , c)
print("sum of two number is :" + str(c))

# python fundaments:-
a = 5
b = 4
c = 6.984
d = 6
st = "name"


#arithmetic operators
print(a + b)
print(a // b)
print(a / c)
print(a % c)

#relatoinal  operators
print(a < b)
print(a <= b)
print(a == c)
print(a > d)
print(a > b and d <= 6)
print(a < b and d >= 6)
print(a < c or d > 6)

# Bitwise operators
print(2 | 3)
print(a ^ b)
print(a and b)

# string convert
name = "mohit Singh"
print(name.upper())
print(name.lower())
print(name.find('S'))
print(name.find('T'))
print(name.find("mohit"))
print(name.replace("mohit Singh", "Bablu kumar"))
print(name.replace("Singh", "stark"))
print(name.replace('m', 'k'))


#boolan find
print('h' in name)
print('a' in name)
print("Singh" in name)

#Arithmetic Operation
print(5 + 2)
print(3 - 8)
print(2 * 5)
print(5 ** 4)
print(5 / 2) #floating value print
print(5 // 2) #only integer value print
x = input("enter the 1 number for arithmetic operation ")
y = input("enter the 2 number for arithmetic operation")
cal = (int(x) + int(y)) - (int(x) * int(x)) % (int(x) - int(y)) + (int(x) / int(y)) * (int(x) // int(y))
print(cal)


#shortcut calcultion
i = 5
i = i + 1  # 6
i += 1
i -= 3  # 7-3
i *= 4  #4*4
i /= 5  # 16/5
i %= 3  #3.2%3
print(i)
result = 2 + 3 * 5
print(result)


# comparison Operators
print(3 > 2)
print(3 <= 4)
print(3 == 6)
print(5 != 6)
d=input("enter the  integer number for comparison operators ")
e=input("enter the integer number for comparison operators")
print(e>d)
print(d<=e)
print(d!=e)


#logical operators 
print(3 > 2 and 3>=3)
print(3 <= 4 or 3 !=3)
print(not 3 >5)
f=input("enter the  integer number for logical operators ")
g=input("enter the integer number for logical operators")
print(f>g and g<f)
print(f<g or g<=f)
print(not f==g ) 


# if-else condition
h = 5
k = 10
if(h < k):
    print("H is greater number")
else:
    print("k is the greater number")
p = input("enter the number:")
q = input("enter the number:")
s = input("enter the number:")
if(p > q):
    R = (int(p) + int(q))
    print(R)
else:
    R = (int(p)-int(q))
    print(R)
if(p > q):
    if(p > s):
        print("p is the greater number")
    else:
        print("S is the greater number ")
else:
    if(q > s):
        print("Q is the greater number")
    else:
        print("S is the greater number")


#nested if_else condition
my_age = int(input("enter your age"))
if my_age >= 18:
    print("you are an adult")
    print("you can give vote")
elif my_age < 18 and my_age >= 15:
    print("you are in high edu")
elif my_age < 15 and my_age >= 5:
    print("you are student in school")
    print("enjoy the school life")
else:
    print("you are a child")
    
#let's Build a calculator

k=int(input("enter the first number"))
operator=input("enter the operator (+,-,/,%,*):")
m=int(input("enter the second  number"))
if operator == "+":
    print(k+m)
elif operator == "-":
    print(k-m)
elif operator == "*":
    print(k*m)
elif operator == "/":
    print(k/m)
elif operator == "%":
    print(k%m)
else:
    print("invalid choice")


#while loop
t=int(input("enter the number:"))
while(t>0): #checking condition(not using infinite loop )
    print("hello")
    t=t-1 #update condition
while(t<=10):# count number
    print(t)
    print(t * "hello")
    t=t+1
while(t<=10): #print trinagle *
    print(t * "*")
    t=t+1
while(t>=1): #print opp. tring. *
    print(t * "*") 
    t=t-1
x=12345667
rev=0
while x!=0:
    rev=rev*10+x%10
    x=x//10
    print(rev)
# reverse an integer 
m=int(input("enter the number for reverse integer "))
rev=0
while m!=0:
    rev=rev*10 + m%10
    m=(m//10)
print(rev)

#for loop
# range of number
numbers=range(1)
print(numbers)
for i in range(5):
    print(i)
for i in range(10):
    print(i+1)
    print("hello")
for i in range(10):
    print(i * "*")
    i=i+1
for i in range(5):
    for j in range(5):
        print(i * "*")
        i=i-1


#list(list is complex type in python & mutable(changeable))
friends=["aman","ram","mohan"]
print(friends[-1])
print(friends)
marks = [95,88.5,70.9,65.3,89] #write integer/float /string type
marks.append(78) # add in list end
marks.insert(3,78) #add in list  who give the index number
print(marks[0:6])
print(98 in marks) #check in marks
for score in marks:
    print(score)
print(len(marks)) #length of marks in list
marks = [95,88.5,70.9,65.3,89]
l=0
while l < len(marks):
    print(marks[l])
    l =l+1
marks.clear() # clear of marks list
print(marks)


#break &  Continue
students = ["Ram","Shayam","Mohan","Sohan","Radha","Radhika"]
for student in students:
    if student == "Radha":
        break;
    print(student)
students = ["Ram", "Shayam", "Mohan", "Sohan", "Radha", "Radhika"]
for student in students:
     if student == "Mohan":
        continue;
     print(student)
       
#while loop with break and contine.
i=5
n=500
while(i<=n):
    if(i>50):
        break
    i += 5
    print(i,end=" ")
    if(i==50):
        i+=2
        continue
    print(i,end=" ")
    i+=2
print('loop ended')  
     
#slicing of the python
l1=['a','b','c','d','e']
print(l1[::-4])
print(l1[-5: :-2])
print('b' in l1)
print('x' not in l1)
l1=l1+['x','y','w','t']# adding l1 elemnt in python
print(l1)
print(l1*3)
print (min(l1))
print(max(l1))
li=['a',1,['bb','ccd','dddd'],3,['abb',['xyz','pqr']]]
print(len(li))
print(len(li[2]))
print(len(li[4][1][1]))
print(li[4][1][1])
print(li[2][2])
print(li[2][2][1])
print(li[2][-2])
l1=['a','b',1,2,'abc']
l2="mohitsingh"
print(l1)
l1[-1]=100
print(l1)
print(l1[1:4])
l1[1:4]=[10000]
print(l1)
del l1[0]
print(l1)
l1=[1,2]+l1
print([1,2]+l1)
print(l1)
l1.append("abcd")
print(l1)
l1.pop(2)
var=l1.pop(1)
print(l1)
nums=set([1,1,5,6,6,6,4,4])
print(len(nums))


# tuple (they are like list ,but they are immutable,define(); )
marks=(78,56,58,85,78,56)
print(marks)
print(marks.count(56)) #count how many time
print(marks.index(56)) #which index
# Sets {sets are a collection of all unique elements. they can not indexing supported}
marks = {89,78,69,96,89,53,89}
name=set("mohit singh")
st="python"
print(list(st))
print(set(st))
print(name)
print(marks)
print(len(marks))
print('c' in name)
print(name.union(st))
s1={1,3,4,5,6,7}
s2={4,4,5,6,7,8,0}
s3={1,2}
s4={1,2,3,4,5,6,7,8,9}
print(s1|s2)
print(s1&s2)
print(s1-s2)
print(s2-s1)
print(s1.issubset(s3))
print(s2<=s3)
print(s2.issuperset(s1))
print(s3>=s1)
for score in marks:
    print(score)

#Dictionary :-stores a (key,value) pair sets
ipl_team={}
print(type(ipl_team))
ipl_team['mumbai']="ROHIT"
ipl_team['delhi']=["AMAN","RAKHI","SONA"]
print(ipl_team)
ipl_team[4]="mumbai indians"
print(ipl_team)
print(ipl_team['mumbai'])
print(ipl_team['delhi'][2])
del ipl_team[4]
print(ipl_team)
number={4:'d',3:'c',5:'e',0:'a',1:'b'}
print(number[5])
print(len(number))
number.clear()
print(number.get(4))
print(number.get(10,"key is not present"))
print(number.items())
print(number.keys())
print(number.values())
print(number.pop(5,"key is not present"))
print(number)
#print(number.popitem(1))
print(number)
marks = {"basis_of computer": 98,"c_language":95,"math":92,"pom":82,"co":78}
print(marks["math"])
marks["english"]=95 #add marks in dictionary
print(marks)
marks["pom"]=98 #existing marks change 
print(marks)


#functions:-
#module function
import math
print(dir(math))
from math import *
print(sqrt(4))

#user defined functions:- def function_name(parameters):

def print_sum(a,b=4):
    print(a+b)
print_sum(1)
def print_sub(a,b):
    print(a-b)
print_sub(4,6)


#number without reassgning number
def contnum(n):
    num=0
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end=" ")
            num=num+1
        print("\n")
num=int(input("enter the number"))
print(contnum(num))
#number without reassging letter
def contnum(n):
    num=65
    for i in range(0,n):
        for j in range(0,i+1):
            ch=chr(num)
            print(ch,end=" ")
            num=num+1
        print("\n")
num=int(input("enter the number"))
print(contnum(num))

#simple pyramid
def count(n):
    num=0
    for i in range(0,n):
        for j in range(0,i+1):
            print("@",end="")
        print("\n")
num=int(input("enter the numebr"))
print(count(num))

#using list
def pypart(n):
    mylist=[]
    for i in range(1,n+1):
        mylist.append("*"*i)
        print(('\n'.join(mylist)))
mylist=int(input("enter the number"))
print(pypart(mylist))



class node():
    def _init_(self, value, right, left):
        self.value = value
        self.right = None
        self.left = None


def tree():
    root = node(10, None, None)

    right = node(11, None, None)
    left = node(7, None, None)

    root.right = right
    root.left = left

    return root


root = tree()


def preOrder(root):
    if root == None:
        return
    print(root.value)
    preOrder(root.left)
    preOrder(root.right)


preOrder(root)


def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print(root.value)
    inOrder(root.right)


inOrder(root)


def postOrder(root):
    if root == None:
        return
    preOrder(root.right)
    preOrder(root.left)
    print(root.value)


postOrder(root)

# number patten half triangle
def numput(n):
    num=1
    for i  in range(0,n):
        num=1
        for j in range(0,i+1):
            print( num,end=" ")
            num=num+1
        print("\n")
num=int(input("enter the number"))
print(numput(num))


# tringle patten
def triangle(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end="")
        print("\n")
k=int(input("enter the numeber"))
print(triangle(k))
#tringle patten

def tringle(n):
    k=n-1
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k=n-k
        for j in range(i+1):
            print("*",end='')
        print("\n")
k=int(input("enter the number for patten"))
print(tringle(k))

#checking Armstrong number or not
num=int(input("enter the a number for armstrong"))
temp=num
cnt=0
while temp>0:
    cnt=cnt+1
    temp=temp//10
sum=0
temp=num
while temp>0:
    rem=temp%10
    sum=sum+pow(rem,cnt)
    temp=temp//10
if (num==sum):
    print("the number", num, "is an armstrong number")
else:
    print("the number",num, "is not an armstrong number")

#swap two number without using third variable

num1 = int(input("enter the number for swapping "))
num2 = int(input("enter the number for swapping"))
num1= num1+num2
num2=num1-num2
num1=num1-num2
print(num1)
print(num2)

#swap two number using third variable
n=int(input("enter the number for swapping"))
p=int(input("enter the number for swapping"))

temp=0
temp=n+p
n=temp-n
p=temp-p
print(n)
print(p)

# prime or not
num=int(input('enter the number for prime '))
if num<2:
    print("it is not prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("it is not prime number")
            break;
    else:
        print("it is prime number")
        
        
#fibonacci series using iterative method
num=int(input("enter the number for fibb"))
n=0
z=1
for i in range(0,num):
    if(i<=0):
        result=1
    else:
        result=n+z
        n=z
        z=result
    print(result)
    
#fibonacci series using recursive method
num = int(input("enter the number for fib"))
def fib(num):
    if num <= 0:
        return 1
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)
for i in range(0,num):
    print(fib(i))


# factorials program with iterative method.
def fact(n):
    if n<0:
        return 0
    elif n==1:
        return 1
    else:
        fact=1
        while(n>1):
            fact *=n
            n-=1
        return fact
num=int(input("enter the  fact number "))
print(fact(num))

# factroial using recursion  function
def fact(n):
    if n==0:
        return 1
    else:
         return n *fact(n-1)
         n =n-1
num = int(input("enter the first number"))
print(fact(num))


# desending order by using for loop

x=int(input("enter the number"))
for i in range(x,0,-3):
    print(i)
    
st="hello world"
for ch in st:
    print(ch)
for i in range(3,len(st)):
    print(st[i])
    
for i in range(20):
    if (i>10):
        break
    print(i)
print("loop endded")
for i in range(1,5):
    for j in range(0,7):
        print("i=",i,"j=",j)
for i in range(1,6):
    for i in range(i,6):
        print("*",end=" ")
    print()    
a = 0
while a < 5:
    print(a)
    a += 1
    if a == 3:
        break
else:
    print(0)
a = 2
while True:
    if a%3 == 0:
        break
    print(a,end=' ')
    a += 2
x=int(input("enter the nim"))
y=x**2
print(y)
n,m=input().split()#prepbyte question solution
sqr=int(n)*int(m)
print(sqr)

# basis program logic buildup...
x = "abcdef"
i = "i" # variable i not mention how many time executed
while i in x:
    print(i, end=" ") # no output display because i = i


# palindrome or not using iterative method.
num=int(input("enter the number for palindrom"))
temp=0
rev=1
while temp !=0:
    rev=rev*10+temp%10
    temp=temp//10
if rev==num:
    print("It id the palindrom")
else:
    print("It is not palindrom")

# greatest among three integers.
a=int(input("enter the greater  numebr "))
b=int(input("enter the greater numebr"))
c=int(input("enter the  greater numebr"))
if(a>b and a>c):
    print("A is the greater number")
elif(b>c):
    print("B is the greater number")
else:
    print("C is the greater number")
    
    
# check a number is binary
num=int(input("enter greater then zero for binary number  "))
while(num>0):
    i=num%10
    if i !=0 and i !=1:
        print("it is  not a binary number")
        break;
    else:
        num = num // 10
        if num==0 or num==1:
            print("it is a binary number")


#sum of digits of number using recursion
num1=int(input("enter the sum of digits number"))
sum=0
#for i in range(0, num1):
for i in range (len(str(num1))):
#while num1>0:
    digit =num1 %10
    sum=sum+digit
    num1=num1//10
print(sum)


# add two number without using arithmetic operator
def add(x,y):
    for i in range(1,y+1):
        x=x+1
    return x
x=int(input("enter the first number for sum"))
y=int(input("enter the second number for sum"))
x=add(x,y)
print(x)


#Average of numbers
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
num3 = int(input("enter the third number"))
num4 = int(input("enter the four number"))
num5 = int(input("enter the five number"))
num6 = int(input("enter the six number"))
num7 = int(input("enter the seven number"))
sum=0
sum=num1+num2+num3+num4+num5+num6+num7
avg=sum//7
print(avg)


# even /odd number 
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
if (num1==num2):
    print("both number are equal ")
elif (num1 % 2 ==0  and num2 % 2 ==0):
    print("it is even number")
else:
    print("It is odd number")
sum=0
sum=sum+num1+num2
if (sum % 2 ==0):
    print("even number")
else:
    print("ood number")


# smallest number among three
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
num3 = int(input("enter the third number"))
if(num1<num2):
    if(num1<num3):
        print("num1 is the smaller number ")
    else:
        print("num3 is the smaller")
else:
    if(num2<num3):
        print("num2 is the smaller number ")

    else:
        print("num3 is the smaller number")


# first n prime number with explanation
num=int(input("enter the number for prime number"))
for i in range(1,num):
    for r in range(2,i):
        if (r%i ==0):
            print("it is prime number")
            break
        else:
            print("it is not prime number")
            
            
# checking leap year and not
def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0:
        print("leap year")
    elif year % 400 == 0:
        print("leap year")
    else:
        print("not leap year")
    return leap
year = int(input("enter the current year"))
print(is_leap(year))


#calculate the power using the poew method 
base = int(input("please enter a number : "))
exponent = int(input("please enter a number: "))
print(pow(base,exponent))


# calculate  the cube of given number
num= int(input("enter the number for cube "))
cube=num*num*num
print(cube)


# LCM  of given two number
def lcm(a,b):
    m=(a*b)
    while a!=0 and b !=0:
        if a>b:
            a%=b
        else:
            b %=a
    return m/(a+b)
x = int(input("enter the number for lcm"))
y= int(input("enter the number for lcm"))
print("Lcm",lcm(x,y))


#square root
num=int(input("enter the number for square root"))
if(num== 0):
    print("it is the homogenstion")
a=int(input("enter  the number "))
b=int(input("enter  the number "))
c=int(input("enter  the number "))
if(num!=0):
       square_root=((b*b+(4*a*c-b*b)/2)/2*a) and  ((b*b-(4*a*c-b*b)/2)/2*a)
       print(square_root)
       
       
# calculate Simple Interest
p=int(input("enter initial principal balance  number  "))
r=int (input("enter  the annual interest rate number "))
t=int(input("enter  the time( in years)"))
simple_interest = (p * r * t) / 100
print(simple_interest)


#calculate simple interest using function
def si(p,r,t):
    si=(p*r*t)/100
    print("the simple interest is :", si)
    return si
p=int(input("enter initial principal balance  number  "))
r=int (input("enter  the annual interest rate number "))
t=int(input("enter  the time( in years)"))
si(p,r,t)


# Remove given character from string
s1 = input("please enter a string : ")
s2= input("please enter a character : ")
print(s1.replace(s2," ")) #replace character


# Remove given character from string using function:
def remove_char(s1,s2): #translate remove character
    dict={ord(s2):None}
    print(s1.translate(dict))
s1 = input("please enter a string : ")
s2 = input("please enter a character : ")
remove_char(s1,s2)


# Calculate the power without using POW function
s1 = int(input("please enter a base number : "))
s2= int(input("please enter a exponent number : "))
result=1;
#for s2 in range(s2,0,-1):  #if you taking for or while loop.
while s2!=0:
    result *=s1
    s2=s2-1
print(result)


#power function using function
def power(x,y):
    if(y==0):
        return 1
    elif(int(y%2)==0):
        return (power(x,int(y/2)))*(power(x,int(y/2)))
    else:
        return(x*(power(x,int(y/2)))*(power(x,int(y/2))))
x=int(input("enter the number "))
y=int(input("enter the number "))
print(power(x,y))


# cube using function:
def cube(x,y):
    if(y==0):
        return 1
    elif(int(y%2)==0):
        return (cube(x,int(y/2)))*(cube(x,int(y/2)))
    else:
        return(x*(cube(x,int(y/2)))*(cube(x,int(y/2))))
x=int(input("enter the number "))
y=int(input("enter the number "))
print(cube(x,y))


# count occurrence of a character in string using for loop:
string=input("enter the string")
char=input("enter the which is find character")
count=0
for i in range(len(string)):
    if(string[i]==char):
        count=count+1
        print(count)
    else:
      print("not available character in string")
print("total number of occurence of",char, "is:",count)
#count occurrence of a character in string using while loop:
string=input("enter the string")
char=input("enter the which is find character")
index=0
count=0
while(index<len(string)):
    if(string[index]==char):
        count=count+1
    index=index+1
print("total number of occurence of",char,"is:",count)


# count occurrence of a character in string using method:
def count_occ(char,string):
    count=0
    for i in range(len(string)):
        if(string[i]==char):
            count=count+1
    return count
string=input("enter the string ")
char=input("enter the which is find character")
count=count_occ(char,string)
print(count)

# both the strings are anagrams(one word to creeat another word eg:dad->add)
def anagcheck(str1,str2):
    if (sorted(str1) == sorted(str2)):
        return True
    else:
        return False
str1=input("enter the first string ")
str2=input("enter the another string")
if anagcheck(str1,str2):
    print("string are anagram")
else:
    print("string are not anagram")


# check given character is vowel or consonant
x=input("enter the character:")
if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U'):
    print("given character is vowel")
else:
    print("given character is consonant")


# check given character is digit or not
x=input("enter the character:")
if(x>='0' and x<='9'):
    print("given character",x,"is a Digit")
else:
    print("given character",x,"is not a Digit")


# replace the string spacwe with a given character
string=input("enter the string ")
ch=input("enter the character")
result=" "
for i in string:
    if i== " ":
        i=ch
    result +=i
print(result)


# replace the string spacwe with a given character using method
def rep_spc(string,ch):
    for i in string:
        result = " "
        if i==" ":
            i=ch
        result += i
string=input("enter the string")
ch=input("enter the character")
rep_spc(string,ch)
print("string after removing space with =",rep_spc)

#hacker rank  if -else problem solving
n=int(input("enter the number").strip())
if n %2 == 0:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    elif n>20:
        print("Not Weird")
    else:
        print("Weird")
else:
    print("Weird")

#hacker rank loops:
n = int(input("enter the number square"))
for i in range(0,n):
    i=i*i
    print(i)
    
    
# hackerrank print function
n = int(input("enter the number for print function"))
for i in range(0,n+1):
    print(i ,end=" ")
 
    
# hackerrank list compostition.
x = int(input("enter the number for x"))
y = int(input("enter the number for y"))
z = int(input("enter the number for z"))
n = int(input("enter the number "))
for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k !=n:
                    print([i,j,k],end="")
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n ])


# hacker Rank finding the percentage problem solving

n = int(input("enter the input number"))
student_marks = {}
for _ in range(n):
    name, *line = input("enter the name of student in list ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("enter name query_name")
sum=0
for i in student_marks[query_name]:
    sum=sum+i
print("{0:.2f}".format(sum/3))

# hacker rank find the runner up score.

if __name__ == '__main__':
    n = int(input("enter the number list for max"))
    arr =list(map(int, input("enter the runnefrup score").split()))
    arr.sort()
    a=arr[(arr.index(max(arr)))-1]
    print(a)

# hacker rank of nested lists

a=[]
for _ in range (int(input("enter the number of nested lists"))):
    name=input("enter the name ")
    score=float(input("enter the score"))
    a.append([score,name])
a.sort()
b = [i for i in a
     if i[0] != a[0][0]]
c = [j for j in b
if j[0] == b[0][0]]
c.sort(key=lambda x:x[1])
for i in range(len(c)):
    print(c[i][1])
    
#linked list node creat

class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.head = None
        self.tail = None
        self.count = 0
    def iterate_item(self):
        # Iterate the list.
        current_item = self.head
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val
    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1
items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')
for val in items.iterate_item():
    print(val)
print("\nhead.data: ",items.head.data)
print("tail.data: ",items.tail.data)

#diaplay array list

from  array import *
array_num= array('i',[1,2,3,4,5])
for i in array_num:
    print(i)

# list questions

class clacult:
    def sum_list(item):
        sum_num=0
        for i in item:
            sum_num +=i
        return sum_num
    print(sum_list([7,8,6,4]))
    def max_list(list):
        max=list[0]
        for i in list:
            if i>max:
                max=i
        return max
    print(max_list([7,8,6,4,9]))
    def min_list(list):
        min=list[1]
        for i in list:
            if i<min:
                min=i
        return min
    print(min_list([7, 8, 6, 4]))
    def match_words(words):
        crs=0
        for word in words:
            if len(word)>1 and word[0]==word[-1]:
                crs +=1
        return crs
    print(match_words(['121','shh','sss','sas','dssd','ddd']))
    def sort_list(tuple):
        def last(n):
            return n[-1]
        return sorted (tuple,key=last)

    print(sort_list([(7,8),(6,4),(4,5),(2,5),(7,6),(1,3)]))
    def item_list(items):
        dup_list=set()
        un_item =[]
        for i in items:
            if i not in dup_list:
                un_item.append(i)
                dup_list.add(i)
        print(dup_list)
    item_list=item_list([2,3,4,5,4,5,5,3,5,6,6,7,7,2,3,3,3,3,9,9])
    
def rev_list(items):
    items.list()
    return items
items =input("enter the number")
print(rev_list(items))

friends=["ram", "mohan", "lal", "sohan", "raj", "hostal", "mote", "hari"]
for friend in friends[0:1]:
    print(friends)
print(friends[1:4])

s=input("enter the string")
u1=set()
u2=set()
vol='AEIOU'
print(s)
for i in range(len(s)):
    if s[i] in vol:
        for k in range(len(s[i:])):
            print(i,s[i:i+k+1])
            u1.add(s[i:i+k+1])
    else:
        for l in range(len(s[i:])):
            print(i,s[i:i+l+1])
            u2.add(s[i:i+l+1])

#hacker rank text alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input("enter the text Alignment number")) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


num = int(input())

lis = list(map(int,input().split()))

result = 0

element = 0

negative=0

for i in range(0,len(lis)):

  if(result+lis[i]>=result ):

      result += lis[i]

      element += 1

  elif(result+lis[i]<result):

      negative += 1

if(negative == len(lis)):

  print(max(lis),1)

else:

  print(result, element)
  
# Arrays of reverse in hackerrank ;

def revarray(a):
    res=[]
    for i in range(len(a)-1,-1,-1):
        res.append(a[i])
    print(res)
a=[int(x) for x in (input("enter the number").split())]
revarray(a)

# Library fees
def libaryfine (d1,m1,y1,d2,m2,y2):
    total =0
    if y1>y2:
        total =total + 10000
    elif y1==y2 and m1>m2:
        total = total + 500 * (m1-m2)
    elif y1== y2 and m1==m2 and d1>d2:
        total = total +15 * (d1-d2)
    else:
        print("Book return on the time and  due date\n")

    print("\n library book return charge ",+total)
    print(total)
due_date= input("enter the due date books ").rstrip().split()
d1 = int(due_date[0])
m1 = int(due_date[1])
y1 = int(due_date[2])
return_date= input("enter the return date books").rstrip().split()
d2 = int(return_date[0])
m2 = int(return_date[1])
y2 = int(return_date[2])

result=libaryfine(d1,m1,y1,d2,m2,y2)

def utopiantree():
    height=1
    n=int(input("enter the number"))
    for i in range(1,n+1):
        if i%2!=0:
         height=height*2
        else:
            height +=1
    print(height)
testcases=int(input("enter the number"))
for _ in range(testcases):
    utopiantree()

n=input()
print(n[0])
print(n[5])

x=int(input())
rem=0
while(x>0):
    rem=x%10
    x=x//10
print(rem)

n=int(input())
for i in range(n):
    for j in range(i):
        print("*",end='')
    print()
 
#resver the patterns
n=int(input())
k=2*n-2
for i in range(n):
    for j in range(k):
        print(end=" ")
    k=k-2
    for j in range(i+1):
        print("*",end=" ")
    print()
#tringles patterns

n=int(input())
k=n-1
for i in range(n):
    for j in range(k):
        print(end=" ")
    k=k-1
    for j in range(i+1):
        print("* ",end=" ")
    print()
#v paterns design
    
ch=input()
spaces=8
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(1,spaces):
        print(end=" ")
    spaces=spaces-2
    for j in range(i,0,-1):
        print(j ,end=" ")
    print()

 #patterns
n=int(input())
while(n<=10):
    print(n * " * ")
    n=n+1
    
n=int(input())
for i in range(n):
    print(i*"*")
    i=i+9

#clock and angle
t=int(input())
while(t>0):
  h,m=map(int,input().split())
  h=h*(360//12)+(m*360)//(12*60)
  m=m*(360//60)
  ang=abs(h-m)
  if(360-ang):
      print(ang)
  else:
    ang=(180-ang)
    print(ang)
  t=t-1
  
#second smallest number
l=[]
for i in range(0,3):
    l.append(int(input()))
l.sort()
print(l[1])

#operater of smaller and greater
X,Y=input().split()
X=int(X)
Y=int(Y)
if(X>Y):
   print("{} is greater to {} ".format(X,Y))
elif(X<Y):
     print("{} is smaller than {}".format(X,Y))
else:
    print("{} is equal than {}".format(X,Y))

T=int(input())
while(T!=0):
  q,p= input().split()
  #p = int(input())
  q = int(q)
  p = int(p)
  #total = double(total)
  #final = double(final)


  total=q*p
  if(q>100):
    final=(total*20)/100
    print(total-final)
  else:
    print(total)
T=T-1


#class and object method....

class First():

    def __init__(self, n):
        self.n = n

    def forLoop(self):
        arr = []
        for i in range(self.n):
            arr.append(i)
        return arr

    def isEven(self):
        if (self.n % 2 == 0):
            return True
        else:
            return False

    def isOdd(self):
        if (self.n % 2 != 0):
            return True
        else:
            return False

    def whileLoop(self):
        arr = []
        while (self.n != 0):
            arr.append(self.n)
            self.n = self.n - 1
        return arr

    def whileLoopResv(self, n):  # n = 1
        arr = []
        i = 0
        while (n > i):  # n = 1, i = 1
            arr.append(i)
            i = i + 1
        return arr

n = int(input())
firstObj = First(15)
print(firstObj)
temp = firstObj.forLoop()
isEvenResult = firstObj.isEven()
isOddResult = firstObj.isOdd()
whileResv = firstObj.whileLoop()
whileResult = firstObj.whileLoopResv(n)

print(temp)
print(isEvenResult)
print(isOddResult)
print(whileResv)
print(whileResult)


#class and function example:-

class Mobile:

    def __init__(self,brandName,color,isJack):
        self.brandName = brandName
        self.color = color
        self.isJack = isJack
        
    def calling(self):
        print("call  Calling")
        
    def cameraClick(self):
        print("click picture captured")
        
    def message(self):
        print("message sent")

def main():

    m1 = Mobile("Apple 11s pro", "moon light","False")
    print(m1.brandName)
    print(m1.color)
    print(m1.isJack)
    m1.calling()
    m1.message()
    m1.cameraClick()
    print("===============================")
    m2 = Mobile("redmi 11s pro", "green","True")
    print(m2.brandName)
    print(m2.color)
    print(m2.isJack)

if __name__== '__main__':
    main()

# type of function .....

def addtion(): # no argument , no return value
    x , y = map(int,input().split())
    print(x + y)

def swap(a,b): # taking argument , no return value
    temp = a
    a = b
    b = temp
    print(a,b)

def swapResult(a,b): # class 'list' using swap element
    print(type(a),type(b))
    temp = a[0]
    a[0] = b[0]
    b[0] = temp
    print(a[0],b[0])

def detaType(): # no argument , no return value
    return "Datatype"

def isEven(a,b): # taking  argument , return value
    if(a % 2 == 0 or b % 2 == 0):
        return True
    else:
        return False

def main():
    a, b = map(int, input().split())
    addtion()
    swap(a,b)
    x = [0] * 1
    y = [0] * 1
    x[0] = a
    y[0] = b
    swapResult(x,y)
    detaResult = detaType()
    isEvenResult = isEven(a,b)
    print(type(detaResult))
    print(isEvenResult)
        
if __name__== '__main__':
    main()
    

#instance and class variable.......

class mobile:
    wireless = True #class variable...
    year = 2022 #class variable..

    def __init__(self,bN,color,isJack):
        self.brandName = bN
        self.color = color
        self.isJack = isJack

    def calling(self):
       print("calling")

    def cameraClick(self):
       print("photo & videos create")

    def message(self):
        print("message Sent")

def main():
    m1 = mobile("Apple","white",False)
    m1.calling()
    m1.cameraClick()
    m1.message()
    m1.screen="LED" #instance variable
    mobile.year=2022 #value change
    mobile.brandName = "samsung" #no argument change in main function
    print(m1.brandName)
    print(m1.color)
    print(m1.message)
    print(m1.screen)
    print(m1.year)
    print("m1.wireless")

    print("========================================")
    m2 = mobile("onePlus","Bule",True)
    print(m2.brandName)
    print(m2.color)
    print(m2.isJack)
    print(m2.year)
    print(m2.wireless)

if __name__=='__main__':
    main()

#inheritance concept
class Car():
    def __init__(self,gears,seats,maxSpeed):
        self.gears = gears
        self.seats = seats
        self.maxSpeed = maxSpeed

    def speedup(self):
        print("speed increasing")

    def apply_break(self):
        print("speed Decreasing")

    def movement(self): # methods overriding
        print("Car moves back and forth")

class Hyundai:
    def __init__(self):
        self.brandName = "Hyundai"

class Harrier(Car): #inheritance of Hyundai property

    def __init__(self,mileage,gears,seats,maxSpeed): #  inheritance the init word and some property adding with previous init are same.
        self.mileage = mileage
        super().__init__( gears, seats,maxSpeed)  # excessing of a super class method

    def race_mode(self):
        print("Race mode is on")

class Verna(Harrier): #inheritance of  harrier

    pass    #inherit the properties and methods

    def jumpMode(self):
         print("Jumping the car ")

class Pal_V(Car):
    pass
    def movement(self): # overriding method
        print("Car moves back and forth , up and down. ")

# object create

c1 = Car(4,12,129)
h1 = Harrier(20, 5, 4, 240)
v1 = Verna(15,5,4,180)
p1 = Pal_V(5,4,300)
h2 = Hyundai()

# function call

h1.speedup()
h1.apply_break()
h1.race_mode()

v1.speedup()
v1.race_mode()
v1.jumpMode()

p1.movement()

# display function
print(h2.brandName)

print(h1.mileage)
print(h1.gears)
print(h1.seats)
print(h1.maxSpeed)

print(v1.mileage)
print(v1.gears)
print(v1.seats)
print(v1.maxSpeed)


# Multiple inheritance

class Father:
    def __init__(self):
        super().__init__()      #calling parent claas constructor
        print("father Class Constructor")
    def showf(self):
        print("Father class method")

class Mother:
    def __init__(self):
        super().__init__()       #calling parent class constructor
        print("Mother Class Constructor")
    def showM(self):
        print("Mother Class Method")

class Son(Mother,Father):
    def __init__(self):
        super().__init__()       #calling parent class constructor
        print("Son Class Constructor")
    def ShowS(self):
        print("Son Class Method")

s = Son()
s.ShowS()
s.showf()
s.showM()

# Access Modifier
class Account:
    _amount = 0 #protected _amount
    def deposit(self,add):
        self._amount += add

    def debit(self,sub):
         self._amount -= sub

    def printAmount(self): #print amount Calling
         print(self._amount)

class User(Account):
    def calclateTax(self): # user account call and calculate tax
        tax = self._amount * 0.2
        print(tax)
u1 = User()
u1.deposit(100)
u1.printAmount()
u1.debit(50)
u1.printAmount()
u1.calclateTax()


# polymorphism Concept

class trueCaller():
    def call(self):
        print("Ringing")
        print("Caller data")

class jioCaller():
    def call(self):
        print("Calling")

class Phone:
    def callFun(self, phoneApp):
        phoneApp.call()

phoneApp = jioCaller()
phoneApp = trueCaller()
p1 = Phone()
p1.callFun(phoneApp)


#operator overloading

class Student:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other): # called by + operator
        ans1 = self.x + other.x
        ans2 = self.y + other.y

        #return (ans1 + ans2)
       # return ans1,ans2
        return '{} {}'.format(ans1,ans2)

    def __lt__(self,other):
        ans1 = self.x + self.y
        ans2 = other.x + other.y
        if(ans1 < ans2):
            return True

        else:
            return False

s1 = Student(10,30)
s2 = Student(50,15)
s3 = s1 + s2 # this + operator calling of add function
#s3 = Student.__add__(s1,s2) #same both calling add function call
print(s3)
if(s1 < s2):
    print("s1 is smaller")

else:
    print("s2 is smaller")

"""












