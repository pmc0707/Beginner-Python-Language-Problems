f=open(r"C:\Users\lenovo\OneDrive\Desktop\github_py\que4.txt","r")
comtent_list=f.readlines()
print(comtent_list)
comtent_list=[x.strip() for x in comtent_list]
print(comtent_list)
f.close()