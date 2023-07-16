import pytest
import src.item
import src.eshop_exceptions
import os
import shutil
import pathlib

tf = '..\src\items.csv' if os.path.isfile('..\src\items.csv') else \
    ('.\src\items.csv' if os.path.isfile('.\src\items.csv') else '')


def test_csv_is_absent():
    """ Моделируем отсутствие файла item.csv """
    # Копия файла - в item_.csv
    if tf != '':                 #если файл есть-удалим его
        print("Удалим ",tf)
        os.remove(tf)

    with pytest.raises(src.eshop_exceptions.CSV_is_absent, match='Отсутствует файл items.csv'):
        src.item.Item.instantiate_from_csv()

    #затем после прохождения теста восстановим файл из копии
    print("Воозвращаемся к работе теста для восстановления файла из ", tf.replace('items.csv','items_.csv'))
    if tf != '':  # если файл был удален - восстановим его
        shutil.copyfile(tf.replace('items.csv','items_.csv'),tf)


def test_csv_is_harmed():
    """ Моделируем повреждение ожидаемой структуры данных в файле items.csv """
    new_line="\nНовая строка"
    print("Проба:",tf)
    with open(tf, 'a') as f:
        f.write(new_line)

    with pytest.raises(src.eshop_exceptions.CSV_is_harmed, match='Файл items.csv поврежден'):
       src.item.Item.instantiate_from_csv()
       #shutil.copy2(tf.replace('items.csv','items_.csv'),tf)  - похоже, во вторую запись трассировка в этом уровне уже не заходит

    shutil.copy2(tf.replace('items.csv','items_.csv'),tf)  # перезаписываем "поврежденный" файл нормальным при выходе из теста


test_csv_is_absent()
test_csv_is_harmed()
