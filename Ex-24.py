# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

listNum = [1.1, 1.2, 3.1, 5, 10.01]
print(listNum)
listStr = []
# Фильтруем только вещественные числа и разделяем их на две строки - целую и дробную части
for i in listNum:
    if isinstance(i, float):
        listStr.append(str(i).split('.'))
# обнуляем целую часть и обратно преобразуем в вещественные
listNewFloat = []
for i in listStr:
    listNewFloat.append(float('0.' + i[1]))
# проверяем список
print(listNewFloat)
# выводим разницу между максимальным и минимальным значением дробной части элементов
print("Результат = ", max(listNewFloat) - min(listNewFloat))