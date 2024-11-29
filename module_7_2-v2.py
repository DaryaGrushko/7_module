#Позиционирование в файле
import io
from pprint import pprint

def custom_write(file_name, strings):
    
    name = file_name
    bytes_start_string = 0
    count_string = 0
    strings_positions = {}

    for string in strings:

        count_string += 1
        if count_string==1:

            file = open(name, 'w', encoding='utf-8')  # открыть файл
            bytes_start_string = file.tell()  # считать позицию курсора
            file.write(f"{string}\n")  # записать текст в файл
            file.close()
            strings_positions[(count_string, bytes_start_string)] = string

        else:

            file = open(name, 'r', encoding='utf-8')  # открыть файл
            file.read()  # прочитать файл
            bytes_start_string = file.tell()  # считать позицию курсора
            file.close()

            file = open(name, 'a', encoding='utf-8')  # открыть файл
            file.seek(bytes_start_string)  # передвинуть курсор на bytes_start_string
            file.write(f"{string}\n")  # записать текст в файл
            file.close()
            strings_positions[(count_string, bytes_start_string)] = string

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)