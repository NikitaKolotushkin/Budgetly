#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt6.QtWidgets import QApplication

from MainWindow import MainWindow


__author__ = 'NikitaKolotushkin'
__version__ = '0.1a'
__license__ = 'GPL-3.0 License'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    # sys.exit(app.exec())
    app.exec()