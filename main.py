#! /usr/bin/env python
# -*- coding: UTF-8 -*-
u"""主模块."""

import sys

sys.path.append('conf')
sys.path.append('src')
try:
    from main_service import MainService
    from log_helper import DEBUG, INFO, WARN, ERROR  # noqa
except Exception:
    raise


def main():
    u"""入口函数."""
    if len(sys.argv) < 2:
        sys.stderr.write('%s <base_dir>!\n' % (sys.argv[0]))
        sys.exit(-1)
    base_dir = sys.argv[1]

    # 主服务
    main_service = MainService()

    # 具体的处理
    main_service.entrance(base_dir)


if __name__ == '__main__':
    main()


# vim: et sta sw=4 sts=4
