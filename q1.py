def mul(n1,n2):
    mult=n1*n2
    if mult<=1000:
        return mult
    else :
        return n1+n2
num1=int(input("enter first num"))
num2=int(input("enter second num"))
result=mul(num1,num2)
print(result)
