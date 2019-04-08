# Function defined outside the class
def f1(self, x, y):
    return min(x,x+y)

class C:
    """Specific class, which has method
    defined outside of the class"""
    f = f1

    def g(self):
        return "hello world"

    h = g

