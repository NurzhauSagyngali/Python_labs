from task1 import grams_to_ounces
from task2 import F_to_C
from task10 import unique_list

x = float(input())

print(grams_to_ounces(x))

F = int(input())

print(F_to_C(F))

lists = input().split()
lists = [int(num) for num in lists]

print(unique_list(lists))
