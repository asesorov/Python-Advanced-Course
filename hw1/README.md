# Homework 1

## Task 1.1
Написать упрощенный вариант утилиты `nl` -- скрипт, который выдает в `stdout` пронумерованные строки из файла.
Если файл не передан, то скрипт читает строки из `stdin`.

Он должен работать так же, как `nl -b a`.

Запуск: `python numlines.py [optional: input file path]`

Исходный код: [numlines.py](task_1/numlines.py)

Артефакты: [здесь](task_1/artifacts)

Пример вывода: [output.txt](task_1/artifacts/output.txt)

## Task 1.2
Написать упрощенный вариант утилиты `tail` -- скрипт, выводящий в `stdout` последние 10 строк каждого из переданных файлов.

- если передано больше одного файла, то перед обработкой очередного файла необходимо вывести его имя. Подробности смотрите в оригинальной утилите `tail`, ваш скрипт должен повторять форматирование.
- если не передано ни одного файла, то нужно вывести последние 17 строк из `stdin`.

Запуск: `python tail.py [optional: input files paths]` (выведет последние 10 строк для каждого файла с названием файла)

Запуск (передавая содержимое файла в stdin): `python tail.py < file_path` (выведет последние 17 строк)

Исходный код: [tail.py](task_2/tail.py)

Артефакты: [здесь](task_2/artifacts)

Пример вывода: [output.txt](task_2/artifacts/output.txt)

## Task 1.3
Написать скрипт, работающий так же, как утилита `wc`, вызванная без дополнительных опций.
Т.е. для каждого переданного файла утилита выводит статистику (3 числа) и имя файла.

При этом:
- если передано больше одного файла, то в самом конце утилита выводит суммарную статистику (total),
- если ни одного файла не передано, то утилита считывает весь вход и печатает для него статистику без имени.

Запуск: `python tail.py [optional: input files paths]` (выведет число строк, число слов, число байт, имя файла)

Запуск (передавая содержимое файла в stdin): `python tail.py < file_path` (выведет число строк, число слов, число байт)

Исходный код: [wc.py](task_3/wc.py)

Артефакты: [здесь](task_3/artifacts)

Пример вывода: [output.txt](task_3/artifacts/output.txt)
