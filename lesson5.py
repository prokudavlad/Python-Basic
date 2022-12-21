# txt = 'Hello Word'
# for leter in txt:
#    print(leter)

# fruits = ['apple', 'banana', 'melon', 'pineapple']
# for fruit in fruits:
#    print(fruit)

# Неправильно
# for i in fruits:
#    print(i)

# txt = 'jhfdkjsaflhdshfkjzlxnsakjldhskf'
# for leter in txt:
#    if leter == 'f':
#        print(leter)

# txt = 'jhfdkjsaflhdshfkjzlxnsakjldhskf'
# list_f = []
# for leter in txt:
#     if leter == 'f':
#         list_f.append(leter)
# print('list_f: ', list_f)

# planning_cycles = [
#     {'sd': 1, 'teams': [1, 2, 3, 4, 5]},
#     {'sd': 1, 'teams': [5, 6, 7, 8, 9]},
#     {'sd': 1}
# ]
# teams = []
# for planning_cycle in planning_cycles:
#     if planning_cycle_teams := planning_cycle.get('teams'):
#         teams += planning_cycle_teams
# print('teams: ', teams)




# txt = 'j5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isnumeric():
#         print(leter)

# res = ''
# txt = 'j5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isalpha():
#         res = res + leter
# print('res: ', res)
# res = ''
# txt = 'j5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isalpha():
#         res += leter
# print('res: ', res)

# txt = 'jhfdkjsaflhdshfkjzlxnsakjldhskf'
# txt.upper()
# for leter in txt:
#     print('leter: ', leter)
# txt = 'jhfdkjsaflhdshfkjzlxnsakjldhskf'
# txt = txt.upper()
# for leter in txt:
#     print('leter: ', leter)

# # Oператор continue начинает следующий проход цикла, минуя оставшееся тело цикла
# txt = 'j5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isalpha():
#         continue
#     print(leter * 2, end='')

# # Oператор break досрочно прерывает цикл.
# txt = '5hf2143dkj5sa465flh5dshfkj7zlx6nsak9jldhs45kf'
# for leter in txt:
#     if leter.isalpha():
#         break
#     print(leter * 2, end='')

# # Oператор else выполнится только в том случае, если выход из цикла произошел без помощи break
# leter = 'a'
# for i in 'hello world':
#     if i == leter:
#         break
# else:
#     print(f'Буквы {leter} в строке нет')

# leter = 'o'
# for i in 'hello world':
#     if i == leter:
#         break
# else:
#     print(f'Буквы {leter} в строке нет')

# list1 = ['1','2','s','g','a','3','4']
# s = "-"
# s = s.join([i for i in list1 if i.isnumeric()])