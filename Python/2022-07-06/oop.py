class person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hi, {self.name}')

p1 = person('Laxmikant', 20)

# print(type(p1))
# print(p1.age)
# print(p1.__class__)
# print(p1.__dict__)
# print(p1.__module__)

# del p1.age
# print(p1.__dict__)

# print(hasattr(p1, "age"))
# print(hasattr(p1, "age"))
# print(hasattr(p1, "gender"))

setattr(p1, "name", "Ajay")
print(p1.__dict__)

print(getattr(p1, "name"))