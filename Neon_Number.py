N=int(input())
s=N*N
sum=0
while(s>0):
    sum=sum+s%10
    s=s//10
if(N==sum):
    print("Neon Number")
else:
    print("Not Neon Number")