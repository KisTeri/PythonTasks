n = int(input("Введите число: "))


def multiplication_table(n:int):
    for i in range(n,n+1):
        for j in range(1,10):
            print(f"{i} * {j} = {i*j}")
        print()


multiplication_table(n)