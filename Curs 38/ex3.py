"""3. Scrie o functie care afiseaza un mesaj de salut. Mesajul de salut trebuie sa contina numele utilzatorului
curent (se obtine cu modulul os) si cati GB (cu doua zecimale) ocupa directorul home. Ex: Salut mdinu!
Spatiu utilizat de tine: 4.55 GB"""

import os
from pathlib import Path

def say_hello():
    """Returns the `directory` size in gigabytes."""

    USER_ROOT = Path("C:\\Users\\" + os.getlogin())
    size = 0
    for path in USER_ROOT.glob("**\*"):
        size += path.stat().st_size

    print(f"Salut {os.getlogin()}! Spatiul utilizat de tine: {round(size/10**9,2)} GB.")

say_hello()