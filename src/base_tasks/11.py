# Написать программу, которая решает следующую задачу: «N школьников делят k яблок поровну так, чтобы каждому достались только целые яблоки, остальные яблоки остаются в корзинке. Определить, сколько яблок достанется каждому школьнику и сколько яблок останется в корзинке»

students_num = int(input("Введите количество школьников: "))
apple_num = int(input("Введите количество яблок: "))


def apple_split(students_num: int, apple_num: int):
    apple_student = apple_num // students_num
    apple_basket = apple_num % students_num
    return apple_student, apple_basket


print(f"Количество яблок у каждого школьника: {apple_split(students_num, apple_num)[0]}\nКоличество оставшихся яблок в корзине: {apple_split(students_num, apple_num)[1]}")
