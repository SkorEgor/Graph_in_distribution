from PyQt5 import QtWidgets
from label_antennas_field.label_antennas_field import LabelAntennasField
from gui_modal import Ui_Dialog
#
#
# class ScheduleToDistribution(Ui_Dialog):
#
#     def __init__(self, dialog):
#         # Создаем окно
#         Ui_Dialog.__init__(self)
#         self.setupUi(dialog)  # Устанавливаем пользовательский интерфейс
#
#         # ПОЛЯ КЛАССА
#
#         # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QDateTimeEdit, QDialogButtonBox, QApplication)
from PyQt5.QtCore import QDateTime, Qt


class DateDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)
        self.setupUi(self)

        self.label_field_antennas = LabelAntennasField()
        self.plotLayout.addWidget(self.label_field_antennas)

        # OK and Cancel buttons
        buttons = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        self.layout_message_buttons.addWidget(buttons)

    # static method to create the dialog and return (date, time, accepted)
    @staticmethod
    def getDateTime(parent=None):
        dialog = DateDialog(parent)
        result = dialog.exec_()
        return (5, 6, result == QDialog.Accepted)