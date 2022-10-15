import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QListWidget, QLabel, QWidget, QVBoxLayout
from PyQt6 import QtCore, QtGui, QtWidgets



class MainWindow(QMainWindow):

    # Initialising the GUI
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("layout.ui", self)
        self.viewSched.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ViewSchedule))
        self.manSched.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ManageSchedule))
        self.records.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Records))
        self.logout.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Logout))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open('stylesheet.css').read())
    window = MainWindow()
    window.show()
    app.exec()

