from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    one = Dish("salada", 17.90)
    two = Dish("arroz", 19.90)
    three = Dish("arroz", 19.90)
    arroz = Ingredient('arroz')

    with pytest.raises(ValueError):
        Dish('salada', -902)

    assert hash(one) != hash(two)
    assert hash(two) == hash(three)

    assert one.name == 'salada'
    assert one.price == 17.90

    assert two == three
    assert one != three

    one.add_ingredient_dependency(arroz, 15)
    assert arroz in one.get_ingredients()

    assert one.get_restrictions() == set()

    assert one.__repr__() == "Dish('salada', R$17.90)"
