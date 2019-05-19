# -*- coding: utf-8 -*-
"""
Модуль для работы с файловой системой
"""
import logging
import pathlib

logger = logging.getLogger(__name__)


def get_python_files_for_proj(project, max_files=100):
    """
    :param project: путь до проекта
    :param max_files: максимальное количество файлов для анализа

    :return: список Python файлов
    """
    logger.debug(f'Find python files for project "{project}"')
    python_files = []
    for python_file in pathlib.Path(project).rglob('*.py'):
        python_files.append(str(python_file))
        if len(python_files) == max_files:
            break
    logger.debug(f'found ({len(python_files)}): {python_files}')
    return python_files
