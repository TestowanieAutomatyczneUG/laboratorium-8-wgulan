import unittest
from meals.Meal import *

class MealTest(unittest.TestCase):
    def setUp(self):
        self.temp = Meal()

    def test_get_meal_by_name(self):
        self.assertEqual(self.temp.get_meal_by_name("arrabiata")['idMeal'], '52771')

    def test_disallow_get_meal_by_name_not_a_string(self):
        self.assertRaises(TypeError, self.temp.get_meal_by_name, 123)

    def test_get_meal_by_id_string(self):
        self.assertEqual(self.temp.get_meal_by_id('52771')['strMeal'], 'Spicy Arrabiata Penne')

    def test_get_meal_by_id_int(self):
        self.assertEqual(self.temp.get_meal_by_id(52771)['strMeal'], 'Spicy Arrabiata Penne')

    def test_disallow_get_meal_by_name_not_a_string_or_int(self):
        self.assertRaises(TypeError, self.temp.get_meal_by_id, {})

    def test_get_random_meal_data_length_equals_51(self):
        self.assertEqual(len(self.temp.get_random_meal()), 51)

    def test_filter_meals_by_main_ingredient(self):
        self.assertEqual(self.temp.filter_meals_by_main_ingredient('chicken breast')[0]['strMeal'], 'Chick-Fil-A Sandwich')

    def test_filter_meals_by_main_ingredient_not_a_string(self):
        self.assertRaises(TypeError, self.temp.filter_meals_by_main_ingredient, 123)

    def test_get_all_meal_categories_num_of_categories_is_14(self):
        self.assertEqual(len(self.temp.get_all_meal_categories()), 14)

    def test_get_all_meal_areas_num_of_areas_is_25(self):
        self.assertEqual(len(self.temp.get_all_meal_areas()), 25)

    def test_get_all_ingredients_num_of_ingredients_is_571(self):
        self.assertEqual(len(self.temp.get_all_ingredients()), 571)

    def test_filter_meals_by_category(self):
        self.assertEqual(self.temp.filter_meals_by_category('seafood')[0]['strMeal'], 'Baked salmon with fennel & tomatoes')

    def test_filter_meals_by_main_category_not_a_string(self):
        self.assertRaises(TypeError, self.temp.filter_meals_by_category, [])

    def test_filter_meals_by_area(self):
        self.assertEqual(self.temp.filter_meals_by_area('canadian')[0]['strMeal'], 'BeaverTails')

    def test_filter_meals_by_main_area_not_a_string(self):
        self.assertRaises(TypeError, self.temp.filter_meals_by_area, 123)

    def tearDown(self):
        self.temp = None

