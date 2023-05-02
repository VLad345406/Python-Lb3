import classes

import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.title = 'Title'
        self.left = 50
        self.top = 100
        self.width = 800
        self.height = 600

        department1 = classes.Department("Department1", 10000, 1500, 10)

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText(department1.name)
        self.label1.move(100, 100)
        self.label1.adjustSize()

        self.button1 = QPushButton(self)
        self.button1.move(100, 150)
        self.button1.setText("Button1")
        self.button1.clicked.connect(self.button1_click)

        self.initUI()

    def button1_click(self):
        # print("click!")
        #self.label1.setText("Text changed")
        #self.label1.adjustSize()
        mark = classes.Marketing
        mark.name = "first"
        classes.defMessageBox(mark.name)


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()




# if __name__ == '__main__':
#   app = QApplication(sys.argv)
#  ex = App()
# sys.exit(app.exec_())

app = QApplication(sys.argv)

window = App()
# window = QMainWindow()

window.setWindowTitle("Title")
window.setGeometry(100, 100, 500, 500)

window.show()

sys.exit(app.exec())
