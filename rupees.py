n=int(input())
r=n-100
t=r//2000
r%=2000
f=r//500
r%=500
o=r//100
print(f'''Hundred:{o+1} 
Five hundred:{f}  
Two thousand:{t}''')