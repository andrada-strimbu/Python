class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def mileage(self): pass

    def towingCapacity(self): pass


class Car(Vehicle):
    def __init__(self, make, model, year, consum, capacitateDeRemorcare):
        super().__init__(make, model, year)
        self.consum = consum
        self.capacitateDeRemorcare = capacitateDeRemorcare

    def mileage(self):
        print(self.consum)

    def towingCapacity(self):
        print(self.capacitateDeRemorcare)


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, consum, capacitateDeRemorcare):
        super().__init__(make, model, year)
        self.consum = consum
        self.capacitateDeRemorcare = capacitateDeRemorcare

    def mileage(self):
        print(self.consum)

    def towingCapacity(self):
        print(self.capacitateDeRemorcare)


class Truck(Vehicle):
    def __init__(self, make, model, year, consum, capacitateDeRemorcare):
        super().__init__(make, model, year)
        self.consum = consum
        self.capacitateDeRemorcare = capacitateDeRemorcare

    def mileage(self):
        print(self.consum)

    def towingCapacity(self):
        print(self.capacitateDeRemorcare)


def main():
    car = Car(make="Toyota", model="Camry", year=2022, consum=7.13, capacitateDeRemorcare=130)
    motorcycle = Motorcycle(make="Harley-Davidson", model="Sportster", year=2021, consum=5, capacitateDeRemorcare=10)
    truck = Truck(make="Ford", model="F-150", year=2023, consum=20, capacitateDeRemorcare=440)
    car.display_info()
    car.mileage()
    car.towingCapacity()
    motorcycle.mileage()
    motorcycle.towingCapacity()
    truck.display_info()
    truck.mileage()
    truck.towingCapacity()



main()
