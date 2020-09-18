
class Recipe:

    def __init__(self, recipe_name):
        self.__recipe_name = recipe_name
        self.__ingredient_name = None
        self.__ingredient_unit = None

    def add_ingredients(self, ingredient_name):
        pass

    def remove_ingredients(self, ingredient_name):
        pass

    def show_recipe(self, recipe_name):
        pass
