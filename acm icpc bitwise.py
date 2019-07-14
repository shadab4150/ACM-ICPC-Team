n,m=[int(x) for x in input().split()]
 
arr=[]

for i  in range(n):
    arr.append(int(input(),2))
arr2=[]
for i in range(n):
    for j in range(i+1,n):
        num=arr[i] | arr[j]
        dat=bin(num)
        dat=dat[2:]
        count=dat.count('1')
        arr2.append(count)
max_topics=max(arr2)
print(max_topics)

print(arr2.count(max_topics))       

        