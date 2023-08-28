#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Input:
# 5
# 1 4 3 2 5
# 6
# Output:
# 5

n = int(input('Введите размер массива: '))
list_n = input('Введите элементы списка через пробел: ').split()
array = list(map(int, list_n))
x = int(input('Введите искомое число: '))
index_element = 0
min_element = abs(x - array[0])
for i in range(1, n):
    element = abs(x - array[i])
    if element < min_element:
        min_element = element
        index_element = i

print (f"Самый близкий по величине элемент к заданному числу {array[index_element]}")


# Вариант 2
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)