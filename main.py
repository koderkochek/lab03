print("Введите вариант сортировки (по возрастанию / по убыванию):")
s = input()

n = int(input("Введите количество чисел: "))
print("Введите числа:")

mas = []
for i in range(n):
    mas.append(int(input()))
    #mas[i] = int(input())

print("Исходный массив:")
print(mas)
if (s == "по возрастанию"):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if mas[j] > mas[j + 1]:
                tmp = mas[j]
                mas[j] = mas[j + 1]
                mas[j + 1] = tmp
if (s == "по убыванию"):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if mas[j] < mas[j + 1]:
                tmp = mas[j]
                mas[j] = mas[j + 1]
                mas[j + 1] = tmp

print("Массив после сортировки пузырьком:")
print(mas)