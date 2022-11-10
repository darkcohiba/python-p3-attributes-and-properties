#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed):
        self.set_name(name)
        self.breed = breed

    def set_name(self, name):
        if (isinstance(name, (str))) and (1 <= len(name) <= 25):
            self.name = name
        else:
            print ("Name must be string between 1 and 25 characters.")
        

sam = Dog("sam", "Lab")
print(sam.name)