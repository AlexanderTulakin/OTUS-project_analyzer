# -*- coding: utf-8 -*-
"""
Модуль для работы с библиотекой NLTK (для обработки естественного языка)
"""
import logging

from nltk import pos_tag

logger = logging.getLogger(__name__)


def is_verb(word: str) -> bool:
    """
    Является ли указанное слово глаголом
    """
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'
