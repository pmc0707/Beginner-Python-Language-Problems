# # # n=int(input())
# # # for i in range(0,n):
# # # #     print(i**2)
# # # ls=list(map(float,input().split()))
# # # ave=print(sum(ls)/len(ls))
# # # ls=tuple(map(int,input().split()))
# # # for i in range(ls):
# # '''n=int(input())
# # if (n%2==0):
# #    if(n>2 and n<5):
# #     print("Not Weird")
# # elif(n>6 and n<20):
# #     print("Weird")
# # elif(n>20):
# #     print("Not Weird")
# # else:
# #     print("Weird")
# #         '''
# # ''' 
# # import math
# # n=3.7
# # print(float(math.floor(3.7)))
# # print(float(math.ceil(3.7)))
# # import math
# # print(dir(math))'''
# # a=int(input("enter the fibonacci number"))
# # fibe=0
# # while(a>=0):
# #   fibe+=a
# # print("fabinancci number of %d is %d"%(a,fibe))
# # a=int(input())
# # b=int(input())
# # c=int(input())
# # for i in range(a,b+1,c):
# #     print(i)
    

# # s=input("enter a string")
# # a=input("enter your choice")
# # if(a=='count'):
# #     print(s.count())
# # elif(a=='lower'):
# #     print(s.lower())
# # elif(a=='upper'):
# #     print(s.upper())
# # elif(a=='find'):
# #     x=input("Enter another string:")
# #     print(s.find(x))
# # elif(a=='index'):
# #     x=input("Enter another string:")
# #     print(s.index(x))
# # elif(a=='strip'):
# #     x=input("Enter another string:")
# #     print(s.strip())
# # elif(a=='replace'):
# #     x=input("Enter another string:")
# #     print(s.replace(x))
# # elif(a=='title'):
# #     print(s.title())
# # elif(a=='capitalize'):
# #     print(s.capitalize())
# # elif(a=='swapcase'):
# #     print(s.swapcase())
# # elif(a=='ljust'):
# #     print(s.ljust())
# # elif(a=='center'):
# #     print(s.center())
# # elif(a=='isdigit'):
# #     print(s.isdigit())
# # elif(a=='isalnum'):
# #     print(s.isalnum())
# # elif(a=='split'):
# #     print(s.split())
# # elif a=='join':
# #     x=input("Enter another string:")
# #     print(s.join(x))
# # else:
# #     print('wrong input')
    
 
# a= int(input("enter the number"))
# x=0
# y=1
# z=0
# while(z<=a):
#     z=x+y
#     x=y
#     y=z
# if(z>=a):
#     print("this isn")
# else:
#     print("no") 
# n=int(input("entr the number"))
# sum=0
# power=len(str(n))
# while n>0:
#     rem=n%10
#     sum+=rem**power
#     n=n//10
# if(sum==n):
#     print("Armstrong")
# else:
#     print("not arm")
# s='hello_class'
# sl=s[::3]
# print(sl)
# sl=s[-2::-1]
# print(sl)
# sl=s[-2:3:-2]
# print(sl)
# sl=s[3::-1]
# print(sl)
# sl=s[3:1:-1]
# print(sl)
# sl=s[3:-2:-1]
# print(sl)
# sl=s[-4:2:1]
# print(sl)
# sl=s[::-2]
# print(sl)
# sl=s[:9:1]
# print(sl)
# m=5
# for i in range (1,m+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()
n=int(input("enter the number"))
for i in range(n):
    for j in range(i,n):
        print("*",end=' ')
    print()