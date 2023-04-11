"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""

import random
from random import randint
first_numb = random.randint(0,1001)
second_numb = random.randint(0,1001)
i = 1
summ = first_numb + second_numb
multi = first_numb * second_numb
added = 0
print("Сумма Петиных чисел =", summ, "произведение =", multi)
while i <= summ:
    added = summ - i
    if added * i != multi: i = i + 1
    else:
        break
print("Петины числа это", first_numb, "и", second_numb)
print("Катины числа это", i, "и", added)



