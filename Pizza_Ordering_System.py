import csv
import datetime

class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
    def get_description(self):
        return self.description
    def get_cost(self):
        return self.get_cost

class Classic(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza made by classic ingredients", 110)

class Margherita(Pizza):
    def __init__(self):
        super().__init__("It is a Napoli pizza made with tomatoes, mozzarella, basil, olive oil and salt.", 130)

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("It contains the delicacies of Turkish taste.", 130)

class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("A light flavor made with thyme tomato sauce and cheddar cheese", 120)

class Decorator:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost
    def get_description(self):
        return self.description
    def get_cost(self):
        return self.cost

class Olives(Decorator):
    def __init__(self):
        super().__init__("Classic olives", 80)
        
class Mushroom(Decorator):
    def __init__(self):
        super().__init__("Classic mushroom", 90)

class GoatCheese(Decorator):
    def __init__(self):
        super().__init__("The cheese which made by goat milk", 95)

class Meat(Decorator):
    def __init__(self):
        super().__init__("Classic meat", 100)

class Onions(Decorator):
    def __init__(self):
        super().__init__("Organic onions", 55)

class Corn(Decorator):
    def __init__(self):
        super().__init__("Organic corn", 40)

def main():
    file = open("Menu.txt", "r") 
    w = file.read()
    print(w)
    while True:
        pizza_choice = input("Please enter your choice (1-5): ")
        try:
            pizza_choice = int(pizza_choice)
        except ValueError:
            print("Invalied choice!")

        if pizza_choice == "1":
            Pizza = Classic()
            pizza_cost = 110
        elif pizza_choice == "2":
            Pizza = Margherita()
            pizza_cost = 130
        elif pizza_choice == "3":
            Pizza = TurkPizza()
            pizza_cost = 130
        elif pizza_choice == "4":
            Pizza = PlainPizza()
            pizza_cost = 120
        else:
            print("Please enter your choice (1-5): ")
            return
        print("Your pizza price is", pizza_cost)
        print("You have ordered a", Pizza.get_description())
        
    
        decorator_choice = input("Please enter your choice (11-16): ")
        if decorator_choice == "11":
            Decorator = Olives()
            decorator_cost = 80
        elif decorator_choice == "12":
            Decorator = Mushroom()
            decorator_cost = 90
        elif decorator_choice == "13":
            Decorator = GoatCheese()
            decorator_cost = 95
        elif decorator_choice == "14":
            Decorator = Meat()
            decorator_cost = 100
        elif decorator_choice == "15":
            Decorator = Onions()
            decorator_cost = 55
        elif decorator_choice == "16":
            Decorator = Corn()
            decorator_cost = 40
        else:
            print("Invalied choice")
            return
        print("Your decorator price is", decorator_cost)
        print("You have ordered a", Decorator.get_description())
        total_price = pizza_cost + decorator_cost
        print("Your total price is", total_price)
        break
    z = datetime.datetime.now()
    print(z)
    TC_Number = int(input("Please enter your TC number: "))
    Credit_Card_Number = int(input("Please enter your credit card number: "))
    Credit_Card_Password = int(input("Please enter your password: "))
    with open('Orders_Database.csv', mode = 'a') as f:
        writer = csv.writer(f)
        writer.writerow([TC_Number, Credit_Card_Number, Credit_Card_Password])
if __name__ == '__main__':
    main()














