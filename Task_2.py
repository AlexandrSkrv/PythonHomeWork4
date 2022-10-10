# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# Пример:
# N = 20 => [2, 2, 5]

num = int(input(""))
i = 2  
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f'{lst}')
