# def f(x):
#     return x


# print(f(6))

# f1 = lambda x: x
# print(f1(6))
# print ((lambda x:x)(6))

# x = "5 4 3 67 2 12"
# print(x)
# x1 = x.split()
# print(x1)
# x2 = list(map(lambda y: int(y)*3, x.split()))
# print(x2)

# x2 = list(filter(lambda y: y%2 == 0, x2))
# print(x2)


# Задача No47.
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
# Пример ввода и вывода данных представлены на следующем слайде
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values)) if values == transformed_values:
# print(‘ok’) else:
# print(‘fail’)
# Вывод:
# ok

transformation= lambda x: x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transormed_values = list(map(transformation, values))
print(values)
print(transormed_values)