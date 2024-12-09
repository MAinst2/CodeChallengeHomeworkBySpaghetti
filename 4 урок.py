import random


# 1)

def nubmer_1(first=300, second=19):
    i = first
    while (i % second) != 0:
        i += 1
    print(i)


nubmer_1(1000, 52)


# 2)
N = 1234


def number_2():
    reversed_N = int(str(N)[::-1])
    print(reversed_N)


number_2()


# 3)
n = 150
d = 150


def number_3():
    i = 1
    while i * d <= n:
        if i * d < n:
            i += 1
        elif i * d == n:
            print('Делится!')
            return
    print('Не делится!')


number_3()

# 4)
N = 15
M = 3


def number_4():
    res = 1
    for _ in range(M):
        res *= N
    print(res)


number_4()

# 5)


def number_5(num):
    i = 1
    while 3 * i <= num:
        if 3 * i < num:
            i += 1
        elif 3 * i == num:
            print('Является')
            return
    print('Не является!')


lst = [int(input('Введите число: ')) for _ in range(5)]
for q in lst:
    number_5(q)

# 6)


def foo_1(count):
    lst = [random.randint(1, 100) for _ in range(count)]
    print(lst)


foo_1(10)


def foo_2(lst):
    for i in lst:
        print(i, end='')
    print()


foo_2([1, 2, 3, 4, 5])


def foo_3():
    lst = [11, 2, 3, 4, 5]
    max_value = f"Максимальное значение: {max(lst)}, а его индекс: {
        lst.index(max(lst))}"
    min_value = f"Минимальное значение: {min(lst)}, а его индекс: {
        lst.index(min(lst))}"

    print(max_value)
    print(min_value)


foo_3()
lst = [11, 2, 3, 4, 5]
N = 3


def foo_4(lst, N):
    less_n = 0
    more_n = 0
    eq_n = 0
    for i in lst:
        if i < N:
            less_n += 1
        elif i > N:
            more_n += 1
        else:
            eq_n += 1
    print(less_n, more_n, eq_n)


foo_4(lst, N)

lst = [11, 2, 3, 4, 5, 122, 3444, 55, 22]


def foo_5(lst, k, n):
    tmp_lst = []
    for i in range(len(lst)):
        if i == n:
            tmp_lst.append(k)
        tmp_lst.append(lst[i])
    if n >= len(lst):
        tmp_lst.append(k)
    print(tmp_lst)


foo_5(lst, 777, 9)


def foo_6(lst, n):
    tmp_lst = []
    i = 0
    while i < len(lst):
        if i == n:
            i += 1
        tmp_lst.append(lst[i])
        i += 1
    print(tmp_lst)


foo_6(lst, 9)


def foo_7(lst, n):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                tmp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = tmp


print(lst)


foo_7(lst, 9)


# 7)

lst = [1144, 255234, 3, 10, 777]


def number_7(lst):
    max_lst = []
    for _ in range(3):
        max_elem = float('-inf')
        for i in lst:
            if i > max_elem and i not in max_lst:
                max_elem = i
        max_lst.append(max_elem)
    print(max_lst[2])


number_7(lst)


# 8)

lst = [1144, 255234]


def number_8(lst):
    if len(lst) > 1:
        new_lst = []
        new_lst.append(lst[-2])
        new_lst.append(lst[-1])
        new_lst.extend(lst[0:-2])
        print(new_lst)
    else:
        print('Список слишком маленький')


number_8(lst)


# 9)

lst = [11, 2, 3, 4, 5, 122, 3444, 55, 22]
k = int(input('Введите число: '))


def number_9(lst, k):
    max_elem = lst[0]
    for i in lst:
        if i > max_elem:
            max_elem = i

    tmp_lst = []
    for i in range(len(lst)):
        tmp_lst.append(lst[i])
        if lst[i] == max_elem:
            tmp_lst.append(k)
    print(tmp_lst)


number_9(lst, k)
