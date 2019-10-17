# 1 В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

dividers_array = [x for x in range(2, 10) ]


def test_divide(number_div):
    dividers = {x for x in range(2, 10)}
    for number_ in range(1, number_div):
        for divider in dividers:
            if number_ % divider == 0:
                dividers[divider] += 1


for number in range(2, 99):



# 3 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint
array_num = [randint(-100, 100) for x in range(100)]

min_ = max_ = 0
min_index = max_index = 0

for index, num in enumerate(array_num):
    if num <= min_:
        min_ = num
        min_index = index
    elif num >= max_:
        max_ = num
        max_index = index

middle_var = array_num[min_index]
array_num[min_index] = array_num[max_index]
array_num[max_index] = middle_var
print(array_num)

# 4 Определить, какое число в массиве встречается чаще всего.
arr_num = [1, 1, 2, 3, 2, 3, 2, 5]
set_num = set(arr_num)
def count_num(number_for_count, arr_for_count):
    sum_num = 0
    for nu in arr_for_count:
        if nu == number_for_count:
            sum_num += 1
    return sum_num
dictionary = {x for x in set_num}
for elem in dictionary:
    dictionary[elem] = count_num(dictionary[elem], arr_num)

