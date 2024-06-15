'''create class car shop in which:
1.create function name carcompany which will allow user to select
a carcompany out displayed companies.if the user enters any random carcompany it should asked reenter.
2.according to the carcompany seclected the user should redirected to selecting the models of that company of that out of the given list if anything random given reenter
3.after selecting the model the user should be redirected to selecting the variant(petrol,disel).
4.according to the car company model and variant the price should be calculated to which sgst and cgst are added to make it the total price.
note->sgst and cgst are common for all the cars.'''
     
       
class CarShop:
    def __init__(self):
        self.car_companies = {
            "maruthi": {
                "spresso": {"petrol": 20000, "diesel": 22000},
                "jimmy": {"petrol": 30000, "diesel": 32000}
            },
            "mahendra": {
                "kuv 100": {"petrol": 25000, "diesel": 27000},
                "THAR 4X4": {"petrol": 35000, "diesel": 37000}
            },
            "Ford": {
                "mustang 1969": {"petrol": 15000, "diesel": 17000},
                "endover": {"petrol": 22000, "diesel": 24000}
            },
            "toyota": {
                "fortuner": {"petrol": 15000, "diesel": 17000},
                "supra": {"petrol": 22000, "diesel": 24000}
            },
        }
        self.sgst = 0.09
        self.cgst = 0.09

    def select_car_company(self):
        while True:
            print("Available car companies: ")
            for company in self.car_companies:
                print(company)
            company = input("Please select a car company: ")
            if company in self.car_companies:
                return company
            else:
                print("Invalid car company. Please try again.")

    def select_car_model(self, company):
        while True:
            print(f"Available models for {company}: ")
            for model in self.car_companies[company]:
                print(model)
            model = input(f"Please select a model from {company}: ")
            if model in self.car_companies[company]:
                return model
            else:
                print("Invalid car model. Please try again.")

    def select_variant(self, company, model):
        while True:
            print(f"Available variants for {model}: ")
            for variant in self.car_companies[company][model]:
                print(variant)
            variant = input(f"Please select a variant for {model} (petrol/diesel): ").lower()
            if variant in self.car_companies[company][model]:
                return variant
            else:
                print("Invalid variant. Please try again.")

    def calculate_price(self, company, model, variant):
        base_price = self.car_companies[company][model][variant]
        total_price = base_price * (1 + self.sgst + self.cgst)
        return total_price

    def run(self):
        company = self.select_car_company()
        model = self.select_car_model(company)
        variant = self.select_variant(company, model)
        total_price = self.calculate_price(company, model, variant)
        print(f"The total price for {company} {model} ({variant}) is: ${total_price:.2f}")

if __name__ == "__main__":
    shop = CarShop()
    shop.run()
         