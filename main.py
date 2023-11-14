from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Awanara")
        layout = QGridLayout()
        self.setStyleSheet('background-color: #202A44')
        self.setFixedSize(640, 480)
        layout.addWidget(QLabel("Pagi"),0,0)
        layout.addWidget(QLabel("Malam"),0,1,1,3)
        layout.addWidget(QLabel("Info"),1,0,1,4)
        layout.addWidget(QLabel("Celcius"),2,0,1,4)
        layout.addWidget(QLabel("Pesan"),2,0,1,4)
        self.setLayout(layout)
        for label in self.findChildren(QLabel):
            label.setStyleSheet('background: #1640D6;color: white;padding:50px;border-radius:15px;font-weight:bold;font-size:22px;')
        
app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())