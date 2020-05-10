# Pytanie 46 - w jaki sposób importujesz zewnętrzne moduły w Pythonie?

# pip install nazwa_modułu

from colorama import init, Fore, Back, Style
init()
print(Fore.RED + "Tekst na czerwono")
print(Back.YELLOW + "... na żółtym tle")
print(Style.RESET_ALL + "... i znowu normalnie.")

# PyPI - Python Package Index - strona, na której dostępna jest ogromna ilość pakietów do Pythona wraz z dokumentacją
# to z niej pip ściąga instalowane przez nas pakiety
