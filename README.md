# Ближайшие бары

Для работы скрипта необходимо скачать json-файл с барами с сайта http://data.mos.ru/opendata/7710881420-bary.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python
# пример ответа скрипта

input data path: C:\python_rep\bars.json
#Вводим полное имя файла с данными
The biggest bar is "Спорт бар «Красная машина»" with 450 seats
The smallest bar is "БАР. СОКИ" with 0 seats
input your longitude: 50.57
#Вводим долготу
input your latitude: 45.98
#Вводим ширину
The closest bar is "Таверна" with 16 seats

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
