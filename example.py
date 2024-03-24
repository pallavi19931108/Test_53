class carModel:
    name = "bmw"
    gear = 5
    def run(self):
        print("Car gear is :",self.gear)
        print("Car name is :",self.name)
    def run1(self):
        print("Car gear is:",self.gear)
car_obj = carModel()
print(car_obj)
car_obj.run()
car_obj.run1()