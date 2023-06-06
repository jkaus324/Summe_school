import random
L = [5,2,-2,-5]
k =0
a = 0
ans = []
for i in range(0,20):
    a = 0
    temp = []
    b = random.sample(L,2)
    for j in range(0,len(b)):
        a=a+b[j]
    if a==0:
        k=k+1
        if b in ans:
            k=k-1
        else:
            ans.append(b)

print(k)
