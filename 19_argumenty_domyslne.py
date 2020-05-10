# Pytanie 19 - wyjasnij jak działa poniższa funkcja.
# Wyjaśnij skąd wzięły się wyniki zwrócone przez poszczególne wywołania funkcji.

def dodaj_do_listy(n, lista=[]):  # lista=[] - argument domyślny funkcji
    lista.append(n)               # dodaj n do końca listy lista
    print(lista)

# Argument domyślny, w tym wypadku pusta lista, zostaje utworzona RAZ
# podczas definiowania funkcji i nie jest tworzona od nowa podczas kolejnych jej wywołań
# dlatego modyfikacja argumentu domyślnego podczas wywołania funkcji, spowoduje zapisanie tego stanu
# i zmodyfikowana lista trafi jako argument do kolejnego wywołania funkcji
# w którym zostanie użyty argument domyślny.

dodaj_do_listy(1)
dodaj_do_listy(2,[4,5])
dodaj_do_listy(3)
