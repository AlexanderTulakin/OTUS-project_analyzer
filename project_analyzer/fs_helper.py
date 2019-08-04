# -*- coding: utf-8 -*-
"""
Модуль для работы с файловой системой
"""
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class FSMixin:
    def _get_files_for_proj(self):
        """
        Возвращает все файлы указанного языка для указанного проекта в переменную self.files.
        """
        logger.debug(f'Ищем {self.lang} файлы для проекта "{self.path}"')
        patterns = {'python': '*.py'}
        pattern = patterns[self.lang]
        if not pattern:
            raise Exception(f'Язык {self.lang} не поддерживается')

        self.files = []
        for proj_file in Path(self.path).rglob(pattern):
            self.files.append(str(proj_file))
            if len(self.files) == self.max_files:
                break
        logger.debug(f'Найдено ({len(self.files)}): {self.files}')
