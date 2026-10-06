# Internet Speed Tester

Простая консольная утилита для измерения скорости загрузки данных по указанному URL.

## Возможности

- Выполняет 10 последовательных HTTP-запросов.
- Измеряет время выполнения каждого запроса.
- Вычисляет среднее время запроса.
- Вычисляет общий объём скачанных данных.
- Вычисляет среднюю скорость загрузки в MB/s.
- Поддерживает автоматическое следование HTTP-редиректам.

## Требования

- Python 3.10+
- Библиотека `httpx`

## Установка

Клонировать репозиторий:

```bash
git clone https://github.com/tinkerov/internet-speed-test
cd internet-speed-test
```

Установить зависимости:

```bash
python -m pip install -r requirements.txt
```

## Использование

Запустить программу, передав прямой URL на скачиваемый файл:

```bash
python main.py "https://devlab.itlibra.com/files/images/jpg/jpg-10mb.jpg"
```

Программа выполнит 10 последовательных загрузок и выведет результаты в консоль.

Пример вывода:

```text
Request 1/10: 2.341 s, 10.00 MB
Request 2/10: 2.102 s, 10.00 MB
Request 3/10: 2.287 s, 10.00 MB
...
Average request time: 2.521 s
Downloaded data: 100.00 MB
Average speed: 3.97 MB/s
```

## Структура проекта

```text
internet-speed-test/
├── main.py
├── requirements.txt
└── README.md
```