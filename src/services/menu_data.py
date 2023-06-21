# # Req 3

import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.load(source_path)

    def load(self, source_path):
        with open(source_path, newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                dish_name = line[0]
                dish_price = float(line[1])
                dish_ingredient = line[2]
                dish_quantity = float(line[3])

                ingredient = Ingredient(dish_ingredient)
                self.ingredients.add(ingredient)

                dish = self._get_dish(dish_name, dish_price)
                dish.add_ingredient_dependency(ingredient, dish_quantity)

    def _get_dish(self, name, price):
        for dish in self.dishes:
            if dish == Dish(name, price):
                return dish
        dish = Dish(name, price)
        self.dishes.add(dish)
        return dish
