class Pizza_Vegan:
    def dough():
        print("Dough-free dough")
    def vegetables():
        print("Add vegetables")
    def ingredients():
        print( "Add Pomidors")
    def sauce():
        print( "Without sauce")
class Dough:
    def dough_on_choice(dough):
        if dough == "A":
            print("I make thick dough")
        elif dough == "B":
            print("I make thin dough")
        elif dough == "C":
            print("I make rye dough")
class Sauce:
    def sauce_on_choice(sauce):
        if sauce == "A":
            print("I add chili sauce")
        elif sauce == "B":
            print("I add garlic honey sauce")
        elif sauce == "C":
            print("I add salsa sauce")
class Cheese:
    def cheese():
        print("Add cheese")
class Pizza_Mushroom(Pizza_Vegan, Dough, Sauce, Cheese):
    def ingredients():
        print( "Add Mushroom")

class Pizza_Meat(Pizza_Vegan, Dough, Sauce, Cheese):
    def ingredients(meat):
        if meat=="A":
            print( "Add chicken")
        elif meat=="B":
            print("Add pork")
        elif meat=="C":
            print("Add beef")
class Cook:
    def PizzaMaker(choice):
        if choice == "G":
            print("Which do you want choose dough? "
              "I can make its thick, thin or rye")
            dough = input("A-Thick dough, B-Thin dough, C-Rye dough:  ")
            Pizza_Mushroom.dough_on_choice(dough)
            Pizza_Mushroom.ingredients()
            print("Do you want vegetables?")
            vegetables = input("Yes/No:  ")
            if vegetables == "Yes":
                Pizza_Mushroom.vegetables()
            print("Which do you want choose sauce? "
              "I can add chili sauce, garlic honey sauce, salsa sauce")
            sauce = input("A-chili sauce, B-garlic honey sauce, C-salsa sauce:  ")
            Pizza_Mushroom.sauce_on_choice(sauce)
            Pizza_Mushroom.cheese()
        elif choice == "M":
            print("Which do you want choose dough? "
              "I can make its thick, thin or rye")
            dough = input("A-Thick dough, B-Thin dough, C-Rye dough:  ")
            Pizza_Meat.dough_on_choice(dough)
            print("What kind meat do you want?"
              "I can make Pizza with Chicken, Pork or Beef")
            meat = input("A-Chicken, B-Pork, C-Beef:   ")
            Pizza_Meat.ingredients(meat)
            print("Do you want vegetables?")
            vegetables = input("Yes/No")
            if vegetables == "Yes":
                Pizza_Mushroom.vegetables()
            print("Which do you want choose sauce? "
              "I can add chili sauce, garlic honey sauce, salsa sauce")
            sauce = input("A-chili sauce, B-garlic honey sauce, C-salsa sauce:  ")
            Pizza_Meat.sauce_on_choice(sauce)
            Pizza_Meat.cheese()
        elif choice == "V":
            Pizza_Vegan.dough()
            Pizza_Vegan.vegetables()
            Pizza_Vegan.ingredients()
            Pizza_Vegan.sauce()
        print( "Your Pizza is done!")
class Start:
    def Choice_Pizza():
        print("Hello! Which do you want choose Pizza? "
              "I can make its Vegan's, Meat or Mushroom")
        Choice = input("V-Vegan's, M-Meat, G-Muchroom:  ")
        Cook.PizzaMaker(Choice)

Start.Choice_Pizza()

