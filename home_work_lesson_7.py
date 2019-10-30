# 1 Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться
# сортировка пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
#
import random
import cProfile


def bubble_sort(num_list: list):
    n = 1
    while len(num_list) > n:
        for i in range(len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        n += 1
    return num_list


def bubble_sort_optimized(num_list: list):
    n = 1
    length = len(num_list)
    while length > n:
        for i in range(length - 1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        n += 1
    return num_list


str_bubble_simple = """
def bubble_sort(num_list: list):
    n = 1
    while len(num_list) > n:
        for i in range(len(num_list) - 1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        n += 1
    return num_list
"""
str_bubble_optimized = """
def bubble_sort_optimized(num_list: list):
    n = 1
    length = len(num_list)
    while length > n:
        for i in range(length - 1):
            if num_list[i] > num_list[i + 1]:
                num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
        n += 1
    return num_list
"""

array_int = [num for num in range(-10000, 10100)]
random.shuffle(array_int)


print(cProfile.run(f'{str_bubble_simple}\nbubble_sort(array_int)'))
print(cProfile.run(f'{str_bubble_optimized}\nbubble_sort_optimized(array_int)'))
# вместо 401 вызова встроенного метода len() вызывается 1 раз, на маленьких массивах
# не показательно, но и то разница у меня в 2 раза.
