n = int(input("Введите число: "))

def print_triangle(n):
    for i in range(1, n+1):
        for j in range(1, n-i+2):
            print(j, end=" ")
        print()


print_triangle(n)