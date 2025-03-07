a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter\n1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\nEnter YOur Choice:"))
if c==1:
    print("Sum: ",a+b)
elif c==2:
    print("Difference",a-b)
elif c==3:
    print("Product",a*b)
elif c==4:
    print("Division",a/b)
else:
    print("Invalid Choice")