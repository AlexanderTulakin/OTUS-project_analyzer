# -*- coding: utf-8 -*-
import logging
import sys

from project_analyzer import api
from project_analyzer import common

logger = logging.getLogger()

ENABLE_LOG = False
DEF_PROJECTS = ['django',
                'flask',
                'pyramid',
                'reddit',
                'requests',
                'sqlalchemy',
                ]


def setup_logger():
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(module)-10s(ln:%(lineno)04d) %(levelname)-05s: %(message)s')
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def print_top_verbs_result(top_words: list):
    """
    Вывести результат анализа по наиболее часто встречающимся глаголам в консоль
    """
    result = f'total {len(top_words)} words, {len(set(top_words))} unique\n'
    for word, occurrence in top_words:
        result += f'{word} {occurrence}\n'
    print(result.rstrip())


def run():
    if ENABLE_LOG:
        setup_logger()

    total_verbs = []
    for project_path in DEF_PROJECTS:
        total_verbs += api.get_verbs_in_proj_functions(project_path)
    top_words = common.get_top_words(total_verbs, top_size=200)

    print_top_verbs_result(top_words)


if __name__ == '__main__':
    run()
