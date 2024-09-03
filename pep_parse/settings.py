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

DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
