# Pytanie 2 - co się stanie po wykonaniu poniższego kodu?

a = "abcdefg"            # do zmiennej a przypisz zostaje string 'abcdefg'
print(a[1])              # wydrukuj element znajdujący się pod indeksem 1 w stringu a
# a[1] = 'X'             # próba modyfikacji stringa - operacja zabroniona skutkująca TypeError

a_lista = list(a)        # stwórz listę a_lista zawierającą litery ze stringa a
a_lista[1] = 'X'         # zmodyfikuj zawartość listy pod indeksem 1 - listy są obiektami, które można modyfikować
a = "".join(a_lista)     # stwórz stringa a łącząc elementy listy a_lista przy użyciu pustego separatora ""
print(a)
