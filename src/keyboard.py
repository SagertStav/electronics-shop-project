import src.item

# Реализуем дополнительный функционал по хранению и изменению раскладки клавиатуры в отдельном классе-миксине, который “подмешивается” в цепочку наследования класса `Keyboard`.
class Mixing_keyboard:

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        self.__language = 'RU' if self.__language == 'EN' else 'EN'
        return self


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__language = 'EN'


class Keyboard(src.item.Item, Mixing_keyboard):
    """
    Класс для представления такой категории товаров в магазине как клавиатуры
    """

    # Переопределяем метод базового класса
    def __init__(self,  name: str, price: float, quantity: int) -> None:
        """
        Создание наследуемого от Item экземпляра класса Keyboard.
        :param name: Название смартфона.
        :param price: Цена за единицу.
        :param quantity: Количество товара в магазине.
        :param language: EN/RU
        """

        super().__init__(name, price, quantity)
        Mixing_keyboard.__init__(self)

