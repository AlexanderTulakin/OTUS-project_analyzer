# -*- coding: utf-8 -*-
"""
Модуль для работы с командной строкой
"""
import argparse
import logging

from validator_collection import validators, errors

logger = logging.getLogger(__name__)


def check_positive(value):
    """
    Проверка, что введенное значение есть положительное целочисленное число

    :raises argparse.ArgumentTypeError:  в случае невалидного значения
    """
    try:
        return validators.integer(value, allow_empty=True, minimum=1)
    except errors.MinimumValueError:
        raise argparse.ArgumentTypeError(f'{value} should be positive number')
    except errors.NotAnIntegerError:
        raise argparse.ArgumentTypeError(f'{value} is not an integer')


def check_path(path):
    """
    Проверка, что введенное значение есть валидный и существующий путь на файловой системе

    :raises argparse.ArgumentTypeError:  в случае невалидного значения
    """
    try:
        return validators.directory_exists(path)
    except errors.PathExistsError:
        raise argparse.ArgumentTypeError(f'{path} does not exist on the local filesystem')
    except errors.NotPathlikeError:
        raise argparse.ArgumentTypeError(f'{path} is not a path-like object')
    except errors.NotADirectoryError:
        raise argparse.ArgumentTypeError(f'{path} is not a valid directory')


def validate_args(parser, args):
    """
    Дополнительный проверки значений командной строки
    """
    if (args.repo_url and args.path) or (not args.repo_url and not args.path):
        parser.error("Need one of param: repo_url or path")


def create_parser():
    """
    Создать парсер командной строки

    :return общие параметры, параметры конкретного отчета
    """
    parser = argparse.ArgumentParser(prog='project_analyzer', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    proj_paths = parser.add_argument_group('Project paths', 'Allowed one of param: repo_url+repo_type or path')
    proj_paths.add_argument('--repo_url', help='Source url (if need to download)', type=validators.url)
    proj_paths.add_argument('--repo_type', help='Source type', choices=['git'], default='git')
    proj_paths.add_argument('--path', help='Path to existing project', type=check_path)

    proj_group = parser.add_argument_group('Project attributes')
    proj_group.add_argument('--lang', help='Language of source code', choices=['python'], default='python')
    proj_group.add_argument('--max_files', help='Max files for analyse', type=check_positive, default=100)

    rep_group = parser.add_argument_group('Report attributes')
    rep_group.add_argument('--rep_format', help='Report format', choices=['json', 'csv', 'text'], default='text')
    rep_group.add_argument('--rep_outp', help='Output - file name or stdout', default='stdout')

    rep_name = parser.add_subparsers(title='Report name', required=True, dest='rep_name')
    top_words = rep_name.add_parser('top_words', help='return top words used in project code.'
                                                      'In default count verbs in functions.')

    top_words.add_argument('--word_type', help='Type of words for analyze', choices=['noun', 'verbs', 'all'],
                           default='verbs')
    top_words.add_argument('--analyze_obj', help='What kind of object need to analyze',
                           choices=['functions', 'local_vars'], default='functions')
    top_words.add_argument('--top_size', help='Count of top words', type=check_positive, default=None)

    # parser.print_help()
    # top_words.print_help()
    parsed_args = parser.parse_args()
    validate_args(parser, parsed_args)
    report_args = argparse.Namespace()
    if parsed_args.rep_name == 'top_words':
        report_args = top_words.parse_known_args()[0]

    return parsed_args, report_args
