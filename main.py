"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from package_lab5.my_library import task5_1, task5_2, task5_3, task5_4, task5_5, task5_6, task5_7


def menu():
    """
    Функция предлагает выбор номера задания\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
    """

    choice_task = int(input('Выберите номер задания в лабороторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()

        match choice:

            case 1:
                input_string = input('Введите строку: ')
                task5_1(input_string)
            case 2:
                text = input('Введите слово: ')
                print(task5_2(text))
            case 3:
                sentence = input("Введите строку: ")
                print(task5_3(sentence))
            case 4:
                text = input('Введите небольшой текст: ')
                task5_4(text)
            case 5:
                color_id = input("Введите шестнадцатеричный идентификатор цвета: ")
                task5_5(color_id)
            case 6:
                input_string = input("Введите строку: ")
                task5_6(input_string)
            case 7:
                text = input('Введите несколько предлложений: ')
                print(task5_7(text))
            case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

