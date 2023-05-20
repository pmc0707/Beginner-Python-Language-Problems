#Q.1
# f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que1.txt","w+")
# f.write("hy Ma'am how are you\nare you fine")
# f.close()
#Q.2

# f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que2.txt","a")
# f.write("hy Ma'am how are you\n im fine ")
# f.readline()
# f.close()
#Q.3
# f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que2.txt","a")
# a=input("enter here : ")
# f.write(a)
# f.close()
#Q.4

# f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que3.txt","a")
# f.write("hy Ma'am how are you\n im fine ")
# s=f.readline
# print(s)
# f.close()
#Q.5
# f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que4.txt","r")
# comtent_list=f.readlines()
# print(comtent_list)
# comtent_list=[x.strip() for x in comtent_list]
# print(comtent_list)
# f.close()
#Q.6
# f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que4.txt","r")
# f.read()
# f.close()
#Q.7
# testsite_array = []
# with open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que4.txt") as my_file:
#     for line in my_file:
#         testsite_array.append(line)

#Q8
# f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que2.txt","r")
# str=f.read()
# word=str.split()
# max_len=len(max(word,key=len))
# for word in word:
#     if len(word)==max_len:
#         long_word=word
# print(long_word)
#Q.9
# f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que2.txt","r")
# s=len(f.readlines())
# print(s)
#f.close()
#Q.10
# from collections import Counter
# f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que2.txt","r")
# s=Counter(f.readline())
# print(s)
# f.close()
#Q>11
# import os
# file_size = os.path.getsize(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que2.txt")
# print("File Size is :", file_size, "bytes")
# list of names
#Q.12
# names = ['radhe', 'shyam', 'kanha']

# with open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que7.txt", 'w') as fp:
#     fp.write('\n'.join(names))
#Q.13
# import shutil
# shutil.copyfile(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que2.txt",r"C:\Users\lenovo\OneDrive\Desktop\github_py\que8.txt")

#Q.15
# import random
# f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que1.txt","r")
# lines = open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que1.txt","r").read().splitlines()
# print(lines)
#Q.16
# f = (r"C:\Users\lenovo\OneDrive\Desktop\github_py\que1.txt")
# file = open(f)
# if not file.closed:
#     file.close()
#Q.17
#f = open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que1.txt","w+")
# s=repr(f.read())
# f.write("i'm a boy")
# print(s)
# f.close()