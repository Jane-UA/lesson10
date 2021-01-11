class Dog:
    age_counter = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        return self.dog_age * self.age_counter


if __name__ == "__main__":
    d = Dog(7)
    print(d.human_age())
