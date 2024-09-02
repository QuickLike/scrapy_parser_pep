import csv
import os
from collections import defaultdict

from pep_parse.settings import FILEPATH


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(FILEPATH, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(
                [['Статус', 'Количество']] +
                [[status, count]
                 for status, count in self.status_counts.items()
                 ] +
                [['Всего', len(self.status_counts)]]
            )
