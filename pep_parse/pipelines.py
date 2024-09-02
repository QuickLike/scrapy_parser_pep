import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{now}.csv'
        filepath = BASE_DIR / filename
        with open(filepath, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(
                [
                    ['Статус', 'Количество']
                ] + [
                    [status, count]
                    for status, count in self.status_counts.items()
                ] + [
                    ['Всего', len(self.status_counts)]]
            )
