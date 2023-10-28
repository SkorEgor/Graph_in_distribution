from gui import Ui_Dialog
#from schedule_to_distribution import ScheduleToDistribution
from schedule_to_distribution import DateDialog

from label_antennas_field.label_antennas_field import LabelAntennasField
from PyQt5.QtCore import Qt


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog, QApplication
import sys

import sys
from PyQt5 import QtWidgets

# КЛАСС АЛГОРИТМА ПРИЛОЖЕНИЯ
class GuiProgram(Ui_Dialog):

    def __init__(self, dialog):
        # Создаем окно
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)  # Устанавливаем пользовательский интерфейс

        # ПОЛЯ КЛАССА
        self.dialog2 = None
        self.program2 = None

        # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ
        self.pushButton.clicked.connect(self.open)


    def open(self):
        # self.app2 = Modal2()
        # self.app2.show()

        # self.dialog2 = QtWidgets.QDialog()
        # self.program2 = ScheduleToDistribution(self.dialog2)
        # print(self.dialog2.show())

        # dlg = Modal3(self)
        # dlg.exec()

        date, time, ok = DateDialog.getDateTime()
        print("{} {} {}".format(date, time, ok))

