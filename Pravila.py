from PyQt5.QtGui import QPixmap
import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('look.ui',self)
        self.pushButton.clicked.connect(self.image1)
        self.pushButton_2.clicked.connect(self.image2)
        self.pushButton_3.clicked.connect(self.image3)
        self.pushButton_4.clicked.connect(self.image4)
        self.pushButton_5.clicked.connect(self.image5)
        self.pushButton_6.clicked.connect(self.image6)
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.label_7.hide()
        self.label_8.hide()
        self.label_9.hide()
        self.label_10.hide()
        self.label_11.hide()
        self.label_12.hide()

    def image1(self):
        with open('avtomobil.txt', 'r', encoding='utf-8') as f:
            znak1 = f.read().splitlines()
        stopzn = znak1[0]
        self.label.setText(stopzn)
        self.label.show()
        self.label_7.setPixmap(QPixmap("stop.jpg"))
        self.label_7.show()
        self.label.setStyleSheet("font-size:13px;color:white")
    def image2(self):
        with open('avtomobil.txt', 'r', encoding='utf-8') as f:
            znak1 = f.read().splitlines()
        dituzn = znak1[1]
        self.label_2.setText(dituzn)
        self.label_2.show()
        self.label_8.setPixmap(QPixmap("Ditu.png"))
        self.label_8.show()
        self.label_2.setStyleSheet("font-size:13px;color:white")
    def image3(self):
        with open('avtomobil.txt', 'r', encoding='utf-8') as f:
            znak1 = f.read().splitlines()
        pishohidzn = znak1[2]
        self.label_3.setText(pishohidzn)
        self.label_3.show()
        self.label_9.setPixmap(QPixmap("pisho.png"))
        self.label_9.show()
        self.label_3.setStyleSheet("font-size:13px;color:white")
    def image4(self):
        with open('avtomobil.txt', 'r', encoding='utf-8') as f:
            znak1 = f.read().splitlines()
        pidzemzn = znak1[3]
        self.label_4.setText(pidzemzn)
        self.label_4.show()
        self.label_10.setPixmap(QPixmap("pidzem.png"))
        self.label_10.show()
        self.label_4.setStyleSheet("font-size:13px;color:white")
    def image5(self):
        with open('avtomobil.txt', 'r', encoding='utf-8') as f:
            znak1 = f.read().splitlines()
        ruhzn = znak1[4]
        self.label_5.setText(ruhzn)
        self.label_5.show()
        self.label_11.setPixmap(QPixmap("ruh.png"))
        self.label_11.show()
        self.label_5.setStyleSheet("font-size:13px;color:white")
    def image6(self):
        with open('avtomobil.txt', 'r', encoding='utf-8') as f:
            znak1 = f.read().splitlines()
        vizn = znak1[5]
        self.label_6.setText(vizn)
        self.label_6.show()
        self.label_12.setPixmap(QPixmap("Viydz.png"))
        self.label_12.show()
        self.label_6.setStyleSheet("font-size:13px;color:white")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
