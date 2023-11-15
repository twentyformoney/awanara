from PyQt6.QtWidgets import * 
from PyQt6.QtGui import *
from PyQt6.QtSvg import *
from PyQt6.QtCore import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Awanari")
        layout = QGridLayout()
        pagelayout = QHBoxLayout()
        sidelayout = QVBoxLayout()
        self.setStyleSheet('background-color: #52CEBA')
        self.setMinimumSize(800,550)
        button1 = QPushButton("")
        button2 = QPushButton("")
        button3 = QPushButton("")
        label1 = QLabel("Test")
        label2 = QLabel("Test2")
        label3 = QLabel("Test3")
        button1.setMaximumSize(1000,1000)
        button1.setIcon(QIcon('./asset/svg/home.svg'))
        button2.setIcon(QIcon('./asset/svg/search.svg'))
        
        button2.setMaximumSize(1000,1000)
        button3.setMaximumSize(1000,1000)
        sidelayout.addWidget(button1)
        sidelayout.addWidget(button2)
        sidelayout.addWidget(button3)
        pagelayout.addWidget(label1)
        pagelayout.addWidget(label2)
        pagelayout.addWidget(label3)
        layout.addLayout(sidelayout,0,0,0,0)
        layout.addLayout(pagelayout,0,1,1,3)
        self.setLayout(layout)
        for label in self.findChildren(QLabel):
            label.setStyleSheet('color: black;padding:30px;border-radius:15px;font-weight:bold;font-size:35px;color:white;')
        for button in self.findChildren(QPushButton):
            button.setStyleSheet('''
                                 .QPushButton{
                                 background: white;
                                 color: white;
                                 margin:5px;
                                 height:auto;
                                 border-radius:13px;
                                 font-weight:bold;
                                 font-size:20px;
                                 }
                                 .QPushButton:hover{
                                 background: #FFA33C;
                    
                                 }
                                 ''')
            
            button.setMinimumHeight(120)
            button.setMinimumWidth(30)
            button.setMaximumHeight(240)
            button.setMaximumWidth(90)
            button.setIconSize(QSize(50,50))
app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec())