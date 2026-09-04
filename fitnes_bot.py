

WATER_PER_KG = 30 #Постоянная обозначающая кол-во мл. воды на кг. веса человека

print("Добрый день! Я Мвп, и я ваш бот-помошник!")
name = input("А как, я могу обращаться к вам? ")
name = name.title()              #Команда для написания Имени с большой буквы

print(name, "приятно познакомиться! ")
age = input ("Сколько вам лет? ")
age = int(age)
 # конструкция на случай если пользователь введет данные с ',', а не с '.'
try: 
    height = input("Пожалуйста, укажите свой Рост в Метрах: ")
    height = float(height)
    weight = input("А теперь вес в Килограммах: ")
    weight = float(weight)
except ValueError:
    print("При указании роста и веса используйте точки для дробной части!")
    height = input("Пожалуйста, укажите свой Рост в Метрах: ")
    height = float(height)
    weight = input("А теперь вес в Килограммах: ")
    weight = float(weight)
             # расчёт индекса массы тела
bmi = weight / (height ** 2)
bmi = round(bmi, 1)
         # расчёт количества воды рекомендованного к потреблению в сутки
water_ml = weight * WATER_PER_KG
water_l = water_ml / 1000
water_l = round(water_l, 1)
                            # Сводный блок расчетов
print("-"*41)
print(f"|Отчет для пользователя: {name} ({age} г.)  |")
print(f"|Твой Индекс Массы Тела: {bmi}           |")
print(f"|Рекомендуемая норма воды: {water_l} л. в день|")
print("-"*41)
print("Расчет окончен. Будьте здоровы!")
