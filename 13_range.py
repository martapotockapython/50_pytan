# Pytanie 13
# stwórz dwie listy:
# A - zawierającą liczby od 1 do 10
# B - zawierającą co trzecią liczbę z zakresu od 100 do 1
# w obu przypadkach możesz napisać tylko jedną linijkę kodu

# print(list(range(10)))
# list - zamieni obiekt typu range na listę
# range(start, stop, krok)
# start - indeks od którego zaczyna się sekwencja (należący do sekwencji)
# stop - indeks o jeden większy od tego, na którym kończy się sekwencja (nie należący już do niej)
# krok - parametr mówiący o ile liczb chcemy się przesuwać. W wersji ujemnej używany w tworzeniu range-ów malejących

A = list(range(1,11))        # tworzy listę od range w zakresie od 1 do 10 włącznie (11 nie wchodzi w sekwencję)
print(A)

B = list(range(100, 0, -3))  # tworzy listę od range w zakresie co trzeciego elementu od 100 do 1 włącznie (0 nie wchodzi w sekwencję),
print(B)

# Python 2.x - range był funkcją - zwracał listę (xrange - działał jak range w Pythonie 3.x)
# Python 3.x - range jest typem danych - zwraca sekwencję liczb












# A = [1,2,3,4,5,6,7,8,9,10]
# B = [100, 97, 94, 91....]
