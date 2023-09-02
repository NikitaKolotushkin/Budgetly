#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt6.QtCore import Qt
from PyQt6 import QtGui, QtMultimedia, uic, QtCore
from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('ui_templates/MainWindow.ui', self)