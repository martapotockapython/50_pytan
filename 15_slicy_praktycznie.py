# Pytanie 15 - napisz funkcję, która sprawdzi czy podany string
# zaczyna się słowem "python" i kończy rozszerzeniem ".py"
# Przetestuj nią stringi:
a = "python_moj_kod.py"
b = "python_notatki.txt"

def sprawdz_czy_python(nazwa_pliku):
    if nazwa_pliku[0:6] == 'python' and nazwa_pliku[-3:] == '.py':
    # jeśli pierwsze 6 znaków stringa nazwa_pliku równają się 'python'
    # ORAZ
    # ostatnie trzy znaki stringa nazwa_pliku równają się '.py'
        return True    # zwróć True
    else:              # w przeciwnym wypadku
        return False   # zwróć False

print(sprawdz_czy_python(a))  # uruchomienie funkcji dla stringa a
print(sprawdz_czy_python(b))  # uruchomienie funkcji dla stringa b
