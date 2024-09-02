import csv
import os
from collections import defaultdict
from datetime import datetime

from pep_parse.constants import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item["status"]] += 1
        return item

    def close_spider(self, spider):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'status_summary_{now}.csv'
        filepath = BASE_DIR / filename
        os.makedirs(BASE_DIR, exist_ok=True)
        rows_to_write = []
        fieldnames = ['Статус', 'Количество']
        total_count_statuses = 0
        for status, count in self.status_counts.items():
            rows_to_write.append({fieldnames[0]: status, fieldnames[1]: count})
            total_count_statuses += 1
        rows_to_write.append(
            {fieldnames[0]: 'Всего', fieldnames[1]: total_count_statuses}
        )
        with open(filepath, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows_to_write)
