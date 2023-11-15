from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Awanara")
        container = QFrame()
        layout = QGridLayout(container)
        pagelayout = QHBoxLayout(container)
        sidelayout = QVBoxLayout(container)
        self.setStyleSheet('background-color: #202A44')
        self.setBaseSize(900, 480)
        container.setStyleSheet('background-color: white')
        button1 = QPushButton("Home")
        button2 = QPushButton("List")
        button3 = QPushButton("About")
        judul = QLabel("AWANARA")
        label1 = QLabel("Test")
        label2 = QLabel("Test2")
        button1.setMaximumSize(1000,1000)
        button2.setMaximumSize(1000,1000)
        button3.setMaximumSize(1000,1000)
        sidelayout.addWidget(judul)
        sidelayout.addWidget(button1)
        sidelayout.addWidget(button2)
        sidelayout.addWidget(button3)
        pagelayout.addWidget(label1)
        pagelayout.addWidget(label2)
        layout.addLayout(sidelayout,0,0)
        layout.addLayout(pagelayout,0,1,1,9)
        self.setLayout(layout)
        for label in self.findChildren(QLabel):
            label.setStyleSheet('color: black;padding:30px;border-radius:15px;font-weight:bold;font-size:35px;color:white;')
        for button in self.findChildren(QPushButton):
            button.setStyleSheet('background: #83A2FF;color: white;padding:10px;margin:10px;height:auto;border-radius:13px;font-weight:bold;font-size:30px;')
            button.setMinimumHeight(80)
        
app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())