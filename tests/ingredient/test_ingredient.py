from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    frango = Ingredient('arroz')
    carne = Ingredient('feijao')
    camarao = Ingredient('arroz')

    assert hash(frango) == hash('arroz')
    assert hash(carne) == hash('feijao')
    assert hash(frango) != hash('feijao')

    assert frango == camarao
    assert frango != carne

    assert frango.name == 'arroz'

    assert frango.restrictions == set()
  
    equal = camarao == frango
    assert frango.__eq__(camarao) == equal

    assert frango.__repr__() == "Ingredient('arroz')"

