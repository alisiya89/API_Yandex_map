import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 100, 700, 550)
        self.setWindowTitle('Работа с картой')

        self.map = QLabel(self)
        self.map.move(50, 30)
        self.map.resize(400, 400)
        pixmap = QPixmap('tmp.png')
        pixmap = pixmap.scaled(400, 400)
        self.map.setPixmap(pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
