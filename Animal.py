
class Animal(object):

    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def get_name(self):
        return self.name

    def set_name(self, new_name=""):
        self.name = new_name

    def __str__(self):
        return f"animal: {self.name}, {self.age}"


class Dog(Animal):

    def speak(self):
        print("Ham Ham")

    def __str__(self):
        return f"dog: {self.name}, {self.age}"


class Person(Animal):
    id = 1

    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = set()
        self.tag = Person.id
        Person.id += 1

    def get_friends(self):
        return self.friends

    def add_friend(self, name):
        self.friends.add(name)


cat = Animal(2)
print("Cat's age: ", cat.get_age())
cat.set_name("Tom")
print(cat)


lassie = Dog(8)
lassie.set_name("Lassie")
lassie.speak()
print(lassie)

ion = Person("Ion", 21)
maria = Person("Maria", 19)
print(maria.get_friends())
maria.add_friend("Ion")
maria.add_friend("Ion")
maria.add_friend("Ion2")
print(maria.get_friends())

print(Person.id)