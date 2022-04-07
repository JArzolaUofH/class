class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):

        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    firstitem = FoodItem()

    item_name = input()
    total_fat = float(input())
    total_carbs = float(input())
    total_protein = float(input())

    seconditem = FoodItem(item_name, total_fat, total_carbs, total_protein)

    num_servings = float(input())

    firstitem.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, firstitem.get_calories(num_servings)))

    print()

    seconditem.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, seconditem.get_calories(num_servings)))
