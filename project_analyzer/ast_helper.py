# -*- coding: utf-8 -*-
"""
Модуль для парсинга кода на Python и обработки полученных результатов
"""
import ast
import logging

from project_analyzer.common import is_magic_func

logger = logging.getLogger(__name__)


class ASTMixin:
    @staticmethod
    def _parse_ast(filename):
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

    @staticmethod
    def _is_func(element):
        """
        Является ли элемент функцией
        """
        return isinstance(element, ast.FunctionDef)

    @staticmethod
    def _is_var(element):
        """
        Является ли элемент переменной
        """
        return isinstance(element, ast.Name)

    def _get_functions(self, filename):
        """
        Получить список функций (как node из AST) из файла, исключая "магические" функции
        """
        syntax_tree = self._parse_ast(filename)
        functions = []
        for node in ast.walk(syntax_tree):
            if self._is_func(node) and not is_magic_func(node.name):
                functions.append(node)
        return functions

    def _get_local_vars_name(self, filename):
        """
        Получить список локальных переменных внутри функций
        """
        local_vars = []
        for func in self._get_functions(filename):
            for node_in_func in func.body:
                if isinstance(node_in_func, ast.Assign) and self._is_var(node_in_func.targets[0]):
                    local_vars.append(node_in_func.targets[0].id)
        return local_vars

    def _get_functions_name(self, filename):
        """
        Получить список наименований функций
        """
        return [func.name.lower() for func in self._get_functions(filename)]

    def get_obj_names(self, filename):
        """
        Получить список объектов для анализа
        Используемые объекты:
            self.rep_params.analyze_obj - какие объекты требуются для анализа

        :param filename: имя файла дла анализа

        :return: список объектов для анализа
        :rtype: list
        """
        if self.rep_params.analyze_obj == 'functions':
            return self._get_functions_name(filename)
        elif self.rep_params.analyze_obj == 'local_vars':
            return self._get_local_vars_name(filename)
        else:
            raise Exception(f'Объекты "{self.rep_params.analyze_obj}" не доступны для анализа')
