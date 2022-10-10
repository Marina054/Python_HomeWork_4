# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

  

n = int(input('Введите число N: '))
p_fact = []
d = 2
while d * d <= n:
    if n % d == 0:
        p_fact.append(d)
        n //= d
    else:
        d +=1
if n > 1:
    p_fact.append(n)
print(p_fact) 
         