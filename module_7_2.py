#Позиционирование в файле
import io
from pprint import pprint

def custom_write(file_name, strings):
    name = 'text.txt'
    bytes_start_string = 0
    strings_positions = {}
    #print ('file_name = ', file_name, 'strings = ', strings)
    count_string = 0
    for string in strings:
        count_string +=1

        #print ('string = ', string, '////count_string = ', count_string)
        file = open(name, 'r', encoding='utf-8') #открыть файл
        file.read()  # прочитать файл
        bytes_start_string = file.tell() # считать позицию курсора
        #print ('bytes_start_string = ', bytes_start_string)
        file.close()
        file = open(name, 'a', encoding='utf-8')  # открыть файл
        file.seek(bytes_start_string) # передвинуть курсор на bytes_start_string
        file.write(f"{string}\n") #записать текст в файл

        strings_positions[(count_string, bytes_start_string)] = string
       # print ('----------------')

    #for key, value in strings_positions.items():
    #    print (f"{key}: {value}")
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