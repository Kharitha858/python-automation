n=[1,2,3,4,5,6,7,8,9,10]
# op:[3,4,5,6,7]
res=[]
for i in range(len(n)):
    if 3<=n[i] and 7>=n[i]:
        res+=[n[i]]
print(res)