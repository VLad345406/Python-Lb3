import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Title'
        self.left = 50
        self.top = 100
        self.width = 800
        self.height = 600
        self.initUI()
        button1 = QPushButton("Button1")
        self.setCentralWidget(button1)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


#if __name__ == '__main__':
 #   app = QApplication(sys.argv)
  #  ex = App()
   # sys.exit(app.exec_())

app = QApplication(sys.argv)

window = App()
window.show()

app.exec()
