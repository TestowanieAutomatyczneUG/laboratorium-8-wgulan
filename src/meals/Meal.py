import json
import requests


class Meal:

    def get_meal_by_name(self, name):
        if type(name) == str:
            name_query = name.replace(" ", "_")
            meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={name_query}").json()
            return meal["meals"][0]
        else:
            raise TypeError("Meal name is not a string")

    def get_meal_by_id(self, id):
        if type(id) == str or type(id) == int:
            meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}").json()
            return meal["meals"][0]
        else:
            raise TypeError("Meal name is not a string nor int")

    def get_random_meal(self):
        meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/random.php").json()
        return meal["meals"][0]

    def filter_meals_by_main_ingredient(self, ingredient):
        if type(ingredient) == str:
            ingredient_query = ingredient.replace(" ", "_")
            meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient_query}").json()
            return meal["meals"]
        else:
            raise TypeError("Ingredient is not a string")

    def get_all_meal_categories(self):
        categories = requests.get(f"https://www.themealdb.com/api/json/v1/1/categories.php").json()
        return categories["categories"]

    def get_all_meal_areas(self):
        categories = requests.get(f"https://www.themealdb.com/api/json/v1/1/list.php?a=list").json()
        return categories["meals"]

    def get_all_ingredients(self):
        ingredients = requests.get(f"https://www.themealdb.com/api/json/v1/1/list.php?i=list").json()
        return ingredients["meals"]

    def filter_meals_by_category(self, category):
        if type(category) == str:
            category_query = category.replace(" ", "_")
            meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category_query}").json()
            return meal["meals"]
        else:
            raise TypeError("Category is not a string")

    def filter_meals_by_area(self, area):
        if type(area) == str:
            area_query = area.replace(" ", "_")
            meal = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?a={area_query}").json()
            return meal["meals"]
        else:
            raise TypeError("Ingredient is not a string")