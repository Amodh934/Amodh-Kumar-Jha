a=float(input("Enter first number :"))
operators=input("Enter operator (+,-,*,/) : ")
b=float(input("Enter a second number :"))
if operators=="+":
    print("result :" ,a+b)

elif operators =="-":
    print("result :" ,a-b)

elif operators =="*":
    print("result :" ,a*b)

elif operators =="/":
    if  b !=0:
        print("result :" ,a/b)
    else:
        print("Error: number division by 0 is not allowed.")

else:
    print("Invalid Operator! ")
    




    
