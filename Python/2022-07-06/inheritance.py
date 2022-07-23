class base1:
    def sayHi(self):
        print("Hi, from base 1")

class base2:
    def sayHi(self):
        print("Hi, from base 2")

# first to inherited gets called first
class derived(base1, base2):
    def greet(self):
        print("Hi, from derived")

# b1 = base1()
# b1.sayHi()

# b2 = base2()
# b2.sayHi()

# b = derived()
# b.greet()
# b.sayHi()

print(derived.mro())