
def which_is_bigger():
    input_number = int(input("Введите число N - количество попыток ввода: "))
    for i in range(input_number):
        number1 = int(input("Введите первое число для сравнения: "))
        number2 = int(input("Введите второе число для сравнения: "))
        if number1 > number2:
            print(f"Первое число - {number2} - больше")
        elif number1 < number2:
            print(f"Второе число - {number2} - больше")
        else:
            print("Числа равны")


which_is_bigger()