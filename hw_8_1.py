#1) Определение количества различных подстрок с использованием
# хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9


def hash_str(string: str):
    hash_array = []
    for i in range(len(string)):
        j = i+1
        while j <= len(string):
            # hash_array.append(hash(string[i:j]))
            hash_array.append(string[i:j])
            j += 1
    return set([subset for subset in hash_array if subset is not (string or ' ')])#.__len__()


print(hash_str('papa '))
