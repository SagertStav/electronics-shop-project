import src.item
import src.phone

#ДЗ - наследование (homework-4)

def test_subclass():
    # смартфон iPhone 14, цена 120_000, количество товара 5, симкарт 2
    phone1 = src.phone.Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'

    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    item1 = src.item.Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10

    phone1.number_of_sim = 0
    # ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.
    assert phone1.number_of_sim == 2

def test_adding_phone_with_items():
    item1 = src.item.Item("Пейджер", 7, 2)
    print(item1 + 3)
    assert (item1 + 3) == "Возможно сложение по количеству только экземпляров класса Item или Phone"

test_subclass()
test_adding_phone_with_items()