import os

from pep_parse.settings import BASE_DIR, SAVE_PATH

os.makedirs(BASE_DIR / SAVE_PATH, exist_ok=True)
