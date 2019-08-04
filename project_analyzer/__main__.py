# -*- coding: utf-8 -*-
import logging
import sys

from project_analyzer import cli
from project_analyzer.project import Project
from project_analyzer.repository import Repo

logger = logging.getLogger()

ENABLE_LOG = True


def setup_logger():
    """
    Настройка логирования
    """
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(name)-35s(ln:%(lineno)04d) %(levelname)-05s: %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def run():
    try:
        if ENABLE_LOG:
            setup_logger()
        params, rep_params = cli.create_parser()
        logger.info(f'Запуск утилиты с параметрами: {params}')
        logger.info(f'Параметры отчета: {rep_params}')
        if params.repo_url:
            params.path = Repo(params.repo_url, params.repo_type).get()
        project = Project(params.path, params.lang, params.max_files)
        project.generate_report(params.rep_name, params.rep_format, params.rep_outp, rep_params)
    except Exception as ex:
        logger.exception(ex)
        raise


if __name__ == '__main__':
    run()
