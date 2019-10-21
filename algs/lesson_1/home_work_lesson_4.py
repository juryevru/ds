# Написать два алгоритма нахождения i-го по счёту простого числа.
# Проанализировать скорость и сложность алгоритмов.

import timeit
import cProfile

eratosthen_str = '''
def eratosthen(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    return [i for i in sieve if i != 0]
'''
eratosthen_str_list = [f'{eratosthen_str} \neratosthen({i})' for i in range(10, 10000, 100)]

simple_num_str = """
def simple_num(n):
    simple_nums = [i for i in range(n)]
    simple_nums[1] = 0
    for index, value in enumerate(simple_nums):
        for i in range(2, value - 1):
            if value % i == 0:
                simple_nums[index] = 0
                break
    return [i for i in simple_nums if i != 0]
"""
simple_str_list = [f'{simple_num_str} \nsimple_num({i})' for i in range(10, 10000, 100)]

for index, string in enumerate(simple_str_list):
    print(f'{index * 100}: {timeit.timeit(string, number=10)}')

for index, string in enumerate(eratosthen_str_list):
    print(f'{index * 100}: {timeit.timeit(string, number=10)}')

for index, string in enumerate(simple_str_list):
    print(f'{index * 100}: {cProfile.run(string)}')

for index, string in enumerate(eratosthen_str_list):
    print(f'{index * 100}: {cProfile.run(string)}')
