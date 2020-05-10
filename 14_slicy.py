# Pytanie 14
# Wypisz pierwsze 5 elementów listy L.
# Wypisz co drugą literę stringa s, zaczynając od ostatniej i cofając się do poczatku.

L = [11, 22, 33, 44, 55, 66, 77, 88, 99, 1010]
s = 'a nMozh^tKysPW 9ęxi b$uML'

# range(start,stop,krok)
# mojedane[start:stop:krok] # slice
# start - indeks od którego zaczyna się slice (należący do slice)
# stop - indeks o jeden większy od tego, na którym kończy się slice (nie należący już do niego)
# krok - parametr mówiący o ile liczb chcemy się przesuwać. W wersji ujemnej używany w tworzeniu sliców-ów czytających sekwencję od prawej do lewej


print(L[0:5]) # -> L[:5]  # wydrukuj slice od indeksu 0 do 4 (5 nie należy do slica)
print(s[-1::-2])          # wydrukuj slice od indeksu ostatniego do początku, przesuwając się co dwa elementy
