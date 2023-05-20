# f=open(r"C:\Users\lenovo\OneDrive\Desktop\lab\lab01.txt","w+")
# f.write("hello python programming lab")
# f.seek(1)
# # print(f.read())
# print(f.tell())
# f.close()
# import pickle
# f=open(r"C:\Users\lenovo\OneDrive\Desktop\lab\lab01.txt","br")
# # l=[1,2,3,4,"Hello"]
# # pickle.dump(l,f)
# # f.close()
# s=pickle.load(f)
# print(s)
# f.close()

import pickle
f=open(r"C:\Users\lenovo\OneDrive\Desktop\lab\lab01.txt","br")
s=pickle.load(f)
print(s)
with open(r"C:\Users\lenovo\OneDrive\Desktop\lab\ab.txt","w")as f:
    f.write("Last Lab")