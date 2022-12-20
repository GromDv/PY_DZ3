    # Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    # Пример:
    # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def FibonachiPositiv(num1, num2):
    if num1 == 0:
        return 1
    else :
        return num1 + num2

def FibonachiNegativ(num1, num2):
    return num2 - num1

n = int(input('Введите число k: '))
listNum = [0,1]
for i in range(2,n+1):
    listNum.append(FibonachiPositiv(listNum[i-2],listNum[i-1]))
print(listNum)

for i in range(n):
    listNum.insert(0, FibonachiNegativ(listNum[0],listNum[1]))

print(listNum)