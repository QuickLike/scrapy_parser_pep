# [Проект scrapy_parser_pep.](https://github.com/QuickLike/scrapy_parser_pep)

## Технологии:

- Python
- Scrapy

## Описание проекта:

Парсер документов [PEP](https://peps.python.org/) на базе фреймворка Scrapy.

### Запуск проекта:
Клонируйте [репозиторий](https://github.com/QuickLike/scrapy_parser_pep) и перейдите в него в командной строке:
```
git clone https://github.com/QuickLike/scrapy_parser_pep

cd scrapy_parser_pep
```
Создайте виртуальное окружение и активируйте его:
```
python -m venv vevn

source venv/Scripts/activate
```
Обновите pip:
```
python -m pip install --upgrade pip
```
Установите зависимости:
```
pip install -r requirements.txt
```
Проект готов к работе!

## Примеры команд
Создает в папке results два файла:

1) pep_ДатаВремя.csv - csv файл со списком всех PEP
2) status_summary_ДатаВремя.csv - csv файл с таблицей из двух колонок «Статус» и «Количество»
```
scrapy crawl pep
```




## Автор

[Власов Эдуард](https://github.com/QuickLike)
