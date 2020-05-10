# Pytanie 6 - jakiej struktury danych użyłbyś do zapisania numerów telefonów
# wszystkich klientów firmy i odpowiadających im nazwisk. Wybierz strukturę tak,
# aby sprawdzenie właściciela numeru telefonu nie zajmowało dużo czasu.

# Następnie stwórz przykładową strukturę przechowującą poniższe informacje:
# 123456789 - Jan Kot
# 999888777 - Anna Lis
# 111222333 - Jan Kot
# Odczytaj nazwisko właściciela numeru 123456789

D = {123456789:'Jan Kot', 999888777:'Anna Lis', 111222333:'Jan Kot'}

print(D[123456789]) # odczytanie elementu słownika D znajdującego się pod kluczem 123456789

# złożoność obliczeniowa wyszukania elementu w liście N-elementowej: O(N)
# złożoność obliczeniowa wyszukania elementu w słowniku N-elementowym: O(1) - lepsza!
















#
