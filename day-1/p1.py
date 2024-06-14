#armstrong number
n=int(input())
n1=n
org=n
ans=0
count=0
while n>0:
    count=count+1
    n=n//10
while n1>0:
    digit=n1%10
    p=digit**count
    ans=ans+p
    n1=n1//10
if ans==org:
    print("arm")
else:
    print("no")
    
     
