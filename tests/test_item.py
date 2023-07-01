"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest, src.item

@pytest.fixture
def smart():
    return src.item.Item("Смартфон", 10000, 20)


def item1():
    item1 = src.item.Item("Миелофон", 1000000, 1)
    item1.pay_rate = 0.75
    return item1


def item2():
    item2 = src.item.Item("Патефон", 0.01, 2)
    item2.pay_rate = 0.8
    print(f'\nпроверка payrate в экз.1 {item1().pay_rate},  в экз2 {item2.pay_rate}')
    return item2


def test_smart_init(smart):
    assert smart.price == 10000
    assert smart.quantity == 20


def test_calculate_total_price():

    assert item1().calculate_total_price() == 1000000
    assert item2().calculate_total_price() == 0.02



def test_apply_discount():
    item1= src.item.Item("Миелофон", 1000000, 1)
    item1.pay_rate = 0.75
    assert item1.price == 1000000
    item1.apply_discount()
    assert item1.price == 750000

    item2 = src.item.Item("Патефон", 0.01, 2)
    old_price = item2.price
    item2.apply_discount()
    assert item2.price == round(old_price * item2.pay_rate, 2)


def test_instantiate_from_csv():
    ''' проверяем правильность закачки и создания всех экземпляров в Items из файла ..\\src\\items.csv '''
    nomenkl_was=len(src.item.Item.all)  # замеряем численность экземпляров до закачки
    src.item.Item.instantiate_from_csv()
    assert len(src.item.Item.all) == (nomenkl_was + 5)
    #print( {src.item.Item.all[k].name for k in range(len(src.item.Item.all))})
    assert {'Смартфон', 'Ноутбук', 'Кабель', 'Мышка', 'Клавиатура'}.issubset({src.item.Item.all[k].name for k in range(len(src.item.Item.all))})
    #print(src.item.Item.all[len(src.item.Item.all)-1].name, type(src.item.Item.all[len(src.item.Item.all)-1].price))
    assert src.item.Item.all[len(src.item.Item.all) - 1].name == 'Клавиатура'  # последние по файлу CSV - 5 клавиатур по цене 75
    assert src.item.Item.all[len(src.item.Item.all)-1].price == 75
def test_string_to_number():
    assert src.item.Item.string_to_number('5') == 5
    assert src.item.Item.string_to_number('5.0') == 5
    assert src.item.Item.string_to_number('5.5') == 5
    assert src.item.Item.string_to_number(5.758) == 5

def test_name_setter_and_getter():
    item1= src.item.Item("Глюкометр", 600, 1)
    #print('Был ',item1.name)
    item1.name="Пульсоксиметр"
    #print('Стал ', item1.name)
    assert item1.name == "Пульсоксим" #усекается


test_calculate_total_price()
test_apply_discount()
test_instantiate_from_csv()
test_string_to_number()
test_name_setter_and_getter()
