class InstantiateCSVError(Exception):
    """Общий класс исключений, которые могут возникнуть при инициализации Items закачкой
     товаров из файла item.csv """
    def __init__(self, *args, **kwargs):
            self.message = args[0] if args else 'Неизвестная ошибка скрипта.'

    def __str__(self):
        return self.message


class CSV_is_absent(InstantiateCSVError):
     """Класс исключения при отсутствии файла """

     def __init__(self, *args, **kwargs):
         self.message = args[0] if args else 'Файл отсутствует'
         print("Исключение запускалось:", self.message)

class CSV_is_harmed(InstantiateCSVError):
        """Класс исключения при повреждении файла
        (в структуре таблицы не все строки представлены 3 заполненными графами"""

        def __init__(self, *args, **kwargs):
            self.message = args[0] if args else 'Ошибка в записях файла'
            print("Исключение вызывалось:", self.message)