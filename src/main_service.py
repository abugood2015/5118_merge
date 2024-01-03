#! /usr/bin/env python
# -*- coding: UTF-8 -*-
u"""主服务模块."""

import os
import sys

sys.path.append('conf')
try:
    from config import Config
    from five_one_one_eight import Reader5118
    from excel_writer import ExcelWriter
    from classify_output import ClassifyOutput
    from log_helper import DEBUG, INFO, WARN, ERROR  # noqa
except Exception:
    raise


class MainService(object):
    u"""主服务类."""

    def __init__(self):
        u"""初始化."""
        # 词的集合
        self.words_set = set()

        # 分类器的列表
        self.classifier_list = []
        for tp in Config.Main.CLASSIFY_OUTPUT:
            self.classifier_list.append(ClassifyOutput(tp[0], tp[1]))

    def entrance(self, base_dir):
        u"""入口.

        Args
            `base_dir` 基础路径
        """
        # 读取长尾词
        self.read_impl(Reader5118.read_longtail, f'{base_dir}/{Config.Main.LONGTAIL_DIR_NAME}')
        # 读取全网下拉词.
        self.read_impl(Reader5118.read_all_suggest, f'{base_dir}/{Config.Main.ALL_SUGGEST_DIR_NAME}')
        # 读取下拉词深度搜索
        self.read_impl(Reader5118.read_deep_suggest, f'{base_dir}/{Config.Main.DEEP_SUGGEST_DIR_NAME}')

        # 按长度排序
        sorted_list = sorted(self.words_set, key=lambda i: len(i), reverse=True)

        # 未分类关键词列表
        unclassified_list = []
        # 遍历每个关键词
        for word in sorted_list:
            # 判断是否过滤
            b_filter = False
            for fw in Config.Main.FILTER_SET:
                if -1 != word.find(fw):
                    b_filter = True
                    break
            if b_filter:
                continue

            b_judge = False
            for classifier in self.classifier_list:
                if classifier.judge(word):
                    b_judge = True
                    break
            if not b_judge:
                unclassified_list.append(word)

        # 输出
        for classifier in self.classifier_list:
            classifier.save()
        ExcelWriter.write(f'{Config.Main.OUTPUT_DIR}/{Config.Main.OUTPUT_FILENAME}', unclassified_list)

        INFO('done.')
    ############################################################################

    def read_impl(self, func, fullpath):
        u"""读取的具体实现.

        Args
            `func`     读取函数
            `fullpath` 完整路径
        """
        # 路径不存在
        if not os.path.exists(fullpath):
            return

        filenames = os.listdir(fullpath)
        for filename in filenames:
            fullname = f'{fullpath}/{filename}'
            words = func(fullname)
            for word in words:
                self.words_set.add(word)
            INFO(f'done: {fullname}')


if __name__ == '__main__':
    main = MainService()


# vim: et sta sw=4 sts=4
