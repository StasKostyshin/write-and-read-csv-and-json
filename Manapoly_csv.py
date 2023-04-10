import random
import csv
import json

################################# Кто больше #######################################№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
def json_write(): # Функция дли записи в  формате JSON
    with open('Shop.json', 'w', encoding='UTF-8') as sh_j: # откроем для записи 'w'
        json.dump(data, sh_j, indent=2, ensure_ascii=False) # Записшем данные из переменной data в файл

def json_read(): # Функция для чтения файла JSON
    with open('Shop.json', 'r', encoding='utf-8') as sh_j: # Откроем для чтения файл
        all_sh_j = json.load(sh_j) #Откроем прочитав полностью
        print(all_sh_j)
        return all_sh_j["В сумме составило"][-1]

def csv_write(): # Функция для записи в csv формате
    with open('Shop.csv', 'w', newline='\n') as sh_c: # откроем для записи
        wr = csv.DictWriter(sh_c, fieldnames=text_in)
        wr.writeheader()
        wr = csv.writer(sh_c)
        text = ['На сумму', sum(sale_in), 'монет']
        wr.writerow(text)

def csv_read(): # Функция для чтения csv файла
    with open('Shop.csv', 'r', newline='') as sh_c:
        wr = csv.reader(sh_c)
        for row in wr:
            print(', '.join(row))
        return row[1]

def game(money):# Функция пользовательских покупок
    sale = random.randint(0,12)
    if sale == 0:
        print('вы попали в налогувую с вас сняли 100 монет')
        money -= 100
    for i in list_all_:
        if sale == i:
            print(f'Вы в точке {list_all_.get(i)[0]}')
            sale_m = input('Хотите приобрести её акции ? 1.Да 2.Нет: ')
            if sale_m == '1':
                if money > list_all_.get(i)[1]:
                    money -= list_all_.get(i)[1]
                    text_in.append(list_all_.get(i)[0]) # додавим в список text_in значение из list_all_.get(i)[0]
                    sale_in.append(list_all_.get(i)[1]) # добавим в список sale_in значение из list_all_.get(i)[1]
                    csv_write() # запустим функцию записи в csv
                else:
                    print('Не хватает финансов')
                break
            else:
                pass
    return money

def game_com(money_com): # Функция игрока
    a = 0
    print('Ход игрока')
    sale = random.randint(1, 12)
    sale_com = random.randint(1, 2)
    for i in list_all_:
        if sale == i:
            print('Игрок в ', list_all_.get(i)[0])
            if sale_com == 1:
                print(f'Игрок приобрёл акции: {list_all_.get(i)[0]}')
                comp_sale.append(list_all_.get(i)[0]) # Добавим в список comp_sale значение из list_all_.get(i)[0]
                cash.append(list_all_.get(i)[1]) # Добавим в список cash значение из list_all_.get(i)[1]
                summa_cash.append(sum(cash)) # Добавим в список summa_cash значение сумму значений из списка cash
                json_write()
            else:
                print('Игрок пропустил ход находясь', {list_all_.get(i)[0]})
    return money_com


def start(money, money_com):
    while money > 0 and money_com > 0:
        money += 20
        money_com += 20
        money = game(money)
        money_com = game_com(money_com)

list_all_= {1: ['Точка на рынке', 10],
            2: ['Ларёк на Жданах', 15],
            3: ['Сайгон на Экспобеле', 20],
            4: ['Магазин обувиЛуч', 23],
            5: ['Магазин Мега топ', 26],
            6: ['Марко', 30],
            7: ['Магазин Орлан', 33],
            8: ['ЕвроОпт', 40],
            9: ['Соседи', 42],
            10: ['Гиппо', 55],
            11: ['Корона', 66],
            12: ['ДанаМол', 75]
            }

money_com = 200
money = 200
text_in = []
text_int = []
sale_in = []
comp_sale = []
cash = []
summa_cash = []

data = {'Объект': comp_sale,'Были куплены игроком по ценам': cash, 'В сумме составило': summa_cash} # Данные для записи в JSON

start(money, money_com)
a = json_read()
b = csv_read()

c = int(b) # Переведём значение из csv файла из строкового в числовое
if c > a:
    print('Вы потратили больше монет на покупки, Вы победили')
else:
    print('Игрок потратил польше на покупки, Комп выиграл')

