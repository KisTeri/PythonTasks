# Составить программу нахождения произведения двух наименьших из трех различных чисел


a, b, c = map(float, input("Введите 3 числа: ").split())


def min_number(a, b, c):
    nums = sorted([a, b, c])
    return f"Произведение 2 наименьших чисел: {nums[0] * nums[1]}"


print(min_number(a, b, c))