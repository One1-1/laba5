
def task5_1(input_string):
    '''
    Задание: Дана строка символов. Определить можно ли из ее символов составить выражение вида «3+5=8»

    :param : input_string - вводимое выражение
    :return: None
    '''
    import re

    pattern = r'(?=.*3)(?=.*5)(?=.*8)(?=.*\+)(?=.*=)'

    if re.search(pattern, input_string):
        print("Можно составить выражение '3+5=8'")
    else:
        print("Нельзя составить выражение '3+5=8'")


def task5_2(word):
    '''
    Задание: Составить программу циклической перестановки букв в словах текста так, что i-я буква слова становится i+1-ой, а последняя - первой

    :param : word - вводимое слово
    :return: result - результат работы программы
    '''

    import re

    sample = r'\b\w+\b'

    result = re.sub(sample, lambda match: match.group(0)[-1] + match.group(0)[:-1], word)

    return result

def task5_3(sentence):
    '''
    Напишите программу, которая вводит строку и выводит ее, сокращая каждый раз на 1 символ до тех пор, пока в строке не останется 1 символ

    :param: sentence
    :return: sentence - возвращаемая строка с одним символом
    '''
    import re

    while len(sentence) > 1:
        print(sentence)
        sentence = re.sub(r'.$', '', sentence)

    return sentence


def task5_4(text):
    '''
    Задание: Найти такое слово в первом предложении, которого нет ни в одном из остальных предложений

    :param: text - Вводимый текст
    :return: None
    '''
    import re

    sentences = re.split(r'(?<=[.!?]) +', text)
    first_sentence_words = set(re.findall(r'\b\w+\b', sentences[0].lower()))
    other_sentences_words = set()

    for i in range(1, len(sentences)):
        other_sentences_words.update(re.findall(r'\b\w+\b', sentences[i].lower()))

    unique_word = first_sentence_words - other_sentences_words

    if unique_word:
        print("Уникальное слово из первого предложения:", unique_word.pop())
    else:
        print("Нет уникальных слов в первом предложении.")


def task5_5():
    '''
    Написать регулярное выражение, определяющее является ли данная строчка
    шестнадцатеричным идентификатором цвета в HTML. Где #FFFFFF для
    белого, #000000 для черного, #FF0000 для красного и т.д.
    – пример правильных выражений: #FFFFFF, #FF3421, #00ff00.
    – пример неправильных выражений: 232323, f#fddee, #fd2.

    :param: None
    :return: None
    '''
    import re

    pattern = r'^#[0-9A-Fa-f]{6}$'

    test_strings = [
        "#FFFFFF",  # правильный
        "#FF3421",  # правильный
        "#00ff00",  # правильный
        "232323",  # неправильный
        "f#fddee",  # неправильный
        "#fd2",  # неправильный
    ]

    for string in test_strings:
        if re.match(pattern, string):
            print(f"{string} - правильный идентификатор цвета")
        else:
            print(f"{string} - неправильный идентификатор цвета")


def task5_6():
    '''
    Задание: Строки, содержащие две буквы «z», между которыми ровно три символа.
    Пример строк, которые подходят: «zabcz», «zzz», «zzxzz». Пример строк,
    которые не подходят: «zz», «zxz», «zzxzxxz»

    :param: None
    :return: None
    '''
    import re

    strings = [
        "zabcz",
        "zzz",
        "zzxzz",
        "zz",
        "zxz",
        "zzxzxxz"
    ]

    pattern = r'z.{3}z'

    for s in strings:
        if re.fullmatch(pattern, s):
            print(s)

def task5_7(text):
    '''
    Задание: Поменять местами два первых слова в тексте. Примеры замен: «this is a text» → «is this a text», «(This, ) is also a text» → «(is, ) This also a text»

    :param: text - вводимый текст
    :return: result - результатт программы
    '''
    import re

    result = re.sub(r'^(\S+)\s+(\S+)', r'\2 \1', text)

    return result










