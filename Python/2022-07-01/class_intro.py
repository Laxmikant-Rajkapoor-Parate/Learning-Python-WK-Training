class person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def greet(self):
        print(f'Hi, {self.name}')

p1 = person('Laxmikant', 20)
p1.greet()
print(f'Age: {p1.age}')
