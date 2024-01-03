#! /usr/bin/env python
# -*- coding: UTF-8 -*-
u"""配置模块."""

import time


class Config(object):
    u"""配置类, 根据不同的需求配置不同的参数."""

    class Main:
        u"""主逻辑的配置."""

        # 长尾词的目录名称
        LONGTAIL_DIR_NAME = '长尾词'
        # 全网下拉词的目录名称
        ALL_SUGGEST_DIR_NAME = '全网下拉词'
        # 下拉词深度搜索的目录名称
        DEEP_SUGGEST_DIR_NAME = '下拉词深度搜索'

        # 全网下拉词csv文件要跳过的前几行
        # 只有三列才是有效的：搜索词 | 关键词 | 平台
        SUGGEST_CSV_SKIP_ROWS = 5
        # 全网下拉词要过滤掉的平台集合
        FILTER_SUGGEST_PLATFORM_SET = set(['京东', '小红书', '天猫', '淘宝', '亚马逊', '拼多多'])

        # 下拉词深度搜索csv文件要跳过的前几行
        DEEP_CSV_SKIP_ROWS = 5

        # 过滤的关键词集合，优先级比下面的分类输出要高！
        FILTER_SET = set(['苦无', '皮肤', '耳机', '彩虹'])
        # 结果输出目录
        OUTPUT_DIR = 'output'
        # 分类结果列表
        # 元素类型：元组，tp[0]表示保存的文件名，tp[1]表示包含的关键词列表。
        CLASSIFY_OUTPUT = [
            ('azami_碧蓝航线.xlsx', ['碧蓝']),
            ('azami_酒吞童子.xlsx', ['酒吞']),
            ('azami_圣路易斯.xlsx', ['圣路易斯']),
            ('azami_鬼灭之刃.xlsx', ['鬼灭之刃']),
            ('azami_甘露寺.xlsx', ['甘露寺']),
            ('azami_南半球.xlsx', ['南半球']),
            ('azami_比基尼.xlsx', ['比基尼']),
            ('azami_玉藻前.xlsx', ['玉藻前']),
            ('azami_甘雨.xlsx', ['甘雨']),
            ('azami_雒雒.xlsx', ['雒雒']),
            ('azami_玛修.xlsx', ['玛修']),
            ('azami_蒂法.xlsx', ['蒂法']),
            ('azami_圣光.xlsx', ['圣光']),
            ('azami_通用.xlsx',
                ['写真', '福利',
                 '美女', '女神', '小姐姐',
                 '图集', '图包', '合集']),
        ]
        # 未分类结果输出文件名
        OUTPUT_FILENAME = f'merge_{time.strftime("%Y%m%d-%H", time.localtime(time.time()))}.xlsx'

    class LOG:
        u"""日志配置."""

        # 日志目录
        LOG_DIR = 'log'

        # debug日志文件名
        DEBUG_LOG_NAME = 'debug.log'
        # debug日志文件最大体积
        DEBUG_LOG_BYTE = 10 * 1024 * 1024
        # debug日志文件最多保留个数(按体积切分)
        DEBUG_LOG_BACKUP = 0

        # info日志文件名
        INFO_LOG_NAME = 'info.log'
        # info日志文件最大体积
        INFO_LOG_BYTE = 30 * 1024 * 1024
        # info日志文件最多保留个数(按体积切分)
        INFO_LOG_BACKUP = 1

        # warn日志文件名
        WARN_LOG_NAME = 'warn.log'
        # warn日志文件最多保留个数(按天切分)
        WARN_LOG_BACKUP = 3


if __name__ == '__main__':
    pass

# vim: et sta sw=4 sts=4
