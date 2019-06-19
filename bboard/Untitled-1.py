class Test:
    def __init__(self, min, max):
        self.min = min
        self.max = max

a = Test(1,  5)
print(a.min, a.max)
print(dir(Test))