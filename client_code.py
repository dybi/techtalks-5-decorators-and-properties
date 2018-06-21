from properties import Celsius


class SomeClass(object):
    def __init__(self, celsius):
        self.celsius = celsius

    def some_function(self):
        return f"The current temperature is: {self.celsius.temperature}"


c = Celsius(20)
c.temperature = 25

sc = SomeClass(c)
print(sc.some_function())
