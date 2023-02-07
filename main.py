import sys
import requests

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 100, 700, 550)
        self.setWindowTitle('Работа с картой')

        self.sheet_scheme = QPushButton('', self)
        self.sheet_scheme.resize(30, 30)
        self.sheet_scheme.move(50, 450)
        self.sheet_scheme.setIcon(QIcon('mapicon.png'))

        self.sheet_spn = QPushButton('', self)
        self.sheet_spn.resize(30, 30)
        self.sheet_spn.move(80, 450)
        self.sheet_spn.setIcon(QIcon('spnicon.png'))

        self.sheet_hybrid = QPushButton('', self)
        self.sheet_hybrid.resize(30, 30)
        self.sheet_hybrid.move(110, 450)
        self.sheet_hybrid.setIcon(QIcon('hybridicon.png'))

        self.sheet_scheme.clicked.connect(self.scheme)
        self.sheet_spn.clicked.connect(self.spn)
        self.sheet_hybrid.clicked.connect(self.hybrid)

        self.map = QLabel(self)
        self.map.move(50, 30)
        self.map.resize(400, 400)
        pixmap = QPixmap('tmp.png')
        pixmap = pixmap.scaled(400, 400)
        self.map.setPixmap(pixmap)

        self.map_ll = [87.3, 55.7]
        self.map_l = 'map'
        self.map_zoom = 7

        self.refresh_map()

    def hybrid(self):
        self.map_l = 'sat,skl'
        self.refresh_map()

    def spn(self):
        self.map_l = 'sat'
        self.refresh_map()

    def scheme(self):
        self.map_l = 'map'
        self.refresh_map()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
           self.map_ll[1] += 4.4
        elif event.key() == Qt.Key_Right:
           self.map_ll[0] += 4.4
        elif event.key() == Qt.Key_Down:
           self.map_ll[1] -= 4.4
        elif event.key() == Qt.Key_Left:
           self.map_ll[0] -= 4.4
        self.refresh_map()

    def refresh_map(self):
        map_params = {
            "ll": ','.join(map(str, self.map_ll)),
            "l": self.map_l,
            "z": self.map_zoom
        }
        response = requests.get('https://static-maps.yandex.ru/1.x/', params=map_params)
        with open('map.png', mode='wb') as f:
            f.write(response.content)
        pixmap = QPixmap()
        pixmap.load('map.png')
        self.map.setPixmap(pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
