class triangulo:
    #Atributos
    a:int
    b:int
    c:int

    a = 0
    b = 0
    c = 0

    #Metodos de classe
    def area(self):
        from math import sqrt
        p = (self.a + self.b + self.c) / 2
        area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area