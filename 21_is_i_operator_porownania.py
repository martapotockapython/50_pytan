# Pytanie 21: co wydrukuje się w wyniku wykonania poniższego kodu?

print(1 == True) # == to operator porównania wartości
print(1 is True) # is to operator porównania identyczności/tożsamości

print(id(1), id(1), id(True))  # wydrukuj id integera 1 i booleana True

print(2 ** 3 == 10 - 2)        # wydrukuj wynik porównania wartości dwóch równań

A = [1,2,3]                    # stworzenie dwóch list o identycznej zawartości
B = [1,2,3]                    # i przypisanych do innych zmiennych A i B
print(A == B)                  # porównanie wartości list A i B
print(A is B)                  # porównanie identyczności/tożsamośli list A i B

a = 'kotek'                    # stworzenie dwóch stringów o identycznej zawartości
b = 'kotek'                    # i przypisanych do innych zmiennych a i b
print(a == b)                  # porównanie wartości stringów a i b
print(a is b)                  # porównanie identyczności/tożsamości stringów a i b
