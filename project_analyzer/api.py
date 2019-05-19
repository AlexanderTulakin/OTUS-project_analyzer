# -*- coding: utf-8 -*-
"""
Модуль для публичного API библиотеки
"""
from project_analyzer.ast_helper import *
from project_analyzer.common import *
from project_analyzer.fs_helper import *

logger = logging.getLogger(__name__)


def get_verbs_in_proj_functions(proj_path):
    """
    Получить все глаголы из наименований функций в Python файлах для указанного проекта
    """
    return [word for word in get_words_in_proj_functions(proj_path) if is_verb(word)]


def get_top_verbs_in_proj_functions(proj_path, top_size=None):
    """
    Получить топ глаголов из наименований функций в Python файлах для указанного проекта
    с группировкой по частоте встречаемости.

    :param proj_path: путь до проекта для анализа
    :param top_size: сколько элементов выводить. Если не указан, то выводятся все элементы
    """
    total_verbs = get_verbs_in_proj_functions(proj_path)
    return get_top_words(total_verbs, top_size)


def get_top_functions_in_proj(proj_path, top_size=None):
    """
    Получить топ функций в Python файлах для указанного проекта

    :param proj_path: путь до проекта для анализа
    :param top_size: сколько элементов выводить. Если не указан, то выводятся все элементы
    """
    fncs = []
    for filename in get_python_files_for_proj(proj_path):
        fncs.extend(get_functions(filename))
    return get_top_words(fncs, top_size)


def get_words_in_proj_functions(proj_path):
    """
    Получить все слова из наименований функций в Python файлах для указанного проекта
    """
    words = []
    for filename in get_python_files_for_proj(proj_path):
        fncs = get_functions(filename)
        logger.debug(f'List of functions for {filename} ({len(fncs)}): {fncs}')
        for function_name in fncs:
            words.extend(split_snake_case_name_to_words(function_name))
    logger.debug(f'List of words ({len(words)}): {words}')
    return words
