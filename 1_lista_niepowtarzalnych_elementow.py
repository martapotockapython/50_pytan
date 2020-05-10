# Pytanie 1 - lista niepowtarzalnych elementów
# Korzystając z podanej listy A
# stwórz listę B zawierającą tylko unikalne elementy z listy A

A = [1,2,3,3,2,1,2,3] # -> B = [1,2,3]

B = []                      # stwórz pustą listę B
for element in A:           # dla kolejnego elementu w liście A
    if element not in B:    # jeśli element nie znajduje się w liście B
        B.append(element)   # dodaj ten element do listy B
print(B)                    # wydrukuj listę B

B = list(set(A))            # stwórz listę B na podstawie setu stworzonego na podstawie listy A
print(B)
