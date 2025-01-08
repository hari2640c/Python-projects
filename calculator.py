import math
print("hello !!")
while True:
    print("operations:sum,difference,product,division,square,root")
    op = input("enter the operation to be done:")
    if (op=="sum"):
        x = float(input("enter number 1"))
        y = float(input("enter number 2"))
        print("sum is:"+str(x+y))

    elif (op =="difference"):
        x = float(input("enter number 1"))
        y = float(input("enter number 2"))
        print("difference is:" + str(x-y))

    elif (op =="product"):
        x = float(input("enter number 1"))
        y = float(input("enter number 2"))
        print("product is:" + str(x*y))

    elif (op =="division"):
        x = float(input("enter number 1"))
        y = float(input("enter number 2"))
        print("quotient is:" + str(x/y))
        print("remainder is"+ str(x%y))

    elif (op =="square"):
        x = float(input("enter number "))
        print("difference is:" + str(x**2))

    elif (op =="root"):
        x = float(input("enter number "))
        if(x>0):
            print("difference is:" + str(math.sqrt(x)))
        else:
            print("error")

    else:
        print("incorrect operation try again")

    c=input("do you want to continue(y/n)")
    if(c.lower()!="y"):
        break

