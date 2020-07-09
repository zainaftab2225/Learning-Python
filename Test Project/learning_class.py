class Animal():
    def __init__(self, name=""):
        self.name = name
        print("An animal has been born.")

    def eat(self):
        print("Munch Munch")

    def make_noise(self):
        print(self.name, " says, Grr!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name
        print("A cat has been born.")

    def make_noise(self):
        print(self.name, " says, Meow!")


class Dog(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name
        print("A dog has been born.")

    def make_noise(self):
        print(self.name, "says, Bark!")


def main():
    pinky = Cat("Pinky")
    gatt = Dog("Gatt")
    spot = Dog("Spot")
    my_animal = Animal("Animal")

    print("Printing noises..")
    pinky.make_noise()
    gatt.make_noise()
    spot.make_noise()
    my_animal.make_noise()

    print("Printing eating..")
    pinky.eat()
    gatt.eat()
    spot.eat()
    my_animal.eat()


if __name__ == "__main__":
    main()
