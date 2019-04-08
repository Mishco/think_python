class Complex:
    """Complex number, contains real part
     and imagine part consist
     Special operand is i, which is defined:
     i^2 = -1
     """
    def __init__(self,realpart, imagpart):
        self.r = realpart   # instance variable unique to each instance
        self.i = imagpart   #
