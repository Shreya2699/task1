a=int(input("enter the number of terms till which u want to print the fibonacci series"))
t1=0
t2=1
i=0
while i<a:
    print(t1)
    s=t1+t2
    t1=t2
    t2=s
    i=i+1
num=int(input("enter a number to check if its fibonacci"))
import math
def pef(n):
    k=int(math.sqrt(n))
    if pow(k,2)==n:
        return True
    else:
        return False
def fib(n):
    r1=5*n*n+4
    r2=5*n*n-4
    if pef(r1) or pef(r2):
        return True
    else:
        return False
if fib(num)   :
    print("yes",num,"is fibonacci")
else:
    print("no",num,"is not fibonacci")













