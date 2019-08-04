# -*- coding: utf-8 -*-
"""
Модуль для работы с репозиториями
"""
import logging
import pathlib

import git

logger = logging.getLogger(__name__)


class Repo:
    def __init__(self, url, type_):
        """
        Инициализация репозитория

        :param url: ссылка до репозитория
        :param type_: тип репозитория, например git
        """
        logger.debug(f'Инициализируем репозиторий {self.url} типа {self.type}')
        self.url = url

        self.type = type_.lower()
        self.path = None
        if self.type != 'git':
            raise Exception(f'Репозиторий с типом {self.type} не поддерживается')

    def _git_clone(self, ignore_exist=True):
        self.path = pathlib.PurePath(self.url).stem
        try:
            git.Repo.clone_from(self.url, self.path)
        except git.exc.GitCommandError as ex:
            if ignore_exist and 'already exists and is not an empty directory' in ex.stderr:
                logger.warning(ex.stderr)
            else:
                raise

    def get(self, ignore_exist=True):
        """
        Скачивать репозиторий в каталог с именем репозитория в место, откуда запускается скрипт

        :param ignore_exist: если True, то игнорировать, что путь куда скачивается репозиторий уже существует
        :return: путь, куда скачен репозиторий
        """
        logger.debug(f'Скачиваем репозиторий')
        if self.type == 'git':
            self._git_clone(ignore_exist)
        logger.debug(f'Путь, куда скачен репозиторий: {self.path}')
        return self.path
