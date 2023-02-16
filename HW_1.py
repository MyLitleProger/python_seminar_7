# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в
# программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все
# в порядке и “Пам парам”, если с ритмом все не в порядке.

# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да
#
# Вывод: Парам пам-пам

def vinni_puh(string: str):
    string_list = list(string.split())
    string_by_word = [i.split('-') for i in string_list]
    count_vowel = 0
    list_count_vowel = []
    for list_item in string_by_word:
        for item in list_item:
            count_vowel += item.count('а')
        list_count_vowel.append(count_vowel)
        count_vowel = 0
    if len(set(list_count_vowel)) == 1 and sum(list_count_vowel) != 0:
        print('Парам пам-пам')
    else:
        print('Пам парам')


#################################################################
def vinni_poh(string: str):
    string = [i.split('-') for i in string.split()]
    count_vowel = [' '.join(i) for i in string]
    count_vowel = [i.count('а') for i in count_vowel]
    return print('Парам пам-пам') if len(set(count_vowel)) == 1 and sum(count_vowel) != 0 else print('Пам парам')


#################################################################

# пара-ра-рам рам-пам-папам па-ра-па-да
# пп-пп рр-рр рррр
# пар-парара па-ра-ра

chant = input('Введите кричалку: ')
print(chant)

vinni_puh(chant)
vinni_poh(chant)
