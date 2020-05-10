# Pytanie 23 - czym jest lambda?
# Napisz przykładowy kod wykorzystujący lambdę.

# lambda argument : wyrażenie
# lambda x:x+2

L = [('Anna',82), ('Robert',33), ('Artur',40), ('Feliks',56)]
# W poniższej linijce funkcja sorted pobiera sekwencję danych do posortowania i klucz, po którym będzie sortować.
# Sekwencją jest lista L, a kluczem lambda, która dla kolejnego elementu listy L (czyli tupli)
# zwraca drugi element danej tupli.
L_posortowana = sorted(L, key = lambda x:x[1])
print(L_posortowana)
