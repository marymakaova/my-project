from random import *
bot_math = [3] * 1 + [4] * 3 + [5] * 6 + [6] *10 + [7] * 15 + [8] * 21 + [9] * 28 + [10] * 36 + [11] * 36
bot_lucky = [x for x in range(3, 19)]
cbm, cpl, cbl = 0, 0, 0
bpl, bbm, bbl = 1000, 1000, 1000
minbet = 100

while True:
    if bpl < minbet:
        print('Вы банкрот,Game over!')
        exit()
    if bbl < minbet:
        print('bot_lucky выбывает из игры')
        flag1 = False
        exit()
    if bbm < minbet:
        print('bot_math выбывает из игры')
        flag2 = False
        exit()
        
    stavka_bm, stavka_bl = 0, 0
    while True:
        stavka_pl = input(f'Сделайте вашу ставку от {minbet} до {min(bpl, bbm, bbl)}: ')
        if stavka_pl.isdigit() and int(stavka_pl) >= minbet and int(stavka_pl) <= min(bpl, bbm, bbl):
            stavka_pl = int(stavka_pl)
            if bbm <= 500 and cbm == min(bpl, bbm, bbl):
                stavka_bm = stavka_pl + stavka_pl // 2
                if stavka_bm <= bbm:
                    print(f'bot_math увеличивает ставку до {stavka_bm}')
                    break
                else:
                    print('bot_math идет ва-банк')
            else:
                stavka_bm = stavka_pl
                print('bot_math поддерживает вашу ставку')
                break
        else:
            print('Неправильный размер ставки')
                
    while True:
        bet_pl = input('Введите число от 3 до 18:')
        if bet_pl.isdigit() and 3 <= int(bet_pl) <=18:
            bet_pl = int(bet_pl)
            break
        else:
            print('Не правильный ввод')
    bet_bot_math = choice(bot_math)
    bet_bot_lucky = choice(bot_lucky)
    c1 = randint(1, 6)
    c2 = randint(1, 6)
    c3 = randint(1, 6)
    summa = c1 + c2 + c3
    if abs(summa - bet_pl) < abs(summa - bet_bot_math) <= abs(summa - bet_bot_lucky):
        print('Вы победили!')
        cpl += 1
        bpl += 3 * stavka_bm
    elif abs(summa - bet_bot_math) < abs(summa - bet_pl) <= abs(summa - bet_bot_lucky):
        print('Победил bot_math')
        cbm += 1
        bbm += 3 * stavka_bm
    elif abs(summa - bet_bot_lucky) < abs(summa - bet_pl) <= abs(summa - bet_bot_math):
        print('Победил bet_bot_lucky')
        cbl += 1
        bbl += 3 * stavka_bm
    else:
        print('Ничья')
        bbm += stavka_bm
        bpl += stavka_bm
        bbl += stavka_bm
    print(f'bot_math поставил на{bet_bot_math},bot_lucky поставил на{bet_bot_lucky}, вы поставили на{bet_pl}')
    print('............................................................')
    print(f'Игрок:{cpl} | bot_math:{cbm} | bot_lucky: {cbl}')
    print(f'Банк игрока {bpl} | Банк bot_math {bbm} | Банк bot_lucky {bbl}')
    print(f'Cумма: {summa}')
