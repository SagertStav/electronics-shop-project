import src.item

# Реализуем дополнительный функционал по хранению и изменению раскладки клавиатуры в отдельном классе-миксине, который “подмешивается” в цепочку наследования класса `Keyboard`.
class Mixing_keyboard:
    def __init__(self):
        self.__language = 'EN'





class Keyboard(src.item.Item, Mixing_keyboard):
    """
    Класс для представления такой категории товаров в магазине как клавиатуры
    """

    # Переопределяем метод базового класса
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание наследуемого от Item экземпляра класса Keyboard.

        :param name: Название смартфона.
        :param price: Цена за единицу.
        :param quantity: Количество товара в магазине.
        :param language: EN/RU
        """

        self.__language = 'EN'
        super().__init__(name, price, quantity)

    @property
    def language(self):
        return self.__language


    @language.setter
    def language(self, value):
        print("Изменение раскладки клавиатуры возможно только посредством метода change_language")
        print("(Вместо: # AttributeError: property 'language' of 'Keyboard' object has no setter)")
        return self.__language


    def change_lang(self):
        self.__language = 'RU' if self.__language=='EN' else 'EN'
        return self




