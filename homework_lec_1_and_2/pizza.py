class Pizza:
    def prepare_base(self):
        print("Start cooking!")
        print("On the basis we put: ")

    def prepare_ingredients(self):
        pass

    def __cook(self):
        pass


class PizzaMeat(Pizza):
    def prepare_ingredients(self):
        print("sauce, onions,tomato, cucumbers, meal, olives and sprinkle with cheese!")
        self.__cook()

    def __cook(self):
        print("We send it to the oven for 20 minutes...")
        print("Meat pizza is done! Enjoy!")


class PizzaVegetable(Pizza):
    def prepare_ingredients(self):
        print("sauce, tomato, mozzarella, basil and sprinkle with cheese!")
        self.__cook()

    def __cook(self):
        print("We send it to the oven for 15 minutes...")
        print("Vegetable pizza is done!")


class PizzaMushroom(Pizza):
    def prepare_ingredients(self):
        print("sauce, mushrooms, onions, dill and sprinkle with cheese!")
        self.__cook()

    def __cook(self):
        print("We send it to the oven for 17 minutes...")
        print("Mushroom pizza is done!")


# scenario
while 1:
    try:
        pizza_type = int(input("Enter type's pizza(1-meat, 2-vegetable, 3-mushroom) for cooking: "))
        break
    except ValueError:
        print("Incorrect input! It isn't number.")

if pizza_type == 1:
    pizza_meat = PizzaMeat()
    pizza_meat.prepare_base()
    pizza_meat.prepare_ingredients()

elif pizza_type == 2:
    pizza_vegetable = PizzaVegetable()
    pizza_vegetable.prepare_base()
    pizza_vegetable.prepare_ingredients()

elif pizza_type == 3:
    pizza_mushroom = PizzaMushroom()
    pizza_mushroom.prepare_base()
    pizza_mushroom.prepare_ingredients()

else:
    print("This number isn't on the menu! Good bay!")
