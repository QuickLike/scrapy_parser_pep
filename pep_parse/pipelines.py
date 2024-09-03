import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR, DATE_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        filename = (
            f'status_summary_{datetime.now().strftime(DATE_FORMAT)}.csv'
        )
        filepath = BASE_DIR / filename
        with open(filepath, 'w') as csvfile:
            writer = csv.writer(
                csvfile,
                dialect='excel',
                quoting=csv.QUOTE_NONE
            )
            writer.writerows(
                (
                    ('Статус', 'Количество'),
                    *self.status_counts.items(),
                    ('Всего', sum(self.status_counts.values()))
                )
            )
