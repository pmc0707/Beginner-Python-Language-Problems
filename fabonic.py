 #Q.1:Python Program for n-th Fibonacci number
# n=int(input("enter the number"))
# fact=1
# while(n>=1):
#     fact*=n
#     n-=1
#     print( "Factorial of %d is %d%d",(n,fact))
# Q.2: Python Program for How to check if a given number is Fibonacci number?
# n=int(input("enter the number :"))
# fact=1
# if(n>=1):
#     fact*=n
#     n-=1
#     print("number is fabonaic ")
# else:
#     print("number is not in fabonaic")
# Q4. WAP  for sum of square of first n natural numbers.
x=int(input("enter the number"))
y=int(input("enter the number"))
xyz=0
pqr=0
for i in range(x,y+1):
    xyz=xyz + (i**2)
    print(xyz)
print()
# Q.14: Write a Python program to find first and last digit of a number.
ls=[45,65,52,57,96,69]
a=ls[0],ls[5]
print(a)