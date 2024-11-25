# 1 Уровень
# 1)
temp_kastrylya = 7
temp_rost = 2    # за сколько секунд увеличивается темперартура в кастрюле на 1 градус
print((100-temp_kastrylya)/temp_rost)

# 2)
i = 1

while i < 6:
    print(str(i) + ' 000')
    i += 1

# 3)
height = int(input('Введите высоту прямоугольного треугольника: '))
for i in range(height):
    i += 1
    print('*' * i)

# 2 Уровень
# 1)

A = int(input('Введите длину коробки: '))
B = int(input('Введите ширину коробки: '))
C = int(input('Введите высоту коробки: '))
M = int(input('Введите высоту двери: '))
K = int(input('Введите ширину двери: '))

sorted_box = sorted([A, B, C])
sorted_door = sorted([M, K])

if (sorted_box[0] <= sorted_door[0] and sorted_box[1] <= sorted_door[1]):
    print('Влезает')
else:
    print('Не влезает')

# 2)
h = int(input('Введите высоту равнобедренного треугольника: '))
probels = h - 1
stars = 1
i = 0
while i < h:
    print(' ' * probels + '*' * stars)
    probels -= 1
    stars += 2
    i += 1


# 3)

N = int(input('Введите число N: '))

i = 1
while i**2 <= N:
    print(i**2)
    i += 1

# 3 Уровень
# 1)
k = int(input('Введите число шариков мороженого: '))

if k == 1 or k == 2 or k == 4 or k == 7:
    print('Нельзя купить такое кол-во шариков мороженого')
else:
    print('Можно купить такое кол-во шариков мороженого')

# 2)
K = float(input('Введите % годовых вклада: '))
M = float(input('Введите сколько клинет положил денег на вклад: '))
S = float(input('Введите сколько клиент получит денег: '))

j = 0
while M <= S:
    M = M + (M / 100 * K)
    j += 1
print(j)

# 3)

N = int(input('Введите число: '))

s = 0

while N > 0:
    s += N % 10
    N //= 10
print(s)

# ЗАДАЧИ НА РАБОТУ СО СПИСКОМ
# 1)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0
i = 0
while i < len(lst):
    s += lst[i]
    i += 1
print(s)

# 2)

my_lst = [17, 40, 79, 1, 44, 14, 48, 32, 50, 62]

i = 0
s = 0
while i < len(my_lst):
    if (my_lst[i] % 2) == 0:
        s += my_lst[i]
        i += 1
    else:
        i += 1
print(s)

# 3) + 4)

my_list = [17, 40, 79, 1, 44, 14, 48, 32, 50, 62]
sml = sorted(my_list)

print(sml[0])
print(sml[-1])

print(my_list.index(sml[0]))
print(my_list.index(sml[-1]))

# ЗАДАЧИ НА РАБОТУ С МЕТОДАМИ СПИСКА
# 1)
lst = []

lst.append('Молоко')
lst.append('Огурцы')
lst.append('Пиво')
lst.append('Рыбка')
lst.append('Чай')
lst.append('Сахар')
lst.append('Сухарики')
del lst[lst.index('Пиво')]
del lst[lst.index('Рыбка')]

print(lst)

# 2)
my_list = [17, 40, 79, 1, 44, 14, 48, 32, 50, 62]
N = int(input('Введите число: '))

if N in my_list:
    print('Число есть в списке')
else:
    print('Числа нет в списке')

# 3)
my_list = [125, 46, 372, 98, 112, 215, 372, 46, 98, 215, 134, 256, 372, 125,
           198, 134, 372, 215, 46, 112, 98, 215, 198, 134, 256, 372, 125, 198, 98, 46]
N = int(input('Введите число: '))

print(f"Число {N} встречается в списке {my_list.count(N)} раз(а)")
