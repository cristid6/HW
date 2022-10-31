"""1. Scrie un script care creeaza un fisier text. In fisierul text trebuie sa se regaseasca
o lista cu toate fisierele dll din directoru C:\Windows\System32"""

from pathlib import Path

ROOT = Path("C:\Windows\System32")

with open("exercitiul1.txt", "w") as fisier:
    for path in ROOT.glob("**/*.dll"):
        fisier.write(f"{path}\n")
