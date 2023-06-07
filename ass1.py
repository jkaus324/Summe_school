import random
L = [5,2,-2,-5]
k =0
a = 0
ans = []
for z in range(0,len(L)):
    for i in range(0,20):
        a = 0
        temp = []
        b = random.sample(L,z+1)
        for j in range(0,len(b)):
            a=a+b[j]
        if a>=0 and a<=2:
            k=k+1
            b.sort()
            if b in ans:
                k=k-1
            else:
                ans.append(b)

print(k)
print(ans)