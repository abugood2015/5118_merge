#! /usr/bin/env python
# -*- coding: UTF-8 -*-
u"""日期时间相关的工具模块."""

import time


def today_monthday():
    u"""获取今天日期, 只包含月份和日期, 比如"08-09", "08-24"等.

    Returns 今天日期
    """
    time.strftime('%m-%d', time.localtime(time.time()))
################################################################################


def human_time_now():
    u"""当前日期时间.

    Return 给人看的日期时间
    """
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def human_time(ts):
    u"""将时间戳转换为可读字符串.

    Args
        `ts` 时间戳, 单位秒.

    Return 给人看的日期时间
    """
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


def this_month():
    u"""本月字符串.

    Return 月份字符串, 比如 "201007" 表示2010年7月份.
    """
    return time.strftime('%Y%m', time.localtime(time.time()))


def next_month():
    u"""下月字符串.

    Return 月份字符串, 比如 "201007" 表示2010年7月份.
    """
    return time.strftime('%Y%m', time.localtime(time.time() + 30*24*3600))


def last_month():
    u"""上月字符串.

    Return 月份字符串, 比如 "201007" 表示2010年7月份.
    """
    return time.strftime('%Y%m', time.localtime(time.time() - 30*24*3600))


# vim: et sta sw=4 sts=4
