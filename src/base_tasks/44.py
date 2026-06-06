from idlelib.config_key import WHITESPACE_KEYS

n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))

def find_greatest_common_divisor(n: int, m: int) -> int:
    while n != m:
        if n > m:
            n -= m
        else:
            m -= n
    print(f"НОД: {n}")


find_greatest_common_divisor(n, m)

