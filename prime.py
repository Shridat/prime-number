l=int(input("Enter a lower interval="))
u=int(input("Enter a upper interval="))

print("Prime numbers between "+str(l)+"and "+str(u)+"is=")
for num in range(l,u+1):
    flag=1
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                flag=0
                break
        if flag:
            print(num)

