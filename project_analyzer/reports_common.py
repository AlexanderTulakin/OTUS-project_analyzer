# -*- coding: utf-8 -*-
"""
Модуль по работе с отчетами
"""
import json
import logging
import pathlib

logger = logging.getLogger(__name__)


class ReportOutpMixin:
    """
    Миксин для вывода отчета. Возможен вывод или в файл или в stdout.
    Используются объекты:
        self.rep_outp       - куда выводить отчет
        self.formated_rep   - форматированный текст отчета
    """
    @staticmethod
    def _save_to_file(filename, content):
        pathlib.Path(filename).write_text(content)

    @staticmethod
    def _save_to_stdout(content):
        print(content)

    def save_report(self):
        if self.rep_outp == 'stdout':
            self._save_to_stdout(self.formated_rep)
        else:
            self._save_to_file(self.rep_outp, self.formated_rep)


class ReportFormatMixin:
    """
    Миксин для форматирования отчета. Возможные форматы: текст, csv, json
    Используемые объекты:
        self.rep_format     - формат отчета
        self.formated_rep   - форматированный вывод отчета
    """
    @staticmethod
    def _format_to_json(rep_dict):
        return json.dumps(rep_dict, indent=2)

    @staticmethod
    def _format_to_csv(rep_dict):
        result = f'{rep_dict["header"]};\n'
        for key, value in rep_dict['body'].items():
            result += f'{key};{value}\n'

        return result.rstrip()

    @staticmethod
    def _format_to_text(rep_dict):
        result = f'{rep_dict["header"]}\n\n'
        for key, value in rep_dict['body'].items():
            result += f'{key}: {value}\n'

        return result.rstrip()

    def format_report(self):
        if self.rep_format == 'json':
            self.formated_rep = self._format_to_json(self.rep_dict)
        elif self.rep_format == 'csv':
            self.formated_rep = self._format_to_csv(self.rep_dict)
        elif self.rep_format == 'text':
            self.formated_rep = self._format_to_text(self.rep_dict)
        else:
            raise Exception(f'Формат {self.rep_format} не поддерживается')


class ReportBase(ReportFormatMixin, ReportOutpMixin):
    def __init__(self, files, rep_params, rep_format, rep_outp):
        """
        Инициализация базового класса для отчетов

        :param files: список файлов для анализа
        :param rep_params: параметры отчета
        :param rep_format: формат вывода
        :param rep_outp: куда выводить отчёт
        """
        self.files = files
        self.rep_params = rep_params
        self.rep_format = rep_format
        self.rep_outp = rep_outp
        self.rep_dict = {'header': '', 'body': []}

    def generate(self):
        raise NotImplementedError
