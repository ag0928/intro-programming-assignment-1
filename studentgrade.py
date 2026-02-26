a=int(input("enter marks for eng"))
b=int(input("enter marks for maths"))
c=int(input("enter marks for phy"))
d=int(input("enter marks for chem"))
e=int(input("enter marks for bio"))
total=a+b+c+d+e
per=total/5
if per<0 or per>100:
    print("its an error")
else:
    print (total,"out of 500")
    print(per,"out of 100")
    if per<45:
        print("fail")
    elif per>=45 and per<60:
        print("pass")
    elif per<0 or per>100:
        print("its an error")
