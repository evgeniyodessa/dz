a=int(input("vvod a: "))
b=int(input("vvod b: "))
c=int(input("vvod c: "))
if a>b and a>c:
    max=a
    print(max)
elif b>a and b>c:
    max=b
    print(max)
else:
    max=c
    print(max)