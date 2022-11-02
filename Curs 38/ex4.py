"""4. Scrie un script care face curatenie pe desktop. Cand executi scriptul toate fisierele (mai putin shortcuts)
vor fi mutate intr-un folder denumit de forma 2022-10-30_11-20 (ora data curenta). Noul folder creat
va sta intr-un folder definit de utilizator intr-un fisier de configurare. Fisierul de config se gaseste
pe acelasi nivel ca si scriptul si contine pe prima linie calea catre folderul parinte al arhivei."""


from pathlib import Path
from datetime import datetime
import shutil

DESKTOP_PATH = Path(r"C:\Users\Cristi\Desktop\New desktop")
ROOT = Path(__file__).parent
CONFIG_PATH = ROOT / "config.txt"
current_date = datetime.now()
folder_name = current_date.strftime("%Y-%m-%d_%H-%M-%S")

try:
    with CONFIG_PATH.open() as fin:
        content = fin.readline()
        content = content.strip("\n")
except OSError as err:
    ARCHIVE_PATH = Path(r"C:\Archive")
    print(f"Error {err}")
else:
    ARCHIVE_PATH = Path(content)

ARCHIVE_PATH.mkdir(exist_ok=True)

FOLDER_PATH = ARCHIVE_PATH / folder_name


try:
    shutil.copytree(DESKTOP_PATH,FOLDER_PATH)
except FileExistsError:
    print("Backup-ul a fost deja efectuat! Incearca peste 1 minut!")
else:
    print("Backup complet!")





