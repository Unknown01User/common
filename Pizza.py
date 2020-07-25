class Factory:
    def get_pizza(self, pizza_type):
        if pizza_type == 1:
            return MushroomPizza()
        elif pizza_type == 2:
            return VegetablePizza()
        elif pizza_type == 3:
            return MeatPizza()
        else:
            print("This type of pizza is not found")


class Pizza:
    def ____init__(self):
        self.type = ""

    def prepare_base(self):
        print("dough is preparing")

    def prepare_ingredients(self):
        pass

    def cook(self):
        self.prepare_base()
        self.prepare_ingredients()
        print(self.type + " is ready!")


class MushroomPizza(Pizza):
    def __init__(self):
        self.type = "Mushroom pizza"

    def prepare_ingredients(self):
        print("Mushroom added")


class VegetablePizza(Pizza):
    def __init__(self):
        self.type = "Vegetable pizza"

    def prepare_ingredients(self):
        print("Vegetable added")


class MeatPizza(Pizza):
    def __init__(self):
        self.type = "Meat pizza"

    def prepare_ingredients(self):
        print("Meat added")


print("choose type of Pizza: \n"
      "1 - mushroom,\n"
      "2 - vegetable,\n"
      "3 - meat\n")
pizza_type = int(input())
print(pizza_type)
factory = Factory
pizza = factory.get_pizza(factory, pizza_type)
pizza.cook()