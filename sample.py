n=int(input())
list=[]
for i in range(0,n):
    l=int(input())
    if(l%2==0):
        list.append(l)
print("Final list : ",list)
