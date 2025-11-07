class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal yaratilmoqda: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Dog yaratilmoqda: {self.breed}")

dog = Dog("Buddy", "Labrador")
