import openai
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel('언어 선택')
        self.languges = QComboBox()
        self.languges.setFixedWidth(200)
        self.languges.setFixedHeight(30)
    def btn_1_clicked(self):
        openai.api_key = "<OPEN API KEY>"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Say Hello to the World!",
            max_tokens=50,
            temperature=0
        )


if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
