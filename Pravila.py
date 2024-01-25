from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, \
    QHBoxLayout, QApplication, QListWidget

app = QApplication([])

editor_window = QWidget()
editor_window.setWindowTitle("Правила Дорожнього руху")
editor_window.resize(900, 600)

editor_window.show()
app.exec_()