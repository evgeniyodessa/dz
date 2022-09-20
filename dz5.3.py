number=int(input("vvod: "))
a=int(number/100)
b=int((number/10)%10)
c=int(number%10)
reversed_number=(c*100+b*10+a)
print(f'{reversed_number:03}')





