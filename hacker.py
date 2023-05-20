# a= [2,3,6,6,5]
# b=list(set(a))
# b.sort(reverse=True)
# c=b[1]
# print(c)

n=int(input())
ls=[]
for i in range(n):
    x=list(input().split())
    ls.append(x)
d={}
d={i[0]:[int(i[1]),int(i[2]),int(i[3])] for i in ls}
q=input()
s=sum(d[q])/3