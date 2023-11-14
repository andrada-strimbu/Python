class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display_info(self):
        return f"{self.name} - Habitat: {self.habitat}"

    def unique(self): pass


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color):
        super().__init__(name, habitat)
        self.fur_color = fur_color

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Class: Mammal, Fur Color: {self.fur_color}")

    def unique(self):
        print(f"{self.name} is giving birth to live young.")


class Bird(Animal):
    def __init__(self, name, habitat, wingspan):
        super().__init__(name, habitat)
        self.wingspan = wingspan

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Class: Bird, Wingspan: {self.wingspan} inches")

    def unique(self):
        print(f"{self.name} is building a nest.")


class Fish(Animal):
    def __init__(self, name, habitat, scale_color):
        super().__init__(name, habitat)
        self.scale_color = scale_color

    def display_info(self):
        base_info = super().display_info()
        print(f"{base_info}, Class: Fish, Scale Color: {self.scale_color}")

    def unique(self):
        print(f"{self.name} is laying eggs in the water.")


def main():
    lion = Mammal(name="Lion", habitat="Grassland", fur_color="Golden")
    eagle = Bird(name="Eagle", habitat="Mountains", wingspan=72)
    salmon = Fish(name="Salmon", habitat="Freshwater", scale_color="Silver")
    lion.display_info()
    lion.unique()
    eagle.display_info()
    eagle.unique()
    salmon.display_info()
    salmon.unique()


main()
