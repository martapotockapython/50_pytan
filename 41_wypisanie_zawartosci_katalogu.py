# Pytanie 41 - napisz funkcję, która dla podanego katalgu wypisze znajdujące się w nim pliki.
# Pamiętaj, że katalog może zawierać podkatalogi, do których funkcja również musi zajrzeć.

# os.listdir - zwraca zawartość danego katalogu
# os.path.join - łączy dwa stringi w ścieżkę czytelną dla danego systemu operacyjnego
# os.path.isdir - sprawdza czy pod nadą ściezką znajduje się katalog
import os

def wypisz_zawartosc_katalogu(sciezka_do_katalogu):

    for element in os.listdir(sciezka_do_katalogu):        # dla każdego elementu w katalogu pod adresem 'sciezka_do_katalogu'
        sciezka_do_elementu = os.path.join(sciezka_do_katalogu, element) # przy uzyciu os.path.join utworz sciezke do tego elementu
        if os.path.isdir(sciezka_do_elementu):             # jeśli element jest również katalogiem
            wypisz_zawartosc_katalogu(sciezka_do_elementu) # uruchom rekurencyjnie funkcję wypisz_zawartosc_katalogu z adresem elementu jako argumentem
        else:                                              # w przeciwnym wypadku (czyli element nie jest katalogiem)
            print(sciezka_do_elementu)                     # wypisz element

wypisz_zawartosc_katalogu(r"C:\Udemy\50 pytań\kod\testowy")
