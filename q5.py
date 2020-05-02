a=int(input("enter a start number"))
b=int(input("enter a end number"))
for i in range(a,b+1):
    for n in range(2,i//2+2):
        if (i%n)==0:
            break
        else:
            if n==i//2+1:
                print(i)
k=int(input("enter a number to check if its prime or not"))
m=2
h=1
while m<k:
    if k%m==0:
        h=h+1
    m=m+1
if h==1:
    print("number is prime")
else:
    print("number is composite")



