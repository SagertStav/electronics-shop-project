import src.item
class Phone(src.item.Item):
    """
    Класс для представления такой категории товаров в магазине как телефон
    """



    # Переопределяем метод базового класса
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: bytes = 1) -> None:
        """
        Создание наследуемого от Item экземпляра класса Phone.

        :param name: Название смартфона.
        :param price: Цена за единицу.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: максимальное число SIM-карт в смартфоне.
        """

        self.__number_of_sim = self.number_of_sim = number_of_sim
        super().__init__(name, price, quantity)
        print(f"смартфон {name}, цена {price:_.0f}, количество товара {quantity}, симкарт {number_of_sim}")


    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if (not isinstance(value, int | bytes)) or value <=0:
            #raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self._number_of_sim = value


    def __repr__(self):
        return f"Phone('{self.name}', {int(self.price)}, {self.quantity}, {self.number_of_sim})"

