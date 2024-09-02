import os
from datetime import datetime
from pathlib import Path

OT_NAME = 'pep_parse'

SAVE_PATH = 'results'

BASE_DIR = Path(__file__).resolve().parent.parent / SAVE_PATH

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

FEEDS = {
    f'{SAVE_PATH}/pep_%(time)s.csv': {
        'format': 'csv',
        'encoding': 'utf-8',
        'overwrite': True,
        'fields': ['number', 'name', 'status'],
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 100,
}

os.makedirs(BASE_DIR, exist_ok=True)

now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
FILENAME = f'status_summary_{now}.csv'
FILEPATH = BASE_DIR / FILENAME
