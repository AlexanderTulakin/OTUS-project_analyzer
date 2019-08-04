# -*- coding: utf-8 -*-
"""
Функции "общего" назначения
"""
import collections
import logging

logger = logging.getLogger(__name__)


def get_top_words(words, top_size=None):
    """
    Получить top_size наиболее часто встречающихся слов с группировкой по частоте встречаемости

    :param words: список слов
    :param top_size: сколько элементов выводить. Если не указан, то выводятся все элементы
    """
    return {item[0]: item[1] for item in collections.Counter(words).most_common(top_size)}


def is_magic_func(func_name):
    """
    Является ли функция "магической" в Python смысле
    """
    return func_name.startswith('__') and func_name.endswith('__')


def split_snake_case_name_to_words(name):
    """
    Получить список слов из наименования функции/переменной
    Разделить для слов - нижнее подчеркивание

    Пример:
        'get_words_from_name' -> ['get', 'words', 'from', 'name']
    """
    return [word for word in name.split('_')]
