# задание 1
N = int(input("введите ширину: "))
while N != 0:
    print("*" * N)
    N -= 1

# задание 2
N = int(input("введите ширину: "))
a = 1
while a <= N:
    print("*" * a)
    a += 1

# задание 3
N = int(input("введите ширину: "))
a = 0
while N != 0:
    print(a * " " + "*" * N)
    N -= 1
    a += 1

# задание 4
N = int(input("введите ширину: "))
a = 1
while N != 0:
    print((N - 1) * " " + "*" * a)
    N -= 1
    a += 1
