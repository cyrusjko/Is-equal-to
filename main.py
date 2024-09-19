n1=int(input("Enter first Number"))
n2=int(input("Enter second Number"))
def checkifsame(n1,n2):
    if n1^n2 != 0:
        print("Numbers are not the same")
    else:
        print("Numbers are the same")
checkifsame(n1,n2)