"""2. Scrie un script care afiseaza cu cate secunde in urma a fost adaugat ceva in folderul Downloads."""

from pathlib import Path

DOWNLOADS_DIR = Path.home()  / "Downloads"

initial_time_delta = DOWNLOADS_DIR.stat().st_mtime

while True:
    if DOWNLOADS_DIR.stat().st_mtime !=  initial_time_delta:
        initial_time_delta = DOWNLOADS_DIR.stat().st_mtime
        print("s-a modificat")