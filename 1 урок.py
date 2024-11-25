# 1 Уровень
# 1)

a = int(input('Пожалуйста, введите число, которое хотите возвести в степень: '))
b = int(input('Пожалуйста, введите степень, в которую хотите возвести предидущее число: '))
print(a ** b)

# 2)

a = int(input('Пожалуйста, введите число от 1 до 7: '))

if a == 1:
    print('Понедельник')
elif a == 2:
    print('Вторник')
elif a == 3:
    print('Среда')
elif a == 4:
    print('Четверг')
elif a == 5:
    print('Пятница')
elif a == 6:
    print('Суббота')
elif a == 7:
    print('Воскресенье')
else:
    print('Вы ввели число не от 1 до 7!')

# 3)

a = int(input('Пожалуйста введите число a: '))
b = int(input('Пожалуйста введите число b: '))

if a > b:
    print(a)
if a < b:
    print(b)
if a == b:
    print('Оба числа равны!')

# 4)

a = int(input('Пожалуйста, введите свой депозит в $: '))

b = int(input('Пожалуйста, введите курс $: '))

print(a*b)


# 2 Уровень
# 1)
a = int(input('Пожалуйста, введите целое число: '))

if a % 2 > 0:
    print('Нечетное')
else:
    print('Четное')

# 2)
a = int(input('Пожалуйста, введите 1-ое число: '))
b = int(input('Пожалуйста, введите 2-ое число: '))
c = int(input('Пожалуйста, введите 3-ое число: '))

min_nubmer = min(a, b, c)

print(min_nubmer)

# 3)
a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
h = int(input('Введите число H: '))

if h > b:
    print('Пересып')
elif h < a:
    print('Недосып')
else:
    print('Нормально')


# 3 Уровень
# 1)
a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
h = input('Выберите операцию +, -, /, *, mod, pow, div: ')

if h == '+':
    print(a+b)
elif h == '-':
    print(a-b)
elif h == '/':
    print(a/b)
elif h == '*':
    print(a*b)
elif h == 'mod':
    print(a % b)
elif h == 'pow':
    print(a**b)
elif h == 'div':
    print(a//b)
else:
    print('Произошла ошибка в воде, попробуйте заново.')

# 2)

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

if a % b == 0 and b % a == 0:
    print('a на b делится нацело, и b на a делится нацело')
elif b % a != 0 and b % a != 0:
    print('b на a не делится нацело, и a на b не делится нацело')
elif a % b != 0 and b % a == 0:
    print('a на b не делится нацело, а b на a делится нацело')
elif b % a != 0 and a % b == 0:
    print('b на a не делится нацело, а a на b делится нацело')
else:
    print('Произошла ошибка')

# 3)
a = input('Введите трёх значное число: ')

if a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
    print('Есть одинаковые цифры')
else:
    print('Нету одинаковых цифр')
