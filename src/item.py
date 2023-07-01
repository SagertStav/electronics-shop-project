import csv

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
        #print(__name__)
        try:
           with open('..\src\items.csv', newline='') as csvfile:
               #для run проходЯт только ДВЕ точки '..\src\items.csv', а для тестов в терминале (poetry run pytest --cov) - одна
               for row in csv.DictReader(csvfile):
                   Item(**row)
        except FileNotFoundError:
            with open('.\src\items.csv', newline='') as csvfile:
                for row in csv.DictReader(csvfile):
                    Item(**row)


