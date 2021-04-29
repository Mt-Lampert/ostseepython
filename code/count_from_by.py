
class CountFromBy:

    def __init__(self, pVal = 0, pIncrement = 1):
        self.val = pVal
        self.increment = pIncrement

    def __repr__(self):
        return f"val: {self.val}; increment: {self.increment}"     


    def increase(self):
       self.val += self.increment 



if __name__ == "__main__":
    a = CountFromBy()
    a.increase()
    print(a)

    a = CountFromBy(42, 10)
    a.increase()
    a.increase()
    print(a)
