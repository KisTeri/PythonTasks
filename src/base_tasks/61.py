n = int(input("Введите количество элементов: "))
list_n = list(map(int, input("Теперь введите числа через пробел: ").split()))
def find_palindrome(n: int, list_n: list):
    if list_n == list_n[::-1]:
        print("Палиндром")
    else:
        palindrome = False
        for i in range(n):
            new_list = list_n[:i] + list_n[i+1:]
            if new_list == new_list[::-1]:
                palindrome = True
                break
        print("Да, палиндром" if palindrome else "Нет, не палиндром")


find_palindrome(n, list_n)