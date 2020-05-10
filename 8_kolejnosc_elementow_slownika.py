# Pytanie 8 - Co zostanie wypisane w wyniku wykonania poniższego kodu?

D = {1: 'Ala', 2: 'ma', 3: 'kota'}

for key in D:      # dla kolejnego klucza w słowniku D
    print(D[key])  # wydrukuj wartość słownika przechowywaną pod tym kluczem

# 2 - 3.5 - słownik nie trzyma kolejności
# 3.6 - trzyma kolejność
# 3.7 - słownik trzyma kolejność (gwarantowane)
# OrderedDict
