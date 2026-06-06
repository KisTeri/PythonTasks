n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Теперь введите числа через пробел: ").split()))
def find_palindrome(n: int, list_n: list):
    palindrome = True
    for i in range(n // 2):
        if list_n[i] != list_n[n - 1 - i]:
            palindrome = False
            break

    if palindrome:
        print("Да, палиндром")
    else:
        print(f"Нет, не палиндром")


find_palindrome(n, list_n)