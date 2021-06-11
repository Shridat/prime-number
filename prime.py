n=int(input("Enter a number="))
flag=1
if(n==1):
    print("1 is neighter prime nor composite number!")
else:
    for i in range(2,n):
        if(n%i==0):
            flag=0
if flag:
    print(str(n)+" is prime!!")
else:
    print(str(n)+" is not prime")

