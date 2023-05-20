from collections import Counter
f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que2.txt","r")
s=Counter(f.readline())
print(s)
f.close()