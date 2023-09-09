# Задача №35.
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 


def is_prime(n, dil=2):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % dil == 0:
        return False
    if dil * dil> n:
        return True
    return is_prime(n, dil + 1)

n = int(input())
print(is_prime(n))