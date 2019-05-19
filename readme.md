# Project Analyzer
Модуль для анализа проектов на Python.

Скрипт выводит список наиболее часто встречающихся глаголов в функциях.
Результат выводится в консоль. 

Пример результата:

```
total 31 words, 3 unique
get 22
save 7
add 2
```
Список проектов для анализа указывается в project_analyzer/__main__.py. 

По умолчанию анализируются проекты:
* django
* flask
* pyramid
* reddit
* requests
* sqlalchemy

Так же возможно использование в качестве библиотеки. Подробности [ниже](#использование_в_качестве_библиотеки).

## Как работает

В указанном проекте находятся все Python файлы. 
Исходный код парсится с помощью [AST](https://docs.python.org/3/library/ast.html)

Для определения частей речи (существительное, глагол и пр.) используется [Natural Language Toolkit](http://www.nltk.org)

## Требования

* Python >= 3.6
* nltk 


## Установка с помощью [GitHub](https://github.com/AlexanderTulakin/OTUS-project_analyzer)
```
$ git clone https://github.com/AlexanderTulakin/OTUS-project_analyzer.git
$ cd OTUS-project_analyzer
$ python setup.py install
```
Далее требуется [установить модель для NLTK](#установка_модели_для_nltk)

Для запуска выполнить команду
```
$ project_analyzer
```

## Запуск с помощью [Github](https://github.com/AlexanderTulakin/OTUS-project_analyzer) без установки
Модуль можно запустить без установки выполнив следующие шаги:
1. Склонировать или установить [репозиторий](https://github.com/AlexanderTulakin/OTUS-project_analyzer)
2. Открыть терминал и перейти в каталог с проектом
3. Выполнить ```python -m pip install -r requirements.txt```
4. [Установить модель для NLTK](#установка_модели_для_nltk)

Теперь для запуска выполнить ```python -m project_analyzer```.


## Установка модели для NLTK
Предварительно требуется установить модель для модуля NLTK для разметки слов по частям речи.
Сделать это можно с помощью команды:

```shell
 $ python nltk.downloader averaged_perceptron_tagger`
```

Если при установке возникает ошибка `SSL: CERTIFICATE_VERIFY_FAILED`, то по её исправлению можно почитать на
[stackoverflow](https://stackoverflow.com/questions/41348621/ssl-error-downloading-nltk-data)

## Использование в качестве библиотеки

Доступные функции:
* get_verbs_in_proj_functions - получить все глаголы из наименований функций в Python файлах для указанного проекта
* get_top_verbs_in_proj_functions - получить топ глаголов из наименований функций в Python файлах для указанного проекта
    с группировкой по частоте встречаемости
* get_top_functions_in_proj - получить топ функций в Python файлах для указанного проекта
* get_words_in_proj_functions - получить все слова из наименований функций в Python файлах для указанного проекта

Пример:

```python
>>> import project_analyzer

>>> project_analyzer.get_top_verbs_in_proj_functions('requests', top_size=2)

[('get', 10), ('save', 5)]
