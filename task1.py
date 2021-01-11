class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print("Hello my name is", self.firstname, self.lastname,
              'and I am', self.age, 'years old')


if __name__ == "__main__":
    p1 = Person('Carl', 'Johnson', 26)
    p1.talk()
