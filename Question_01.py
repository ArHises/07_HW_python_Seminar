"""
Задача 34:  
    Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
    Поскольку разобраться в его кричалках не настолько просто, 
    насколько легко он их придумывает, Вам стоит написать программу. 
    Винни-Пух считает, что ритм есть, 
    если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
    Фраза может состоять из одного слова, 
    если во фразе несколько слов, то они разделяются дефисами. 
    Фразы отделяются друг от друга пробелами. 
    Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
    В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
    если с ритмом все не в порядке

*Пример:*

**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    

**Вывод:** Парам пам-пам  

"""

poem = 'пара-ра-рам рам-пам-папам па-ра-па-да'
poem = list(poem.split())
# print(poem)

vowels = {'а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы'}

def vowels_len_word(word, vowels):
    return len(list(filter(lambda char: char in vowels, word)))
# print(vowels_len_word(poem[0], vowels))

# def build_rhythm(poem, vowels):
#     return list(vowels_len_word(word, vowels) for word in poem)

build_rhythm = lambda poem, vowels: list(vowels_len_word(word, vowels) for word in poem)
# print(build_rhythm(poem, vowels))

def chech_rhythm(poem):
    return all(num ==  poem[0] for num in poem)

if chech_rhythm(build_rhythm(poem, vowels)):
    print("Парам пам-пам")
else:
    print("Пам парам")


    
