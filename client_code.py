from properties import Celsius


class SomeClass(object):
    def some_function(self):
        c = Celsius()
        return f"The current temperature is: {c.temperature}"


sc = SomeClass()

print(sc.some_function())
