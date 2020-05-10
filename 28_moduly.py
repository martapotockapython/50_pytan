# Pytanie 28 - jaki błąd popełniono w poniższym kodzie?
# Co zrobić aby go uniknąć?
# Stworz moduł kserokopiarka zawierający funkcję, która podany string wydrukuje dwa razy
# Użyj tej funkcji w kodzie poniżej

from drukarka import wydrukuj_imie

def wydrukuj_imie(imie):
    print(imie)

# # Kod poprawiony
# from drukarka import wydrukuj_imie as wydrukuj_imie_z_drukarki
# # z modułu drukarka zaimportuj funkcję wydrukuj_imię i nadaj jej alias wydrukuj_mnie_z_drukarki
# from kserokopiarka import zrob_ksero
# # z modułu kserokopiarka zaimportuj funkcję zrob_ksero
#
# def wydrukuj_imie(imie):
#     print(imie)
#
# wydrukuj_imie("Marta")
# wydrukuj_imie_z_drukarki("Marta")
# zrob_ksero("Witaj świecie!")
