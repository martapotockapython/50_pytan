# Pytanie 29 - do czego w Pythonie służy plik: __init__.py ?
# Stwórz kod w krótki sposób prezentujący jego zastosowanie.

import muzyka.trabka               # importuj pakiet.moduł
import muzyka.perkusja

muzyka.trabka.graj()               # uruchomienie pakiet.moduł.funkcja
muzyka.perkusja.graj()

# from muzyka import trabka        # z pakietu zaimportuj moduł
# from muzyka import perkusja
#
# trabka.graj()                    # uruchomienie moduł.funkcja
# perkusja.graj()

from muzyka.trabka import graj as graj_trabka      # zaimportuj funkcję z pakiet.moduł, nadaj jej alias
from muzyka.perkusja import graj as graj_perkusja

graj_trabka()                      # uruchomienie za pomocą aliasu
graj_perkusja()
