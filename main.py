"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""
import controler
import view

count = 0


def tax_of_rich():
    controler.rich_tax()
    print(view.print_tax('богатство', 10))
    print(view.print_score(controler.get_score()))


def score():
    view.print_accept()
    print(view.print_score(controler.get_score()))


def tax_of_triple():
    controler.set_score(controler.get_score() * controler.TRIPLE_TAX)
    global count
    count = 0
    print(view.print_tax('3 операции', 3))
    print(view.print_score(controler.get_score()))


while True:
    choice = input(view.get_menu())
    match choice:
        case '1':
            try:
                if controler.check_rich(controler.get_score()):
                    tax_of_rich()
                amount = float(input(view.print_amount_insert()))
                if controler.check_multiple(amount):
                    controler.set_score(controler.get_score() + amount)
                    score()
                    count += 1
                    if count == 3:
                        tax_of_triple()
                else:
                    print(f'{view.print_incorrect()} сумма должна быть кратна 50')
            except ValueError:
                print(f'{view.print_incorrect()} введённые данные неверны')
        case '2':
            try:
                if controler.check_rich(controler.get_score()):
                    tax_of_rich()
                amount = float(input(view.print_amount_take()))
                if controler.check_multiple(amount):
                    controler.set_score(controler.get_score() - amount - controler.percent_of_take(amount))
                    print(view.print_tax('снятие', 1.5))
                    score()
                    count += 1
                    if count == 3:
                        tax_of_triple()
                else:
                    print(f'{view.print_incorrect()} сумма должна быть кратна 50')
            except ValueError:
                print(f'{view.print_incorrect()} введённые данные неверны')
        case '3':
            print('Пока')
            quit()
        case _:
            print('Ты где нашёл эту кнопку')
