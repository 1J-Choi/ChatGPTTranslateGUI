import openai
import sys
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1 = QLabel('언어 선택')
        label2 = QLabel('입력')
        label3 = QLabel('결과')

        self.languges = QComboBox()
        self.languges.setFixedWidth(200)
        self.languges.setFixedHeight(30)
        for i in ["english", "japanese", "chinese"]:
            self.languges.addItem(i)

        btn_1 = QPushButton('번역')
        btn_1.clicked.connect(self.btn_1_clicked)

        self.input_text = QTextEdit()
        self.input_text.setFixedWidth(300)
        self.input_text.setFixedHeight(50)
        self.translated_text = QTextBrowser()
        self.translated_text.setFixedWidth(300)
        self.translated_text.setFixedHeight(50)

        gbox = QGridLayout()
        gbox.addWidget(label1, 0, 0)
        gbox.addWidget(self.languges, 0, 1)
        gbox.addWidget(btn_1, 0, 2)
        gbox.addWidget(label2, 1, 0)
        gbox.addWidget(self.input_text, 1, 1)
        gbox.addWidget(label3, 2, 0)
        gbox.addWidget(self.translated_text, 2, 1)

        self.setLayout(gbox)
        self.setWindowTitle('ChatGPT Translate')
        self.setGeometry(300, 300, 480, 250)
        self.show()
    def btn_1_clicked(self):
        prompt = "please translate \"" + self.input_text.toPlainText()\
                 + "\" into " + self.languges.currentText()

        with open("secret.json", "r", encoding="utf8") as f:
            contents = f.read()
            json_data = json.loads(contents)
        openai.api_key = json_data['apikey']

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            temperature=0
        )

        self.translated_text.setText(response['choices'][0]['text'])


if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
