# Pytane 38 - do czego służą dekoratory @staticmethod i @classmethod?

class Matematyka:
    def __init__(self):
        self.pi = 3.14

    def policz_obwod_okregu(self, r):
        return 2 * self.pi * r

    @staticmethod          # metoda statyczna nie jest swiadoma bycia czescia klasy
    def dodaj(a, b):       # a wiec nie widzi innych metod tej klasy
        return a + b

    # @staticmethod
    # def dodaj_i_pomnoz(a,b):
    #     return dodaj(a,b) * 2

    @classmethod                    # metoda klasowa jest swiadoma bycia czescia klasy i widzi inne metody w klasie
    def dodaj_i_pomnoz(cls,a,b):    # wymaga slowa kluczowego cls (zamiast self) bo operuje na klasie a nie na jej obiekcie/instancji
        return cls.dodaj(a,b) * 2

m = Matematyka()
print(m.policz_obwod_okregu(5))
print(Matematyka.dodaj(2,3))
print(Matematyka.dodaj_i_pomnoz(2,3))
