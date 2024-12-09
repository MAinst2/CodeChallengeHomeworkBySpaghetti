# 1 Уровень
# 1)

import requests
d1 = {
    'a': 5,
    'b': 4,
    'c': 6,
}

d2 = {
    'd': 55,
    'e': 444,
    'f': 61,
}


for key, val in d2.items():
    print(key)
    d1[key] = val


print(d1)
print(d2)

# 2)
d = {
    'a': 5,
    'b': 4,
    'c': 6,
    'd': 55,
    'e': 444,
    'f': 61,
}

values_summ = 0
for val in d.values():
    values_summ += val

print(values_summ/len(d))

# 3)

lst_1 = [4, 5, 6]
lst_2 = [1, 2, 3]

d = {}

for key, val in zip(lst_1, lst_2):
    d[key] = val
    print(d)


# 4)

text = '''Да, любовь (думал он опять с совершенной ясностью), но не та любовь, которая любит за что-нибудь, для чего-нибудь или почему-нибудь, но та любовь, которую я испытал в первый раз, когда, умирая, я увидал своего врага и все-таки полюбил его. Я испытал то чувство любви, которая есть самая сущность души и для которой не нужно предмета. Я и теперь испытываю это блаженное чувство. Любить ближних, любить врагов своих. Все любить – любить Бога во всех проявлениях. Любить человека дорогого можно человеческой любовью; но только врага можно любить любовью Божеской. И от этого-то я испытал такую радость, когда я почувствовал, что люблю того человека. Что с ним? Жив ли он… Любя человеческой любовью, можно от любви перейти к ненависти; но Божеская любовь не может измениться. Ничто, ни смерть, ничто не может разрушить ее. Она есть сущность души. А сколь многих людей я ненавидел в своей жизни. И из всех людей никого больше не любил я и не ненавидел, как ее'''


text = text.lower()


text = text.replace('.', '').replace(',', '').replace('!', '').replace('?', '')
text = text.replace('(', '').replace(')', '').replace('-', '').replace('–', '')

words_lst = text.split()
words_dict = {}
for word in words_lst:
    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1

for word, amount in words_dict.items():
    print(word, amount)

# 5)


url = 'https://chainid.network/chains.json'
response = requests.get(url)
data = response.json()

for info_dict in data:
    rpc = None
    if len(info_dict['rpc']):
        rpc = info_dict['rpc'][0]

    eip_1559 = False
    if 'feauters' in info_dict and len(info_dict['feauters']):
        for elem in info_dict['feauters']:
            if elem['name'] == 'EIP1559':
                eip_1559 = True
                break

    explorer = None
    if 'explorers' in info_dict and len(info_dict['explorers']):
        explorer = info_dict['explorers'][0]['url']

    print(f"{info_dict['name']} | "
          f"{rpc} | "
          f"eip-1559: {eip_1559} | "
          f"{info_dict['nativeCurrency']['symbol']} | "
          f"decimals: {info_dict['nativeCurrency']['decimals']} | "
          f"chain_id: {info_dict['chainId']} | "
          f"explorer: {explorer}"
          )


# 6)

url = 'https://chainid.network/chains.json'
response = requests.get(url)
data = response.json()

chain_id = int(input('Введите ID чейна: '))

for info_dict in data:
    if info_dict['chainId'] == chain_id:
        print(info_dict['nativeCurrency']['symbol'])
        break
