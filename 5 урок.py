# 1 УРОВЕНЬ

# 1)

n_ticket = '111345898004'
if int(n_ticket[0]) + int(n_ticket[1]) + int(n_ticket[2]) == int(n_ticket[-3]) + int(n_ticket[-2]) + int(n_ticket[-1]):
    print('Счастливый')
else:
    print('Обычный')


# 2)

word = 'А роза упала на лапу Азора'
word_l = word.lower().replace(' ', '')
word_r = word_l[::-1]
if word_l == word_r:
    print('Является палиндромом')
else:
    print('Не является палиндромом')


# 3)


def is_valid_email(email):
    valid_tlds = [
        ".com", ".org", ".net", ".info", ".biz", ".edu", ".gov", ".mil", ".int",
        ".xyz", ".io", ".pro", ".top", ".club", ".site", ".online", ".store", ".tech",
        ".ru", ".ua", ".by", ".kz", ".uk", ".de", ".fr", ".it", ".es", ".nl", ".se",
        ".pl", ".ch", ".cz", ".cn", ".jp", ".in", ".kr", ".sg", ".hk", ".id", ".ph",
        ".us", ".ca", ".br", ".mx", ".ar", ".co", ".cl", ".za", ".ng", ".eg", ".ke",
        ".ma", ".au", ".nz", ".pg", ".fj"]

    if email.count('@') != 1:
        return False

    parts = email.split('@')
    parts_s = parts[1]

    if parts_s.count('.') < 1:
        return False

    parts_d_s = '.' + parts_s.split('.')[-1]
    if parts_d_s in valid_tlds:
        return True
    else:
        return False


email = str(input('Введите Email: '))

if is_valid_email(email):
    print("Email верный")
else:
    print("Email не верный")


# 4)

s = 'Python-разработчик, уверенный в своей безупречности, на код-ревью раскритиковал подход с использованием functools.lru_cache, настаивая на явной оптимизации, но через месяц получил инцидент: ‘Прод пал — память закончилась из-за циклических ссылок в его кастомной реализации memoization'

s_mod = s.lower().replace('.', '').replace(',', '').replace(
    '!', '').replace('?', '').replace('@', '').replace('"', '').replace('(', '').replace(')', '').replace('-', ' ').replace('–', '').replace(':', '').replace('—', '').replace('‘', '').replace('\'', '')

words_lst = s_mod.split()
words_dict = {}

for word in words_lst:
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1


for word, amount in words_dict.items():
    print(word, amount)


# 2 УРОВЕНЬ

# 1)

password = str(input('Введите пароль: '))


def check_password(password):

    if len(password) <= 8:
        print('Пароль должен содержать не менее 8 символов')
        return
    elif len(password) > 16:
        print('Пароль не должен быть больше 16 символов')
        return
    lower_c = 0
    upper_c = 0
    num = 0
    char = 0

    for ch in password:
        if ord(ch) in range(97, 123):
            lower_c += 1
        if ord(ch) in range(65, 91):
            upper_c += 1
        if ord(ch) in range(48, 58):
            num += 1
        if ord(ch) in range(33, 48) or ord(ch) in range(58, 65) or ord(ch) in range(91, 97):
            char += 1

    if len(password) >= 12 and lower_c >= 3 and upper_c >= 2 and num >= 2 and char >= 1:
        print('Сложный')
    elif len(password) >= 8 and lower_c >= 2 and upper_c >= 1 and num >= 1:
        print('Средний')
    else:
        print('Простой')


check_password(password)


# 2)

s = 'afajfhndafdkjafjqsdfhjhf'

new_s = {}

i = 0
while i < len(s):
    if s[i] not in new_s:
        new_s[s[i]] = 1
        i += 1
    else:
        new_s[s[i]] += 1
        i += 1

for ch, amount in new_s.items():
    print(ch, amount)


n = ''

keys = list(new_s.keys())

i = 0
while i < len(new_s):
    n += str(keys[i])
    n += str(new_s[keys[i]])
    i += 1
print(n)


# 3)

s = 'Python-разработчик, уверенный в своей безупречности, на код-ревью раскритиковал подход с использованием functools.lru_cache, настаивая на явной оптимизации, но через месяц получил инцидент: ‘Прод пал — память закончилась из-за циклических ссылок в его кастомной реализации memoization'

s_mod = s.lower().replace(' ', '')


new_s = {}

i = 0
while i < len(s_mod):
    if s_mod[i] not in new_s:
        new_s[s_mod[i]] = 1
        i += 1
    else:
        new_s[s_mod[i]] += 1
        i += 1


def get_value(item):
    return item[1]


sorted_ch = sorted(new_s.items(), key=get_value, reverse=True)[:3]

for ch, count in sorted_ch:
    print(f"{ch} - {count}")


# 4)

text = 'Сегодня мы решили отправиться в небольшой поход (недалеко от города). Маршрут проходил через лес (густой и влажный после дождя), где можно было встретить множество птиц и животных. На середине пути мы сделали привал (около небольшого озера), чтобы перекусить и отдохнуть. Погода была приятной (с лёгким ветерком), а настроение у всех — отличным. К концу дня мы добрались до финишной точки маршрута (старый мост через реку) и сделали несколько фотографий на память.'

new_text = ''

status = False

for ch in text:
    if ch == '(':
        status = True
        continue
    elif ch == ')':
        status = False
        continue
    if status:
        continue
    else:
        new_text += ch
print(new_text)
