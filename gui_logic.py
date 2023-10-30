from gui import Ui_Dialog
from schedule_to_distribution import DateDialog


# КЛАСС АЛГОРИТМА ПРИЛОЖЕНИЯ
class GuiProgram(Ui_Dialog):

    def __init__(self, dialog):
        # Создаем окно
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)  # Устанавливаем пользовательский интерфейс

        # ДЕЙСТВИЯ ПРИ ВКЛЮЧЕНИИ
        self.pushButton.clicked.connect(self.open_and_get_data)

    # открытие модального окна и получения данных
    def open_and_get_data(self):
        print(DateDialog.get_array())
