class oprator_overloading:
    def __init__(self, num) -> None:
        self.x = num

    def __add__(self, other):
        return self.x + other.x
        
    def __sub__(self, other):
        return self.x - other.x
    
    def __it__(self, other):
        return self.x < other.x

o1 = oprator_overloading(10)
o2 = oprator_overloading(20)

print(o1+o2)
print(o1-o2)
print(o1.__it__(o2))