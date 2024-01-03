#! /usr/bin/env python
# -*- coding: UTF-8 -*-
u"""输出模块."""

import sys

sys.path.append('conf')
try:
    from config import Config
    from excel_writer import ExcelWriter
    from log_helper import DEBUG, INFO, WARN, ERROR  # noqa
except Exception:
    raise


class ClassifyOutput:
    u"""分类输出器."""

    def __init__(self, filename, keywords_list):
        u"""初始化.

        Args
            `filename`      文件名
            `keywords_list` 关键词列表
        """
        self.fullname = f'{Config.Main.OUTPUT_DIR}/{filename}'
        self.keywords_set = set(keywords_list)
        self.words_list = []

    def judge(self, word):
        u"""判断关键词是否属于本分类器.

        Args
            `word` 目标关键词

        Returns True: 属于.
               False: 不属于.
        """
        for keyword in self.keywords_set:
            if -1 != word.find(keyword):
                self.words_list.append(word)
                return True
        return False

    def save(self):
        u"""保存."""
        ExcelWriter.write(self.fullname, self.words_list)


# vim: et sta sw=4 sts=4
