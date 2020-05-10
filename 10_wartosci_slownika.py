# Pytanie 10 - korzystając ze słownika stworzonego w poprzednim zadaniu
# sprawdź czy któraś z liter wystąpiła w stringu dokładnie 4 razy.
# Jeśli tak - wypisz True, jeśli nie - False.

litery = {'m': 1, 'y': 3, 's': 1, 'z': 3, 'd': 2, 'o': 2, \
          'k': 2, 'a': 2, 'u': 2, 'j': 2, 'ą': 2, 'g': 1, \
          't': 1, 'n': 1, 'i': 1, 'e': 1, 'c': 1}

print(litery.values())       # wydrukuje obiekt dict_values zawierający wartości słownika
print(list(litery.values())) # drukuje listę stworzoną na podstawie obiektu dict_values


if 4 in litery.values():     # jeśli 4 znajduje się w sekwencji dict_values
    print(True)              # wydrukuj True
else:                        # w przeciwnym wypadku
    print(False)             # wydrukuj False

print(True if 4 in litery.values() else False)  # wydrukuj True jeśli 4 jest w dict_values, w przeciwnym wypadku False
