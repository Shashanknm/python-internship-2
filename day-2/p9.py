a=[4,2,3,0,0,1,0,0,0,1]
i=3
j=2
k=0

c_0=0
c_1=0
c_2=0

for i in range(len(a)):
    if a[i]==0:
        c_0 +=1
    elif a[i]==1:
        c_1 +=1
    else:
        c_2 +=1

j=0

while c_0>0:
    a[j]=0
    j=j+1 
    c_0=c_0-1
    

while c_1>0:
    a[j]=1
    j=j+1 
    c_1-=1
    
    
while c_2>0:
    a[j]=2
    j=j+1 
    c_2-=1
    
print(a)
    