f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que2.txt","r")
str=f.read()
word=str.split()
max_len=len(max(word,key=len))
for word in word:
    if len(word)==max_len:
        long_word=word
print(long_word)