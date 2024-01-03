#! /usr/bin/env python
# -*- coding: UTF-8 -*-
u"""
自定义日志类.

使用方法:
1) 导入
from log_helper import DEBUG,INFO,WARN,ERROR
2) 使用
DEBUG(xxx)
INFO(xxx)
WARN(xxx)
ERROR(xxx)
"""
import logging
import logging.handlers
import os
import sys

sys.path.append('conf')
try:
    from config import Config
except Exception:
    raise


class LogHelper(object):
    u"""日志."""

    def __init__(self):
        u"""初始化."""
        if not os.path.exists(Config.LOG.LOG_DIR):
            os.makedirs(Config.LOG.LOG_DIR)
        self.debug_logger = LogHelper.create_debug_log()
        self.info_logger = LogHelper.create_info_log()
        self.warn_logger = LogHelper.create_warn_log()

    @staticmethod
    def create_debug_log():
        u"""创建调试日志."""
        logger = logging.getLogger('LogHelper-DebugLog')
        logger.setLevel(logging.DEBUG)

        log_name = Config.LOG.LOG_DIR + '/' + Config.LOG.DEBUG_LOG_NAME
        fh = logging.handlers.RotatingFileHandler(
            log_name,
            maxBytes=Config.LOG.DEBUG_LOG_BYTE,
            backupCount=Config.LOG.DEBUG_LOG_BACKUP)
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s %(message)s', datefmt='%H:%M:%S')
        fh.setFormatter(formatter)

        logger.addHandler(fh)
        return logger

    @staticmethod
    def create_info_log():
        u"""创建信息日志."""
        logger = logging.getLogger('LogHelper-InfoLog')
        logger.setLevel(logging.INFO)

        log_name = Config.LOG.LOG_DIR + '/' + Config.LOG.INFO_LOG_NAME
        fh = logging.handlers.RotatingFileHandler(
            log_name,
            maxBytes=Config.LOG.INFO_LOG_BYTE,
            backupCount=Config.LOG.INFO_LOG_BACKUP)
        fh.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s %(filename)s:%(lineno)d %(message)s', datefmt='%m-%d %H:%M:%S')
        fh.setFormatter(formatter)

        logger.addHandler(fh)
        return logger

    @staticmethod
    def create_warn_log():
        u"""创建告警日志."""
        logger = logging.getLogger('LogHelper-WarnLog')
        logger.setLevel(logging.WARNING)

        log_name = Config.LOG.LOG_DIR + '/' + Config.LOG.WARN_LOG_NAME
        fh = logging.handlers.TimedRotatingFileHandler(
            log_name,
            when='D',
            interval=1,
            backupCount=Config.LOG.WARN_LOG_BACKUP)
        fh.setLevel(logging.WARNING)

        formatter = logging.Formatter(
            '%(levelname)s %(asctime)s (%(filename)s:%(lineno)d %(funcName)s) %(message)s',
            datefmt='%m-%d %H:%M:%S')
        fh.setFormatter(formatter)

        logger.addHandler(fh)
        return logger


################################################################################
LOG = LogHelper()
DEBUG = LOG.debug_logger.debug
INFO = LOG.info_logger.info
WARN = LOG.warn_logger.warn
ERROR = LOG.warn_logger.error
################################################################################


# vim: et sta sw=4 sts=4
