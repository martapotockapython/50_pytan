# Pytanie 32 - do czego w Pythonie służą dekoratory? Napisz dekorator, który będzie
# będzie dodawał trzy gwiazdki przed i po efekcie działania udekorowanej funkcji.

def dodaj_gwiazdki(funkcja):     # definicja dekoratora niczym nie różni się od definicji zwykłej funkcji
    def funkcja_udekorowana():   # wewnątrz dekoratowa tworzymy WEWNĘTRZNĄ funkcję, w której udekorujemy funkcję pobraną jako argument
        print("***")             # dekorowanie funkcji
        funkcja()                # wywołanie funkcji będącej argumentem dekoratora
        print("***")             # dekorowanie funkcji
    return funkcja_udekorowana   # zwrócenie funkcji WEWNĘTRZNEJ, w której udekorowano funkcję będącą argumentem dekoratora

@dodaj_gwiazdki                  # zapis @dodaj_gwiazdki BEZPOŚREDNIO nad definicją funkcji f() powoduje, że funkcja f() zostaje udekorowana
def f():                         # definicja funkcji f()
    print("Cześć, jestem f()")
