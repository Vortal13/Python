# Задача №17.
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Пример
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

lst = [1, 1, 2, 0, -1, 3, 4, 4]
# print(lst)
# lst1 = []
# for i in lst:
#     if i not in lst1:
#         lst1.append(i)
# #print(lst1)
# print(len(lst1))

print(len(set(lst)))