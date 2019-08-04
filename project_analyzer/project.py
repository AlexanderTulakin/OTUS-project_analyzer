# -*- coding: utf-8 -*-
"""
Модуль по работе с проектами
"""
import logging

from project_analyzer.fs_helper import FSMixin
from project_analyzer.report_top_word import ReportTopWord

logger = logging.getLogger(__name__)


class Project(FSMixin):
    def __init__(self, path, lang, max_files):
        """
        Инициализия проекта

        :param path: путь до расположения проекта
        :param lang: язык, на котором написан проекта. Например, python
        :param max_files: максимальное количество файлов для анализа
        """
        logger.debug(f'Инициализируем {lang} проект {path}')
        logger.debug(f'Максимум файлов для анализа: {max_files}')
        self.path = path
        self.lang = lang.lower()
        self.max_files = max_files
        self._get_files_for_proj()

    def generate_report(self, rep_name, rep_format, rep_outp, rep_params):
        """
        Сформировать отчет

        :param rep_name: имя отчета. Например, top_words
        :param rep_format: формат генерируемого отчета. Например, json
        :param rep_outp: куда выводить отчет. Например, stdout
        :param rep_params: параметры конкретного отчета
        """
        logger.debug(f'Генерируем отчет {rep_name}')
        if rep_name.lower() == 'top_words':
            report = ReportTopWord(self.files, rep_params, rep_format, rep_outp)
        else:
            raise Exception(f'Отчёт {rep_name} не поддерживается')
        report.generate()
        report.format_report()
        report.save_report()
