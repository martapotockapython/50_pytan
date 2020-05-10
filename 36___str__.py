# Pytanie 36 - wykorzystajmy klasę Pies i obiekt maly_pies z poprzedniego pytania.
# Co stanie się gdy wypiszemy print(maly_pies)?
# Co zrobiłbyś, aby wydrukowana w ten sposób informacja zawierała imie i rase psa?

class Pies:
    def __init__(self, imie, rasa):
        self.imie = imie
        self.rasa = rasa

# zdefiniowanie w klasie metody __str__ pozwala sformatować tekst, który zostanie wypisany w wyniku:
# wykonania funkcji print na obiekcie danej klasy - print(obiekt)
# wywołania funkcji str od obiektu klasy  - str(obiekt)
    def __str__(self):
        return f"Pies rasy {self.rasa} ma na imie {self.imie}"

maly_pies = Pies("Pikuś", "ratlerek")
print(maly_pies)
