# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(285, 525)
        Form.setMinimumSize(QtCore.QSize(285, 525))
        Form.setMaximumSize(QtCore.QSize(285, 525))
        Form.setBaseSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("asset/awanari.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 365, 561))
        self.widget.setObjectName("widget")
        self.background = QtWidgets.QLabel(self.widget)
        self.background.setGeometry(QtCore.QRect(-4, -8, 365, 551))
        self.background.setStyleSheet("background:url(:/images/bg1.png)")
        self.background.setText("")
        self.background.setObjectName("background")
        self.suhu = QtWidgets.QLabel(self.widget)
        self.suhu.setGeometry(QtCore.QRect(30, 70, 111, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.suhu.setFont(font)
        self.suhu.setStyleSheet("color: rgb(255, 255, 255);")
        self.suhu.setObjectName("suhu")
        self.icon_suhu = QtWidgets.QLabel(self.widget)
        self.icon_suhu.setGeometry(QtCore.QRect(180, 70, 91, 101))
        self.icon_suhu.setStyleSheet("image: url(:/images/siang.png)")
        self.icon_suhu.setText("")
        self.icon_suhu.setObjectName("icon_suhu")
        self.bg_kelembapan = QtWidgets.QLabel(self.widget)
        self.bg_kelembapan.setGeometry(QtCore.QRect(10, 200, 81, 81))
        self.bg_kelembapan.setStyleSheet("border-image: url(:/images/bg1.2.png);\n"
"border-radius: 5px;\n"
"")
        self.bg_kelembapan.setText("")
        self.bg_kelembapan.setObjectName("bg_kelembapan")
        self.saran = QtWidgets.QLabel(self.widget)
        self.saran.setGeometry(QtCore.QRect(-10, 350, 301, 181))
        self.saran.setStyleSheet("border-image: url(:/images/bg0.jpg);\n"
"border-top-left-radius: 30px;\n"
"border-top-right-radius: 30px;")
        self.saran.setText("")
        self.saran.setObjectName("saran")
        self.saran_teks = QtWidgets.QLabel(self.widget)
        self.saran_teks.setGeometry(QtCore.QRect(36, 382, 201, 41))
        self.saran_teks.setStyleSheet("color: rgb(113, 149, 231)")
        self.saran_teks.setObjectName("saran_teks")
        self.kelembapan = QtWidgets.QLabel(self.widget)
        self.kelembapan.setGeometry(QtCore.QRect(20, 240, 61, 21))
        self.kelembapan.setStyleSheet("color: rgb(255, 255, 255)")
        self.kelembapan.setObjectName("kelembapan")
        self.lokasi = QtWidgets.QLabel(self.widget)
        self.lokasi.setGeometry(QtCore.QRect(20, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lokasi.setFont(font)
        self.lokasi.setStyleSheet("color: rgb(255, 255, 255)")
        self.lokasi.setObjectName("lokasi")
        self.bg_angin = QtWidgets.QLabel(self.widget)
        self.bg_angin.setGeometry(QtCore.QRect(100, 200, 81, 81))
        self.bg_angin.setStyleSheet("border-image: url(:/images/bg1.2.png);\n"
"border-radius: 5px;\n"
"")
        self.bg_angin.setText("")
        self.bg_angin.setObjectName("bg_angin")
        self.bg_indeks = QtWidgets.QLabel(self.widget)
        self.bg_indeks.setGeometry(QtCore.QRect(190, 200, 81, 81))
        self.bg_indeks.setStyleSheet("border-image: url(:/images/bg1.2.png);\n"
"border-radius: 5px;\n"
"")
        self.bg_indeks.setText("")
        self.bg_indeks.setObjectName("bg_indeks")
        self.angin = QtWidgets.QLabel(self.widget)
        self.angin.setGeometry(QtCore.QRect(110, 240, 31, 21))
        self.angin.setStyleSheet("color: rgb(255, 255, 255)")
        self.angin.setObjectName("angin")
        self.indeks = QtWidgets.QLabel(self.widget)
        self.indeks.setGeometry(QtCore.QRect(200, 240, 51, 21))
        self.indeks.setStyleSheet("color: rgb(255, 255, 255)")
        self.indeks.setObjectName("indeks")
        self.value_kelembapan = QtWidgets.QLabel(self.widget)
        self.value_kelembapan.setGeometry(QtCore.QRect(20, 260, 47, 13))
        self.value_kelembapan.setStyleSheet("color: rgb(255, 255, 255)")
        self.value_kelembapan.setObjectName("value_kelembapan")
        self.value_angin = QtWidgets.QLabel(self.widget)
        self.value_angin.setGeometry(QtCore.QRect(110, 260, 47, 13))
        self.value_angin.setStyleSheet("color: rgb(255, 255, 255)")
        self.value_angin.setObjectName("value_angin")
        self.value_indeks = QtWidgets.QLabel(self.widget)
        self.value_indeks.setGeometry(QtCore.QRect(200, 260, 47, 13))
        self.value_indeks.setStyleSheet("color: rgb(255, 255, 255)")
        self.value_indeks.setObjectName("value_indeks")
        self.icon1 = QtWidgets.QLabel(self.widget)
        self.icon1.setGeometry(QtCore.QRect(20, 210, 31, 31))
        self.icon1.setStyleSheet("image: url(:/images/kadar air.png)")
        self.icon1.setText("")
        self.icon1.setObjectName("icon1")
        self.icon2 = QtWidgets.QLabel(self.widget)
        self.icon2.setGeometry(QtCore.QRect(110, 210, 31, 31))
        self.icon2.setStyleSheet("image: url(:/images/angin.png)")
        self.icon2.setText("")
        self.icon2.setObjectName("icon2")
        self.icon3 = QtWidgets.QLabel(self.widget)
        self.icon3.setGeometry(QtCore.QRect(230, 210, 41, 31))
        self.icon3.setStyleSheet("image: url(:/images/uv.png)")
        self.icon3.setText("")
        self.icon3.setObjectName("icon3")
        self.search = QtWidgets.QLabel(self.widget)
        self.search.setGeometry(QtCore.QRect(240, 30, 31, 21))
        self.search.setStyleSheet("image:url(:/images/search white.png)")
        self.search.setText("")
        self.search.setObjectName("search")
        self.date = QtWidgets.QLabel(self.widget)
        self.date.setGeometry(QtCore.QRect(20, 30, 121, 31))
        self.date.setStyleSheet("color: rgb(255, 255, 255)")
        self.date.setObjectName("date")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Awanari"))
        self.suhu.setText(_translate("Form", "21°C"))
        self.saran_teks.setText(_translate("Form", "                   SARAN #7195E7"))
        self.kelembapan.setText(_translate("Form", "Kelembapan"))
        self.lokasi.setText(_translate("Form", "Graha Indah"))
        self.angin.setText(_translate("Form", "Angin"))
        self.indeks.setText(_translate("Form", "Indeks UV"))
        self.value_kelembapan.setText(_translate("Form", "87%"))
        self.value_angin.setText(_translate("Form", "3 km/jam"))
        self.value_indeks.setText(_translate("Form", "6 dari 11"))
        self.date.setText(_translate("Form", "Tue, 21 November 2023"))
import main_rc
if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self = Ui_Form()
        self.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())