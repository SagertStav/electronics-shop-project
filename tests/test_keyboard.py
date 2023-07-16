import src.item
import src.phone
import src.keyboard

#ДЗ - множественное наследование (homework-5)

def test_mult_heritage():


   kb = src.keyboard.Keyboard('Dark Project KD87A', 9600, 5)
   assert str(kb) == "Dark Project KD87A"

   assert str(kb.language) == "EN"

   kb.change_lang()
   assert str(kb.language) == "RU"

   # Сделали RU -> EN -> RU
   kb.change_lang().change_lang()
   assert str(kb.language) == "RU"

   kb.language = 'CH'
   # AttributeError: property 'language' of 'Keyboard' object has no setter

test_mult_heritage()