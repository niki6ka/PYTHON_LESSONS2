"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""

import random
from random import randint
coins = str(input("Введите общее количество монет: "))
avers = 0
revers = 0
i = 1
position = 0
if str.isdigit(coins)==False: print("Увы, моншер! Задача подразумевает работу с числами!!!")
else:
      coins = int(coins)
      if coins < 2: print("А смысл бросать", coins, "монет?")
      else:
        print("БРОСАЕМ!!!")
        while i<=coins:
            position = random.randint(0,1)
            if position == 0:
                print(i, "Аверс", end=" ")
                avers = avers+1
            else:
                print(i, "Реверс", end=" ")
                revers = revers + 1
            i = i + 1
print()
if avers == revers: print("Аверсов и реверсов поровну, переворачивайте что хотите")
else:
    if avers > revers: print("Быстрее перевернуть", revers, "реверсов")
    else: print("Быстрее перевернуть", avers, "аверсов")




