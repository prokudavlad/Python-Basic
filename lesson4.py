# ================================================
# Условний оператор if
current_temperature = input('Сколько сейчас градусов на улице:')
print('current_temperature: ', current_temperature)
print('type(current_temperature): ', type(current_temperature))

# current_temperature = int(input('Сколько сейчас градусов на улице:'))
# print('current_temperature: ', current_temperature)
# print('type(current_temperature): ', type(current_temperature))
# if current_temperature:
#     print("Спасибо, я получил данние")
# if current_temperature < 5:
#     print('Одень шапку!')
# else:
#     print('Можеш не одевать шапку')

# current_temperature = int(input('Сколько сейчас градусов на улице:'))
# if current_temperature < 5:
#     print('Одень шапку!')
# elif current_temperature > 25:
#     print('Одень кепку!')
# else:
#     print('Можеш не одевать шапку')

# current_temperature = int(input('Сколько сейчас градусов на улице:'))
# if current_temperature < 5:
#    print('Одень шапку!')
# elif current_temperature > 25:
#    print('Одень кепку!')
# elif current_temperature < -25:
#    print('Останься дома!')
# else:
#    print('Можеш не одевать шапку')

# my_str = ""
# if my_str:
#     print(my_str)
# else:
#     print("No")

# my_list = [1, 2]
# if my_list:
#     print(my_list)
# else:
#     print("No")

# =================================================================
# res if condotion else else_res
# current_temperature = int(input('Сколько сейчас градусов на улице:'))
# print('Одень шапку!') if current_temperature < 5 else print('Можеш не одевать шапку!')

# current_temperature = int(input('Сколько сейчас градусов на улице:'))
# x = current_temperature if current_temperature < 5 else None
# print('x: ', x)
# print('type(x): ', type(x))

# current_temperature = int(input('Сколько сейчас градусов на улице:'))
# print('Одень шапку!') if current_temperature < 5 else pass

# expr = "no remainder" if 5% 2 == 0 else None
# print('expr: ', expr)


# ==================================================================
# форми представления строк
# str_ = "Hello"
# print('str_: ', str_)
# print('type(str_): ', type(str_))
# print("We are the so-called "Vikings" from the north.")
# # # https://www.w3schools.com/python/python_strings_escape.asp
# print("We are the so-called \"Vikings\" from the north.")
# print('We are the so-called "Vikings" from the north.')

# print('Hello')
# print("Hello")
# print('''Hello''')
# print("""hello""")

# # Перенос строк
# print(
#     'Hello
#     World'
# )
# print("Hello \n\tworld")
# print('Hello віфвіфл влідфосттвіслов осрлоровілріотілостіст стіфлововволд іфвоіфвілоі вірсловіслоі лорлоіфрсіфлрвл вловріфлорві іфвіфловрло World')
# print('''
#     Hello віфвіфл "влідфосттвіслов" осрлоровілріотілостіст 'стіфлововволд'
#     іфвоіфвілоі вірсло'віслоі "лорлоіфрсіфлрвл" вловріфлорві іфвіфловрло
#     World від'єднатися
# ''')
# print("""Hello World""")


# Пространство имен строкового обекта
# df = 23
# print('df=', df)
# print('df-', df)
# print(df)
# print('df: ', df)
# print('type(df): ', type(df))
# print('dir(df): ', dir(df))
# print(dir(None))
# print(dir(''))

# Длина строки
# a = "hello world!"
# print(len(a))
# a = "hello \nworld!"
# print('a: ', a)
# print(len(a))

# # Получение єлемента по индексу
# a = "hello world!"
# print(a[-1])
# a = "hello \nworld!"
# print(a[6])

# Перебор стро
# a = "hello world!"
# for i in a:
#     print(i)ки в цикле


# Проверка существует ли подстрока в строке
# txt = "The best things in life are free!"
# print("free" in txt)
# txt = "The best things in life are free!"
# if "free" in txt:
#     print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# print("expensive" in txt)

# txt = "The best things in life are free!"
# print("expensive" not in txt)
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#     print("Yes, 'expensive' is NOT")

# Срези строк
# https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
# b = "Hello,World!"
# print(b[2:6])
# print(b[0])
# print(b[:6])
# print(b[2:])
# print(b[-5:-2])
# print(b[2:9:2])
# print(b[::-1])
# print(b[::-2])
# print(b[:])

# Методи преобразования строк
# a = "Hello, World!"
# print(a.upper())
# a = "Hello, World!"
# print(a.lower())
# a = " Hello, World! "
# print(a.lstrip()) # returns "Hello, World!"
# a = "Hello, world!"
# print(a.replace("H", "J"))
# a = "Hello, World!, dsht"
# print(a.split(" ")) # returns ['Hello', ' World!']

# Обеденение строк (Канкатенация)
# a = "Hello"
# b = "World"
# c = a + b
# print('c: ', c)
# a = "Hello"
# b = " World"
# c = a + b
# print(c)
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# Формотирование строк
# age = 36
# txt = "My name is John, I am " + age
# print(txt)
# age = 36
# txt = "My name is John, I am " + str(age)
# print(txt)

# https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# age = 36
# txt = "My name is John, and I am {}".format(age)
# print(txt)

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# myorder = "I want to pay {2} dollars for {0} pieces of item {1}.".format(quantity, itemno, price)
# print(myorder.format(quantity, itemno, price))

# myorder = f"I want to pay {price} dollars for {quantity} pieces of item {itemno}."
# print(myorder)

# print(f"I want to pay {price} dollars for {quantity} pieces of item {itemno}.")

# # https://pythonworld.ru/osnovy/formatirovanie-strok-operator.html
# myorder = "I want %s pieces of item %s for %s dollars." % (quantity, itemno, price)
# print(myorder)
# print('%d %s, %d %s' % (6, 'bananas', 10, 'lemons'))

# Строковие Методи
# https://www.w3schools.com/python/python_strings_methods.asp
# txt = "hello, and welcome to my world."
# x = txt.capitalize()
# print (x)

# txt = "Hello, And Welcome To My World!"
# x = txt.casefold()
# print(x)

# txt = "banana"
# x = txt.center(20)
# print(x)

# txt = "banana"
# x = txt.center(20, "O")
# print(x)

# txt = "I love apples, apple are my favorite fruit"
# x = txt.count("apple")
# print(x)