# Pytanie 46 - w jaki sposób zadbasz o to, aby twój kod był czytelny
# i łatwy do zrozumienia dla innych programistów?

# PEP8 !                 # link do PEP8 w materiałach dodatkowych

import os                # piszemy po jednym imporcie na linijkę
import math              # w bloku najwyżej importujemy moduły bibliteki standardowej

import modul_zewnetrzny  # w bloku niżej importujemy moduły zewnętrzne

import moj_fajny_modul   # w bloku najniżej importujemy moduły wewnętrzne (prywatne, firmowe)


class KlasyDuzymiLiterami:  # nad klasą i pod klasą powinny być dwie puste linie
    pass


zmienne_malymi_literami = 'snake case'

def funkcje_rowniez_malymi():  # nad funkcją i pod funkcją powinno być po jednej pustej linii
    pass

A = [1, 2, 2]               # zapisując sekwencje dajemy spację po przecinku
B = ['tak','jest','zle']    # czyli ta linijka zapisana jest niepoprawnie
