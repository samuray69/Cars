class Car():
    def __init__(self, company, country):
        self.company = company
        self.country = country
        self.all_budget = 0

    def company_info(self):
        print(f"Company: {self.company}, Country: {self.country}")


class Model(Car):
    def __init__(self, company, country, model, price):
        super().__init__(company, country)
        self.model = model
        self.price = price

    def car_info(self):
        print(f"Model: {self.model}, Price: {self.price}")


ford_model = Model("Ford", "USA", "Mustang", 6000)
hummer_model = Model("Ford", "USA", "Mustang", 6000)
