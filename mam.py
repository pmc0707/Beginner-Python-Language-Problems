# a=10
# b=20
# print(a,b,sep=',')

# string

# a=(input("enter the number"))
# b=(input("enter the sec number"))
# print("sum of a and b is :",a+b)

# #input by using int

# a=int(input("enter the number"))
# b=int(input("enter the sec number"))
# print("sum of a and b is :",a+b)
# r=float(input("radius of cirlce"))
# a=3.14*r*r
# print("area of circle is :",a)
# x=y=z=20
# print(x,y,z)
# print(x)

# x=y=z=int(input("enter the number"))
# print(y)
# a=int(input("a="))
# b=int(input("b="))
# a,b=b,a
# print("after swapping a=",a)
# print("after swapping b=",b)
# a=int(input())
# if(a%3==0 and a%7==0):
#     print("number is divisible by both")
# elif(a%3==0):
#       print("divisible by 3")
# elif(a%7==0):
#     print("by 7")
# else:
#     print("not divisible by 7 and 3")
# a=int(input("enter the starting point"))
# b=int(input("enter the mid point"))
# c=int(input("enter the end point"))
# for i in range(b,a-1,-c):
#     print(i,end=' ')
# a=int(input("enter the starting point"))
# b=int(input("enter the stopping point"))
# c=int(input("enter the jump point"))
# for i in range(a,b+1,c):
#     print(i)
# for p in range(b,a-1,-c):
#     print(p)
# for k in range(a,b+1,c):
#     print(k,end=" ")
# for j in range(b,a-1,-c,):
#     print(j,end=" ")
#WAP to print increment decrement by the user & vertically as well as horizontally by user.
# a=int(input("enter the starting point"))
# b=int(input("enter the stopping point"))
# c=int(input("enter the jump point"))
# d=int(input("enter the user 1/2/3/4 :"))
# verticalincrement=1
# verticaldecrement=2
# horizontalincrement=3
# horizontaldecrement=4
# if(1==d):
#     for i in range(a,b+1,c):
#         print(i)
# elif(2==d):
#     for j in range(b,a-1,-c):
#         print(j)
# elif(3==d):
#     for p in range(a,b+1,c):
#         print(p,end=" ")
# elif(4==d):
#     for k in range(b,a-1,-c):
#         print(k,end=" ")               
# else:
#     print("invalid user i'd") 
# s="section u lab"
# s1=s[::-1]
# print(s1)
# s2=s[-2::-1]
# print(s2)
# s3=s[3::-1]
# print(s3)
# s4=s[3:-2:1]
# print(s4)
# s5=s[3:-2:-1]
# print(s5)
# s6=s[:50:1]
# print(s6)
# s7=s[-1:-40:-1]
# print(s7)
# p='Hello world'
# p.count('l',5)
# print()
# p.find('e')
# s='hello world'
# print(s.rstrip('d'))
# print(s.split())
# print(s.isupper())
# print(" ".join(s))
# l=[1,2,'hello','class']
# l.append('o')
# print(l)
# l.append([10,120])
# print(l)
# #extend
# l.extend(['hy','ji'])
# print(l)
# l.pop(2)
# print(l)
# l.insert(2,"boy")
# print(l)
# l.clear()
# print(l)
# l1=list(l)
# print(l1)
# n=int(input("enter the number"))
# for i in range(n,0,-1):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()
# i=5
# a=0
# for i in range(1,i+1):
#     print(i*"*"+a*" "+i*"*")
# def tol():
#     global a
#     a=50
#     print("insisde function call ",a)
# a=70
# print("before function call",a)
# tol()
# print("after function call",a)    

#no local is keyword which is used to notify outer function variable value with inner function value
#outer function must be return that variable.
# def display():
#     a=100
#     print("in function",a)
#     def D1():
#         nonlocal a
#         a=70
#         print("non loacal function",a)
#     D1()
#     return a
# a=4
# print("B.F",a)
# print(display())    
# import math
# print(math.sqrt(4))
# import calendar
# print(calendar.month(2003,4))
# import keyword
# print(keyword.kwlist)
#USER DEFINE: which is define by user with in a file and that file which is used by import keyword with the name of file
# def display(name,rollno):
#     print("hello",name,rollno)
# def greet(name):
#     print('GM',name)
# def add(a,b):
#     c= a + b
#     print(c)
#**FROM keyword is used used to import soe fumnction to that particular file
# import random
# # print(random.random())
# print(random.randrange(4,50))
# print(random.randrange(4,50,10))
# print(random.randrange(445,50))
# comp=random.randrange(1,101)
# user=int(input("enter the number"))
# if(user>comp):
#     print('no is too high')
#     print('comp number is :',comp)
# elif(user<comp):
#     print('no is too low')
# else:
#     print('on gusseed')
# import math as m
# print(m.pi)
# print(m.e)
# print(m.sqrt(4))
# print(m.ceil(19.5))
# print(m.floor(19.6))
# print(m.pow(2,4))#power function generate floarting number and only two argumaent must be pass.
# #diff b/w math.pow and pow?
# print(m.degrees(30))
# print(m.radians(1718.8733853924696))
# print(m.sin(90))
# f=open("C:\\Users\\lenovo\\Desktop\\u\\abc.txt","a+")
# print(f.write("file handling example\n python"))
# f.seek(1)
# print(f.read())
# print(f.tell())
# f.close()
# f=open("C:\\Users\\lenovo\\Desktop\\u\\sum.txt","a")
# a= int(input("enter the number"))
# b=int(input("enter the number"))
# c=a+b
# f.write("first number"+str(a))
# f.write("\tfirst second"+str(b))
# f.write("\t addition="+str(c))

# f.close()
# f=open(r"C:\Users\lenovo\Desktop\u\1.JPG","br")
# print(f.read())
