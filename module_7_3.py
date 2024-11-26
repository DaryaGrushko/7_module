#Оператор "with"
#Задача "Найдёт везде"

import re
class WordsFinder:
    count_call = 0
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        array_words = []
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text_file = file.read().lower()
                marks = str.maketrans(dict.fromkeys(list(",.=!?;:-"), ""))
                new_str = text_file.translate(marks)
                split_str = new_str.split()
                all_words[file_name] = split_str
        return all_words

    def find(self, word):
        dict = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                position = words.index(word.lower())+1
                dict[name] = position
        return dict

    def count(self, word):
        count = 0
        dict_count = {}
        all_words = self.get_all_words().items()
        for name, words in  all_words:
            element_count = len([item for item in words if item==word.lower()])
            dict_count[name] = element_count
        return dict_count

finder2 = WordsFinder('test_file.txt', 'test_file2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


