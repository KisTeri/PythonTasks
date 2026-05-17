

def number_not_zero():

    while True:
        number = int(input("Введите целое число: "))
        if number > 0:
            print("Положительное")
        elif number < 0:
            print("Отрицательное")
        else:
            print("Ноль")
            break


number_not_zero()