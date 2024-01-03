#! /usr/bin/env python
# -*- coding: UTF-8 -*-
u"""信号模块."""

import signal
import sys

sys.path.append('conf')
try:
    from log_helper import DEBUG, INFO, WARN, ERROR  # noqa
except Exception:
    raise


class SignalHelper(object):
    u"""信号处理类."""

    # 是否退出
    IS_EXIT = False
    # 中断回调函数, 不带任何参数.
    INTERRUPT_CALLBACK = None

    @staticmethod
    def init():
        u"""初始化."""
        SignalHelper.IS_EXIT = False

        # 捕获: Ctrl-C 组合键信号
        signal.signal(signal.SIGINT, SignalHelper.handle_signal)
        # 捕获: kill pid 时的信号
        signal.signal(signal.SIGTERM, SignalHelper.handle_signal)
        # 捕获: 守护进程发出的关闭信号
        signal.signal(signal.SIGHUP, SignalHelper.handle_signal)

    @staticmethod
    def handle_signal(sig, frame):
        u"""信号处理函数.

        Args
            `sig`   捕获到的信号
            `frame`
        """
        INFO('catch signal_num=%d' % sig)
        SignalHelper.IS_EXIT = True

        # 中断回调
        if SignalHelper.INTERRUPT_CALLBACK is not None:
            SignalHelper.INTERRUPT_CALLBACK()

    @staticmethod
    def exit():
        u"""是否退出.

        Returns True 要退出
               False 还在运行
        """
        return SignalHelper.IS_EXIT


if __name__ == '__main__':
    pass


# vim: et sta sw=4 sts=4
