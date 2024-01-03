#! /usr/bin/env python
# -*- coding: UTF-8 -*-
u"""Excel模块."""

import sys

import xlsxwriter


sys.path.append('conf')
try:
    from log_helper import DEBUG, INFO, WARN, ERROR  # noqa
except Exception:
    raise


class ExcelWriter:
    u"""Excel写入器."""

    @staticmethod
    def write(excel_file, items):
        u"""创建并写入Excel文件.

        Args
            `excel_file` 文件名.
            `items`      数据项列表.
        """
        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook(excel_file)
        worksheet = workbook.add_worksheet()

        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': True, 'align': 'center'})
        bold.set_font_name('微软雅黑')
        bold.set_font_size(10)
        bold.set_align('center')
        bold.set_align('vcenter')

        # 表头
        worksheet.write(0, 0, '关键词', bold)

        # 设置列宽
        worksheet.set_column(0, 0, 25.38)

        # 单元格格式
        text_cell_fm = workbook.add_format({'font_name': '微软雅黑', 'font_size': 10})
        text_cell_fm.set_align('left')
        text_cell_fm.set_align('vcenter')

        row_idx = 1
        for item in items:
            worksheet.write(row_idx, 0, item, text_cell_fm)

            row_idx += 1

        workbook.close()


# vim: et sta sw=4 sts=4
