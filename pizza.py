class Pizza:
    ingredients = []
    name = ""

    def get_name(self):
        return self.name

    def prepare_dough(self):
        print("The dough is ready!")

    def add_ingredients(self):
        pass


    def bake_pizza(self):
        print("The pizza is baking!")


    def cook(self):
        self.prepare_dough()
        self.add_ingredients()
        self.bake_pizza()
        print(self.get_name() + " is ready!")


class MushroomPizza(Pizza):
    ingredients = ["mushrooms", "onion", "cheese"]
    name = "Mushroom pizza"

    def add_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient + " is added!")


class MeatPizza(Pizza):
    ingredients = ["sausage", "bacon", "ham", "olives", "tomato", "cheese"]
    name = "Meat pizza"

    def add_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient + " is added!")



class VegetablesPizza(Pizza):
    ingredients = ["olives", "tomato", "onion", "pickled cucumber", "paprika", "potato", "cheese"]
    name = "Vegetables pizza"

    def add_ingredients(self):
        for ingredient in self.ingredients:
            print(ingredient + " is added!")


while True:
    print("Please chose mushroomPizza or meatPizza or vegetablesPizza and enter the name.")
    pizzaName = input();
    if (not pizzaName):
        break
    else:
        if (pizzaName == "mushroomPizza"):
            mushroomPizza = MushroomPizza()
            mushroomPizza.cook()
        elif (pizzaName == "meatPizza"):
            meatPizza = MeatPizza()
            meatPizza.cook()
        elif (pizzaName == "vegetablesPizza"):
            vegetablesPizza = VegetablesPizza()
            vegetablesPizza.cook()
        else:
            print("Such pizza isn`t exist, please try again!")

