# -*- coding: utf-8 -*-
"""
Модуль для работы с библиотекой NLTK (для обработки естественного языка)
"""
import logging

from nltk import pos_tag

import project_analyzer.common as common

logger = logging.getLogger(__name__)


class NLTKMixin:
    def is_verb(self, word: str) -> bool:
        """
        Является ли указанное слово глаголом
        """
        return self._is_chosen_pos(word, ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'])

    def is_noun(self, word: str) -> bool:
        """
        Является ли указанное слово существительным
        """
        return self._is_chosen_pos(word, ['NN', 'NNS', 'NNP', 'NNPS'])

    @staticmethod
    def _is_chosen_pos(word: str, pos: list) -> bool:
        """
        Принадлежит ли слово указанным типам NLTK
        """
        if not word:
            return False
        pos_info = pos_tag([word])
        return pos_info[0][1] in pos

    def is_chosen_word_type(self, word, word_type):
        """
        Принадлежит ли слово указанной части речи
        """
        if word_type == 'noun':
            return self.is_noun(word)
        elif word_type == 'verbs':
            return self.is_verb(word)
        else:
            raise Exception(f'Часть речи "{word_type}" не поддерживается')

    def get_words_from_name(self, name) -> list:
        """
        Получить список слов определенной части речи из наименования функции/переменной
        Предполагается, что наименования сформированы по snake_case

        Пример:
            'get_words_from_name' -> ['get']

        Используемые объекты:
            self.rep_params.word_type - интересующая часть речи. Например, verbs
        """
        return [word for word in common.split_snake_case_name_to_words(name)
                if self.is_chosen_word_type(word, self.rep_params.word_type)]
