n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

def rectangle(n:int,m:int):
    for i in range(n):
        for j in range(m):
            print("*",end=" ")
        print()
        

rectangle(n,m)