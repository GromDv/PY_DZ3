# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Конвертируем в двоичный вид методом рекурсии
def ConvertToBin(num):
    if num > 0:
        res = num%2 + ConvertToBin(num//2)*10
    else:
        res = 0
    return res

number = int(input('Введите число: '))
print("В двоичном формате это: ", ConvertToBin(number))
