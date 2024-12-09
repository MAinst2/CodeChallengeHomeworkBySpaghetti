with open("coingecko.txt", "r", encoding="utf-8") as file:
    s = file.read()


to_find = 'd-lg-inline font-normal text-3xs tw-ml-0 md:tw-ml-2 md:tw-self-center tw-text-gray-500">'
splited = s.split(to_find)

for elem in splited:
    test_lst = elem[:20].split('\n')
    if len(test_lst) < 2:
        continue
    print(test_lst[1])
