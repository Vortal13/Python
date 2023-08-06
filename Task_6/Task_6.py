# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# #Пример
# 385916 -> yes
# 123456 -> no

num=input('Введите намер билета: ')

if (int(num[0])+int(num[1])+int(num[2]))==(int(num[3])+int(num[4])+int(num[5])):
    print ('yes')
else:
    print ('no')

# Вариант 2
# a=n//1000
# b=n%1000
# sum1=a//100+(a//10)%10+a%10
# sum2=b//100+(b//10)%10+b%10

# if sum1==sum2:
#     print ('yes')
# else:
#     print ('no')