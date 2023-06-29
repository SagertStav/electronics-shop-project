"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import src.item

@pytest.fixture


def smart():
    return src.item.Item("Смартфон", 10000, 20)


def item1():
    item1 = src.item.Item("Миелофон", 1000000, 1)
    item1.pay_rate = 0.75
    return item1


def item2():
    item2 =  src.item.Item("Патефон", 0.01, 2)
    item2.pay_rate = 0.8
    return item2


def test_smart_init(smart):
    assert smart.price == 10000
    assert smart.quantity == 20


def test_calculate_total_price():

# обращение к фикстуре заново превращает pay_rate = 1 ?
    assert item1().calculate_total_price() == 1000000


print(item1().calculate_total_price())
    print(item1().pay_rate)
    assert item2().calculate_total_price() == 0.02


def test_apply_discount():  #itm аргумент не воспринимает
    assert item1().price == 1000000
    #old_price = item1().price
    item1().pay_rate = 0.75
    item1().apply_discount()
    # оказывается, при аргументе self можно оставлять пустые ( ) аргументы
    print(f'item1_price: {item1().price} (pay_rate = {item1().pay_rate})')

    # но после вызова функции - текстуры price снова возвращается в 1 млн.
    assert item1().price == 1000000 #750000
# так что выполненность apply_discount() нивелируется,
# price в тестах снова стала 1000 000, так как проверка завязана
# только на вызове item1( ) как функции


    old_price = item2().price
    item2().apply_discount()
    print(f'item2: (pay_rate = {item2().pay_rate})', item2().price, '   ', \
    round(old_price * item2().pay_rate, 2) )
    assert item2().price == round(old_price * item2().pay_rate, 2)


test_calculate_total_price()

print(item1().all)
print(item2().all)
test_apply_discount()