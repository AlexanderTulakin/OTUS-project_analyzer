# Project Analyzer
Модуль для анализа проектов.

Возможности:
* работа как с git репозиториями, так и с локальными проектами
* анализ проектов на Python
* вывод результата в консоль или в файл
* различные варианты форматирования результата: json, text или csv
* ввод всех параметров через командную строку

На текущий момент доступны отчёты:
* top_words

    Вывод список наиболее часто встречающихся глаголов или существительных в функциях или локальных переменных функций.
    
    Нюансы работы:
    * Исходный код парсится с помощью [AST](https://docs.python.org/3/library/ast.html)
    * Для определения частей речи (существительное, глагол и пр.) используется [Natural Language Toolkit](http://www.nltk.org)
    
    Пример результата:
    ```
    total 4 words, 4 unique

    get: 8
    is: 7
    save: 3
    run: 1
    ```

## Использование

```
project_analyzer [-h] [--repo_url REPO_URL] [--repo_type {git}]
                        [--path PATH] [--lang {python}]
                        [--max_files MAX_FILES] [--rep_format {json,csv,text}]
                        [--rep_outp REP_OUTP]
                        {top_words} ...

optional arguments:
  -h, --help            show this help message and exit

Project paths:
  Allowed one of param: repo_url+repo_type or path

  --repo_url REPO_URL   Source url (if need to download) (default: None)
  --repo_type {git}     Source type (default: git)
  --path PATH           Path to existing project (default: None)

Project attributes:
  --lang {python}       Language of source code (default: python)
  --max_files MAX_FILES Max files for analyse (default: 100)

Report attributes:
  --rep_format {json,csv,text}
                        Report format (default: text)
  --rep_outp REP_OUTP   Output - file name or stdout (default: stdout)

Report name:
  {top_words}
    top_words           return top words used in project code.In default count
                        verbs in functions.
                        
          Params for report:
              --word_type {noun,verbs,all}
                                    Type of words for analyze
              --analyze_obj {functions,local_vars}
                                    What kind of object need to analyze
              --top_size TOP_SIZE   Count of top words                
```

## Требования

* Python >= 3.6
* nltk
* validator-collection
* gitpython


## Установка с помощью [GitHub](https://github.com/AlexanderTulakin/OTUS-project_analyzer)
```
$ git clone https://github.com/AlexanderTulakin/OTUS-project_analyzer.git
$ cd OTUS-project_analyzer
$ python setup.py install
```
Далее [установить модель для NLTK](#установка-модели-для-nltk)

## Установка модели для NLTK
Предварительно требуется установить модель для модуля NLTK для разметки слов по частям речи.
Сделать это можно с помощью команды:

```shell
 $ python nltk.downloader averaged_perceptron_tagger`
```

Если при установке возникает ошибка `SSL: CERTIFICATE_VERIFY_FAILED`, то по её исправлению можно почитать на
[stackoverflow](https://stackoverflow.com/questions/41348621/ssl-error-downloading-nltk-data)

