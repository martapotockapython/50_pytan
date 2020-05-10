# Pytanie 33 - do czego w Pythonie służy słowo kluczowe yield ?
# Napisz przykładowy kod wykorzystujący yield.

def zwracaj_kolejne_parzyste():        # definicja generatora wygląda jak definicja zwykłej funkcji
    for n in range(2,20,2):            # range tworzący zakres od 2 do 20, przesuwając się o 2
        yield n                        # słowo yield informuje interpreter, że ta funkcja będzie generatorem

z = zwracaj_kolejne_parzyste()         # tworzenie obiektu generatora

for i in range(10):                    # pętla for wykonująca się 10 razy
    print(next(z))                     # która za kazdym razem drukuje kolejną wartość zwróconą z obiektu genratora z

y = ('a' * n for n in range(5))        # generator expression - wyrażenie generatorowe
                                       # tworzy generator, który będzie zwracał kolejne wielokrotności stringa 'a'
                                       # zakresie od 0 do 4

for i in range(5):                     # wypisanie kolejnych wartości zwróconych przez obiekt genratora y
    print(next(y))
