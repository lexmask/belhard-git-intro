import collections
import math

a = input("первое значение ")
a = a.strip(" ")
b = input("второе значение ")
b = b.strip(" ")

a = [int(i) for i in a.split(' ')]    #преобразование в списко
b = [int(i) for i in b.split(' ')]    #преобразование в список
if len(a) != len(b):
    print("строки должны содержать одиноковое кол-во значений")
else:
    for i in range(len(a)):
        print(f"Теугольник {i + 1} с катетами {a[i]} и {b[i]} имеет площадь {a[i] * b[i] / 2} и гипотенузу {round(math.sqrt(pow(a[i],2) + pow(b[i],2)),2)}")

