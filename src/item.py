import csv
import os
import src.eshop_exceptions

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    @staticmethod
    def string_to_number(one_str):
      ''' string_to_number() возвращает целое представление числа из строкового '''
      return int(float(one_str))

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = float(price)
        self.quantity = int(quantity) #не дает использовать string_to_number(quantity) - is not defined
        self.all.append(self)

    def __repr__(self):
        """ представление экземпляра класса Item в отладке: Item('Товар', цена, количество """
        return f"Item('{self.name}', {int(self.price)}, {self.quantity})"

    def __str__(self):
        """ представление экземпляра класса Item для пользователя, при печати: 'Товар' """
        return self.name


    # Геттер для name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        """Метод срабатывает при операции присваивания и усекает название товара до 10 символов """
        self.__name=name[:10]
        if len(name)>10:
            print(f"Предупреждаю: название товара '{name}' усечено до 10 символов: '{self.__name}'!")


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return round(self.price*self.quantity,2)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        #self.price *= self.pay_rate  # так не округляет
        self.price = round(self.pay_rate * self.price, 2)
        #print(f"\nПроверка измененности цены в самой фикстуре после её выполнения: price={self.price}")

    @classmethod
    def instantiate_from_csv(cls):
        ''' instantiate_from_csv() - класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_ '''
        cls.all.clear() # очищаю все экземпляры из списка

        try:
           with open('..\src\items.csv' if os.path.isfile('..\src\items.csv') else '.\src\items.csv', newline='') as csvfile:
               #для run проходЯт только ДВЕ точки '..\src\items.csv', а для тестов в терминале (poetry run pytest --cov) - одна
               for row in csv.DictReader(csvfile):
                   Item(**row)

        except FileNotFoundError:
            raise src.eshop_exceptions.CSV_is_absent("Отсутствует файл items.csv")
            #print(e)
        except TypeError: #len(**row) != 3:
            raise src.eshop_exceptions.CSV_is_harmed("Файл items.csv поврежден")
            print("Файл items.csv поврежден")




    def __add__(self, other):
        import src.phone
        if isinstance(other, (Item, src.phone.Phone)):
           return self.quantity + other.quantity
        else:
           s = "Возможно сложение по количеству только экземпляров класса Item или Phone"
           print(s)
           return s

