# -*- coding: utf-8 -*-
"""
Отчет top_word
Выводит список наиболее часто встречающихся указанных частей речи в функциях/классах/переменных
"""
import logging

import project_analyzer.common as common
from project_analyzer.ast_helper import ASTMixin
from project_analyzer.nltk_helper import NLTKMixin
from project_analyzer.reports_common import ReportBase

logger = logging.getLogger(__name__)


class ReportTopWord(ReportBase, NLTKMixin, ASTMixin):

    def generate(self):
        """
        Сгенерировать отчет. Результат должен быть записан в
        self.rep_dict['header'] - заголовок (строка)
        self.rep_dict['body'] - тело (словарь)
        """
        analyze_objects = []
        for filename in self.files:
            analyze_objects.extend(self.get_obj_names(filename))
        logger.debug(f'Объекты для анализа: {analyze_objects}')

        words = []
        for analyze_object in analyze_objects:
            words.extend(self.get_words_from_name(analyze_object))
        logger.debug(f'Итоговые слова: {words}')

        top_words = common.get_top_words(words, self.rep_params.top_size)

        self.rep_dict['header'] = f'total {len(words)} words, {len(set(words))} unique'
        self.rep_dict['body'] = top_words
        logger.debug(f'Результат: {self.rep_dict}')
