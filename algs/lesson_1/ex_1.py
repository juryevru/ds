# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
a = int(input('Введите трёхзначное целое число'))
b_1 = a % 10
b_2 = a % 100 // 10
b_3 = a // 100
c = b_1 + b_2 + b_3
d = b_1 * b_2 * b_3
print(c, d)
