

def number_even_or_not():
    input_number = int(input("Введите число N - количество попыток ввода: "))
    for i in range(input_number):
        number = int(input("Введите число: "))
        if number % 2 == 0:
            print("Это число четное")
        else:
            print("Это число нечетное")


number_even_or_not()