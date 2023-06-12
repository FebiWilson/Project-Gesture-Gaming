

number=int(input("enter a number "))

count=0
if number>1:
    for i in range(1,number+1):
        if number%i==0:
            count=count+1
    if count==2:
            print("the number is prime")
    else:
            print("the number is not prime")


