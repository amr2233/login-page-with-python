from PyQt5.Qt import *
import urllib
import sys

class firstApp(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        layout = QFormLayout()

        label = QLabel("username :")
        label2 = QLabel("password : ")
        self.textbox = QLineEdit()
        self.textbox2 = QLineEdit()
        self.btn = QPushButton("login")

        layout.addWidget(label)
        layout.addWidget(self.textbox)
        layout.addWidget(label2)
        layout.addWidget(self.textbox2)
        layout.addWidget(self.btn)

        self.setLayout(layout)
        self.setWindowTitle("login page")
        self.setFocus()

        self.textbox.setPlaceholderText("type username")
        self.textbox2.setPlaceholderText("type password")



app = QApplication(sys.argv)
dialog = firstApp()
dialog.show()
app.exec_()
