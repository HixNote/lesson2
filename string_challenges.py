# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а',0))


# Вывести количество гласных букв в слове
word = 'Архангельск'
print(len([i for i in word.lower() if i in  ["а","у","е","о","я","ы","и","ю","э"]]))



# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print('\n'.join(i[0] for i in sentence.split(' ')))


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
a=[len(i) for i in [i for i in sentence.split(' ')]]
print(sum(a)//len(a))
