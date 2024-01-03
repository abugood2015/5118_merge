#! /usr/bin/env python
# -*- coding: UTF-8 -*-
u"""5118模块."""

import sys

import pandas as pd

sys.path.append('conf')
try:
    from config import Config
    from log_helper import DEBUG, INFO, WARN, ERROR  # noqa
except Exception:
    raise


class Reader5118:
    u"""5118读取器."""

    @staticmethod
    def read_longtail(filename):
        u"""读取长尾词.

        Args
            `filename` csv文件

        Returns 词列表
        """
        words = []

        df = pd.read_csv(filename, encoding='gb18030')
        for row in df.itertuples():
            words.append(getattr(row, '关键词'))

        return words

    @staticmethod
    def read_all_suggest(filename):
        u"""读取全网下拉词.

        Args
            `filename` csv文件

        Returns 词列表
        """
        words = []

        df = pd.read_csv(filename, encoding='gb18030', skiprows=Config.Main.SUGGEST_CSV_SKIP_ROWS)
        for row in df.itertuples():
            # 平台
            platform = getattr(row, '关键词')
            # 判断是否要过滤
            if platform in Config.Main.FILTER_SUGGEST_PLATFORM_SET:
                continue
            word = getattr(row, '搜索词')
            words.append(word)

        return words

    @staticmethod
    def read_deep_suggest(filename):
        u"""读取下拉词深度搜索.

        Args
            `filename` csv文件

        Returns 词列表
        """
        words = []

        df = pd.read_csv(filename, encoding='gb18030', skiprows=Config.Main.DEEP_CSV_SKIP_ROWS)
        for row in df.itertuples():
            word = getattr(row, '关键词')
            words.append(word)

        return words


# vim: et sta sw=4 sts=4
