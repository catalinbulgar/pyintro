class Stiva:

    def __init__(self, nr):
        self.stiva = []

    def push(self, val):
        self.stiva.append(val)

    def pop(self):
        val = self.stiva[-1]
        del self.stiva[-1]
        return val


obiect = Stiva(4)
obiect.push(3)
obiect.push(2)
obiect.push(1)
print(obiect.stiva)
print(obiect.pop())
print(obiect.pop())
print(obiect.pop())
print(obiect.stiva)
obiect1 = Stiva(6)
obiect1.push(4)
obiect1.push(5)
obiect1.push(6)
print(obiect1.stiva)
