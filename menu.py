import complex


def enter():
    print('Выберите тип вводимых данных: ', '1 - Комплексные числа ', '2 - Рациональные числа', sep='\n')
    number_type = int(input())
    if number_type == 1:
        num1 = input('Введите первое число: ')
        num2 = input('Введите второе число: ')
        sign = input('Введите знак действия: ')
        print(complex.count(num1, num2, sign))
    elif number_type == 2:
        num1 = input('Введите первое число: ')
        num2 = input('Введите второе число: ')
        sign = input('Введите знак действия: ')
    #else:

        #count(num1, num2, sign)

