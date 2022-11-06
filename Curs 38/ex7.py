"""7. PROIECT: Downloads folder watcher
Pe acelasi nivel cu directorul Downloads se creeaza un director DownloadsClean, in el se creeaza
folderele Music, Pictures, Videos, Documents, Executables, Others. (automat la pornirea scriptului)
Scriptul urmareste folderul Downloads al uilizatorul curent.
La fiecare modificare se citeste continutul si apoi se face clasificarea si mutarea."""


import shutil
from pathlib import Path
import time
import os

DOWNLOAD_CLEAN =  Path.home() / "Downloads Clean"
DOWNLOAD_DIR = Path.home() / "Downloads"
MUSIC_DIR = DOWNLOAD_CLEAN / "Music"
PICTURE_DIR = DOWNLOAD_CLEAN / "Pictures"
VIDEO_DIR = DOWNLOAD_CLEAN / "Video"
EXE_DIR = DOWNLOAD_CLEAN / "Apps"
OTHERS_DIR = DOWNLOAD_CLEAN / "Others"

DOWNLOAD_CLEAN.mkdir(exist_ok=True, parents=True)
MUSIC_DIR.mkdir(exist_ok=True, parents=True)
PICTURE_DIR.mkdir(exist_ok=True, parents=True)
VIDEO_DIR.mkdir(exist_ok=True, parents=True)
EXE_DIR.mkdir(exist_ok=True, parents=True)
OTHERS_DIR.mkdir(exist_ok=True, parents=True)


initial_time_delta = DOWNLOAD_DIR.stat().st_mtime
initial_size = 0
final_size = 0


while True:
    if DOWNLOAD_DIR.stat().st_mtime != initial_time_delta:
        initial_time_delta = DOWNLOAD_DIR.stat().st_mtime
        for path in DOWNLOAD_DIR.glob("**/*"):
            while True:
                for path in DOWNLOAD_DIR.glob("**/*"):
                    initial_size = path.stat().st_size
                    time.sleep(2)
                for path in DOWNLOAD_DIR.glob("**/*"):
                    final_size = path.stat().st_size
                print(initial_size, final_size)
                if initial_size != final_size:
                    continue
                else:
                    break
            if path.suffix in [".mp3", ".wma", ".aac"]:
                shutil.move(path, MUSIC_DIR)
            elif path.suffix in [".jpg", ".jpeg", ".png"]:
                shutil.move(path, PICTURE_DIR)
            elif path.suffix in [".mpg", ".mkv", ".flv", ".avi", ".gif", ".mov", ".wmv", ".mp4"]:
                shutil.move(path, VIDEO_DIR)
            elif path.suffix in [".exe"]:
                shutil.move(path, EXE_DIR)
            else:
                shutil.move(path, OTHERS_DIR)