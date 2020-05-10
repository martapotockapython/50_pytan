# Pytanie 37 - co zostanie wypisane w wyniku uruchomienia poniższego kodu?

class ZwierzeLadowe:                      # klasa ZwierzeLadowe ma dwie metody: przedstaw_sie i biegaj
    def przedstaw_sie(self):
        print("Jestem zwierzęciem lądowym.")
    def biegaj(self):
        print("Biegam tu i tam.")

class ZwierzeMorskie:                     # klasa ZwierzeMorskie ma dwie metody: przedstaw_sie i plywaj
    def przedstaw_sie(self):
        print("Jestem zwierzęciem morskim.")
    def plywaj(self):
        print("Pływam tu i tam.")

class SwinkaMorska(ZwierzeLadowe, ZwierzeMorskie): # klasa SwinkaMorska dziecziczy z klas: ZwierzeLadowe i ZwierzeMorskie
    pass                                           # klasa ZwierzeLadowe lądowe ma priorytet nad klasą ZwierzeMorskie bo jest podana jako pierwszas

swinka = SwinkaMorska()      # tworzenie obiektu klasy SwinkaMorska
swinka.przedstaw_sie()       # wywołanie metody przedstaw_sie odziedziczonej z klasy ZwierzeLadowe
swinka.biegaj()              # wywołanie metody biegaj odziedziczonej z klasy ZwierzeLadowe
swinka.plywaj()              # wywołanie metody pływaj odziedziczonej z klasy ZwierzeMorskie
