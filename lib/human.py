class Human:
    species = "Homo sapiens"
    def __init__(self, name):
        self.name = name
        self._age = 0

    def get_age(self):
        print("Retrieving age.")
        print(f"Age is { self._age }")
        return self._age

    def set_age(self, age):
        if age > 1:
            print(f"Setting age to { age }")
            self._age = age
        else:
            print("Age must be greater than one.")

    age = property(get_age, set_age)


sam = Human("Sam")
sam.age = -2
sam.age