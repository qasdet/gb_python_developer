# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр (отсекаем минус, считаем все в плюс).
# Пример:
# 67,82 -> 23
# 0,56 -> 11

float_num = input('Введите число с плавающей точкой: ')
print(type(float_num))
sum = 0
for i in float_num:
    if i != '.':
        sum += int(i)
print(sum)

# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) """

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")


# 3. Реализуйте случайное перемешивание списка.
# Пример:
# Исходный вариант -> ['Вася Пупкин', 100, 3.14, 'True '] 
# Результат -> [100, 3.14, 'True ', 'Вася Пупкмн']

list = ['Веселый пианист', 250, 3.14, 'True ']
print(list) 
import random
random.shuffle(list)
print('->', list) 