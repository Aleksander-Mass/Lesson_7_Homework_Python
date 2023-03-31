'''
### Задание 2

Напишите функцию группового переименования файлов. Она должна:

принимать параметр желаемое конечное имя файлов. 
При переименовании в конце имени добавляется порядковый номер.

принимать параметр количество цифр в порядковом номере.

принимать параметр расширение исходного файла. 

Переименование должно работать только для этих файлов внутри каталога.

принимать параметр расширение конечного файла.

принимать диапазон сохраняемого оригинального имени. 
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного 
имени файла. К ним прибавляется желаемое конечное имя, 
если оно передано. Далее счётчик файлов и расширение.
'''

import os
from pathlib import Path


def file_rename(new_name: str, number: int, extension: str, letters_range: list) -> None:
    directory = Path(Path().cwd())
    number = (10 ** number) // 10
    for file in os.listdir(directory):
        min_l, max_l = letters_range[0], letters_range[1]
        if file.split('.')[-1] == extension:
            os.rename(f'{directory}/{file}', f'{directory}/{file[min_l: max_l]}{new_name}{number}.{extension}')
            number = number + 1


if __name__ == '__main__':
    p = Path(Path().cwd())
    new_name = input('Имя желаемых файлов: ')
    count_numbers = int(input('Кол-во цифр в порядковом номере: '))
    ext = input("Для какого расширения применить: ")

    letters_range = [int(input("Номер буквы с которой сохранить имя ")),
                     int(input("Номер буквы с которой закончить сохранять имя "))]

    file_rename(new_name, count_numbers, ext, letters_range)