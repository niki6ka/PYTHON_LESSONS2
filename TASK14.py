"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""
max_step = str(input("Введите максимальную степень: "))
i = 0
if (str.isdigit(max_step) == False): print("Такая себе степень")
else:
    max_step = int(max_step)
    while i <= max_step:
        print(i, "степень числа 2 = ", pow(2, i))
        i = i + 1

