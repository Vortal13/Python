#Задача №11. 
#Дано натуральное число A > 1. Определите, каким по
#счету числом Фибоначчи оно является, то есть
#выведите такое число n, что φ(n)=A. Если А не
#является числом Фибоначчи, выведите число -1.
#Пример:
#Input: 5
#Output: 6 


n=int(input('Введите число: '))
a0=0
a1=1
a2=0
num=0

while a2 <= n:
    a2 = a0 + a1
    a0 = a1
    a1 = a2
    num+=1
if a0 == n:
    print(num)
else:
    print('-1')
    

# Вариант 2
# a = int(input('enter num: '))
# mylist = [0, 1]
# while fib < a:
#     fib = mylist[len(mylist) - 1] + mylist[len(mylist) - 2]
#     mylist.append(fib)
    
# print([-1, len(mylist)][fib == a])
# pythonanywere