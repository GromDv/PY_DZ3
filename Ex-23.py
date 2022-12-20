# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

listNum = [2, 3, 4, 5, 6]
listRes = []
mutpl = 1
for i in range(len(listNum) // 2):
    listRes.append(listNum[i] * listNum[-1-i])
if len(listNum) % 2 == 1:
    listRes.append((listNum[len(listNum) // 2])**2)
print(listNum)
print(listRes)