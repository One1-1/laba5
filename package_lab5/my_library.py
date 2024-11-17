
def task5_1(input_string):
    '''
    Задание: Дана строка символов. Определить можно ли из ее символов составить выражение вида «3+5=8»

    :param : input_string - вводимое выражение
    :return: None
    '''

    chars = "3+5=8"
    flag = True

    for char in chars:
        if chars.count(char) > input_string.count(char):
            flag = False
            break

    if flag:
        print("Можно составить выражение '3+5=8'")
    else:
        print("Нельзя составить выражение '3+5=8'")


def task5_2(text):
    '''
    Задание: Составить программу циклической перестановки букв в словах текста так, что i-я буква слова становится i+1-ой, а последняя - первой

    :param : text - вводимое слово
    :return: result - результат работы программы
    '''

    words = text.split()

    new_words = []
    for word in words:
        if len(word) > 1:
            new_word = words[-1] + word[:-1]
        else:
            new_word = word
        new_words.append(new_word)

    result = ' '.join(new_words)

    return result

def task5_3(sentence):
    '''
    Напишите программу, которая вводит строку и выводит ее, сокращая каждый раз на 1 символ до тех пор, пока в строке не останется 1 символ

    :param: sentence
    :return: sentence - возвращаемая строка с одним символом
    '''


    if len(sentence) > 0:
        while len(sentence) > 1:
            print(sentence)
            sentence = sentence[:-1]

        print(sentence)
    else:
        print("Строка не должна быть пустой.")

    return sentence


def task5_4(text):
    '''
    Задание: Найти такое слово в первом предложении, которого нет ни в одном из остальных предложений

    :param: text - Вводимый текст
    :return: None
    '''

    text = text.lower()

    sentences = text.split('.')

    sentences_cleaned = []
    for s in sentences:
        stripped_sentence = s.strip()
        if stripped_sentence:
            sentences_cleaned.append(stripped_sentence)

    if len(sentences_cleaned) < 2:
        print("Недостаточно предложений для анализа.")
    else:
        first_sentence = sentences_cleaned[0]
        other_sentences = sentences_cleaned[1:]

        first_words = set(first_sentence.split())

        other_words = set()
        for sentence in other_sentences:
            words = sentence.split()
            for word in words:
                other_words.add(word)

        unique_words = first_words.difference(other_words)

        if unique_words:
            print(unique_words)
        else:
            print("Нет уникальных слов в первом предложении.")



def task5_5(color_id):
    '''
    Написать регулярное выражение, определяющее является ли данная строчка
    шестнадцатеричным идентификатором цвета в HTML. Где #FFFFFF для
    белого, #000000 для черного, #FF0000 для красного и т.д.
    – пример правильных выражений: #FFFFFF, #FF3421, #00ff00.
    – пример неправильных выражений: 232323, f#fddee, #fd2.

    :param: color_id - вводимый идентификатор цвета
    :return: None
    '''

    import re

    pattern = r'^#[0-9A-Fa-f]{6}$|^#[0-9A-Fa-f]{3}$'

    if re.match(pattern, color_id):
        print("Это правильный идентификатор цвета.")
    else:
        print("Это неправильный идентификатор цвета.")


def task5_6(input_string):
    '''
    Задание: Строки, содержащие две буквы «z», между которыми ровно три символа.
    Пример строк, которые подходят: «zabcz», «zzz», «zzxzz». Пример строк,
    которые не подходят: «zz», «zxz», «zzxzxxz»

    :param: None
    :return: None
    '''

    import re

    pattern = r'z.{3}z'

    if re.search(pattern, input_string):
        print("Строка подходит.")
    else:
        print("Строка не подходит.")


def task5_7(text):
    '''
    Задание: Поменять местами два первых слова в тексте. Примеры замен: «this is a text» → «is this a text», «(This, ) is also a text» → «(is, ) This also a text»

    :param: text - вводимый текст
    :return: result - результатт программы
    '''
    import re

    result = re.sub(r'^(\S+)\s+(\S+)', r'\2 \1', text)

    return result










