n=int(input())
sqr=pow(n,2)
mod=pow(10,len(str(n)))
if sqr%mod==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")