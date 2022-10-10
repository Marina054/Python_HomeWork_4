# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
str1 = '1234'
str2 = 'qwe'
str3 = str1 + str2
list2 = list(str3)
random.shuffle(list2)
Mix = ''.join([random.choice(list2) for x in range(20)])
print(Mix)

from collections import OrderedDict
print(list(OrderedDict.fromkeys(Mix)))