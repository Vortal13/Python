# Орел и решка
# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки. 
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.
# Примечание. Если выпавших Решек нет, то необходимо вывести число 00.
# Тестовые данные 🟢
# Sample Input 1:
# ОРРОРОРООРРРО
# Sample Output 1:
# 3
# Sample Input 2:
# ООООООРРРОРОРРРРРРР
# Sample Output 2:
# 7
# Sample Input 3:
# ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
# Sample Output 3:
# 31


money = input('Введите какой стороной лежат монеты (Р-решка, О-орел): ').upper()

n = 0
i = 0

while i < len(money):
    if money.find('P' * (i + 1)) >=0:
        n+=1
    i+=1
print ('Наибольшее количество подряд выпавших Решек: ',n)