# -*- coding: utf-8 -*-
"""
Модуль для парсинга кода на Python и обработки полученных результатов
"""
import ast
import logging

from project_analyzer.common import is_magic_func

logger = logging.getLogger(__name__)


def parse_ast(filename):
    """
    Распарсить файл в AST (abstract syntax tree)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return ast.parse(file.read(), filename=filename)
    except Exception as ex:
        logger.warning(f'Ошибка при разборе файла {filename}')
        logger.exception(ex)
        return None


def is_func(element):
    """
    Является ли элемент функцией
    """
    return isinstance(element, ast.FunctionDef)


def get_functions(filename):
    """
    Получить список функций из файла, исключая "магические" функции
    """
    syntax_tree = parse_ast(filename)
    functions = []
    for node in ast.walk(syntax_tree):
        if is_func(node) and not is_magic_func(node.name):
            functions.append(node.name.lower())
    return functions
