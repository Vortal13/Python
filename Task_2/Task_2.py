#Задача 2: Найдите сумму цифр трехзначного числа.
#Пример
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

n=int(input('Введите число: '))
summ=int((n%10+((n//10)%10)+((n//100)%10)))

print (f"Сумма цифр в числе {n} равна {summ}")

#Вариант 2
#res = int((n%10)+((n//10)%10)+((n//100)%10))