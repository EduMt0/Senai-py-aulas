class calculadora1:
    #Atributos da classe
    PI = 3.14

#Metodos estaticos da classe
    @staticmethod
    def circuferencia(raio) -> float:
        return 2 * calculadora1.PI * raio
    @staticmethod
    def area(raio) -> float:
        return calculadora1.PI * raio ** 2 