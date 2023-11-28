import main_rc
import requests
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QPoint, QSequentialAnimationGroup
from bs4 import BeautifulSoup as bs
import requests
from win10toast import ToastNotifier
import time
lokasitempat = "KalimantanTimur"
url = f"https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-{lokasitempat}.xml"
response = requests.get(url, verify=False)
r = response.text
now = datetime.datetime.now()
harini = now.strftime("%A, %B %Y")
current_time = datetime.datetime.now().time()
prakiraan = {'Pagi': '', 'Siang': '', 'Malam': ''}
kode = {
    '0': 'Cerah ',
    '1': 'Cerah Berawan ',
    '2': 'Cerah Berawan ',
    '3': 'Berawan ',
    '4': 'Berawan Tebal ',
    '5': 'Udara Kabur ',
    '10': 'Asap ',
    '45': 'Kabut ',
    '60': 'Hujan Ringan ',
    '61': 'Hujan Sedang ',
    '63': 'Hujan Lebat ',
    '80': 'Hujan Lokal ',
    '95': 'Hujan Petir ',
    '97': 'Hujan Petir '
}
pagi = datetime.time(6, 0, 0)
siang = datetime.time(12, 0, 0)
sore = datetime.time(18, 0, 0)
malam = datetime.time(21, 0, 0)


def cekbg():
    if pagi:
        return "border-image: url(:/images/bg1.png)"
    if siang:
        return "background:url(:/images/bg1.png)"
    if malam:
        return "background:url(:/images/bg3.png)"





def cekbgicon():
    if pagi:
        return "background:url(:/images/bg2.png);border-radius: 5px;"
    if siang:
        return "background:url(:/images/bg2.png);border-radius: 5px;"
    if malam:
        return "background:url(:/images/bg3.2.png);border-radius: 5px;"


def ipInfo(addr=''):
    from urllib.request import urlopen
    from json import load
    if addr == '':
        url = 'https://ipinfo.io/json'
    else:
        url = 'https://ipinfo.io/' + addr + '/json'
    res = urlopen(url)
    # response from url(if res==None then check connection)
    data = load(res)
    # will load the json response into data
    city = data['city']
    return city

#variable 
bg = cekbg()
bgicon = cekbgicon()
LokasiID = ipInfo()


class cuaca_text():
    global h0,h6,h12,th0,th6,th12,ws0,ws6,ws12
    LokasiTerkini = bs(r, "xml")
    try:
        KotaCuaca = LokasiTerkini.find(description={LokasiID}).find(id="weather")
        h0 = KotaCuaca.find(h='0').value.string
        h6 = KotaCuaca.find(h='6').value.string
        h12 = KotaCuaca.find(h='12').value.string

        prakiraan['Pagi'] = kode[h0]
        prakiraan['Siang'] = kode[h6]
        prakiraan['Malam'] = kode[h12]

    except:
        print("Data Tidak Ditemukan (Kota tidak tersedia)")
        quit()
    try:
        Kondisit = LokasiTerkini.find(description={LokasiID}).find(id="t")

        th0 = Kondisit.find(h='0').value.string
        th6 = Kondisit.find(h='6').value.string
        th12 = Kondisit.find(h='12').value.string
    except:
        print("Data Tidak Ditemukan (Suhu tidak tersedia)")
    try:
        Kondisit = LokasiTerkini.find(description={LokasiID}).find(id="ws")

        ws0 = Kondisit.find(h='0').value.string
        ws6 = Kondisit.find(h='6').value.string
        ws12 = Kondisit.find(h='12').value.string
    except:
        print("Data Tidak Ditemukan (Kecepatan Angin tidak tersedia)")
    try:
        Kondisit = LokasiTerkini.find(description={LokasiID}).find(id="hu")
        global hu
        hu = Kondisit.value.string
        def ceksuhu():
            # Compare the current time with the defined ranges
            if current_time >= pagi and current_time < siang:
                return th0
            elif current_time >= siang and current_time < sore:
                return th6
            elif current_time >= sore and current_time < malam:
                return th12
            else:
                return th12
       
    except:
        print("Data Tidak Ditemukan ")
    try:
        def cekcuaca():
            # Compare the current time with the defined ranges
            if current_time >= pagi and current_time < siang:
                return h0
            elif current_time >= siang and current_time < sore:
                return h6
            elif current_time >= sore and current_time < malam:
                return h12
            else:
                return h12

        
    except:
        print("Data Tidak Ditemukan")
    global pengecekancuaca,weather_kondisi
    pengecekancuaca = int(cekcuaca())

    try:
        
        def get_weather_saran():
            if pengecekancuaca == 0:
                return "Saat ini Sangat Cerah! Sebaiknya Gunakan Sunscreen"
            elif pengecekancuaca == 1 or pengecekancuaca == 2:
                return "Sekarang adalah Waktu Yang Cocok Untuk Beraktivitas di Luar Ruangan"
            elif pengecekancuaca == 3 or pengecekancuaca == 4 or pengecekancuaca == 5:
                return "Waspada Datangnya Hujan! Sebaiknya Sediakanlah Payung"
            elif pengecekancuaca == 10:
                return "Saat ini Penuh Asap! Pakailah Masker"
            elif pengecekancuaca == 45:
                return "Saat ini di Penuhi Dengan Kabut! Hati-hatilah Saat Berkendara"
            elif pengecekancuaca == 60:
                return "Sekarang Sedang Hujan Ringan, Sebaiknya Gunakanlah Jas Hujan Atau Payung"
            elif pengecekancuaca == 61:
                return "Saat ini Sedang Hujan Sedang, Gunakanlah Payung Atau Jas Hujan Saat Berpergian"
            elif pengecekancuaca == 63:
                return "Sekarang Sedang Hujan Lebat! Sebaiknya Keluar Rumah Pada Saat Hujan Berhenti, Jika Sedang Berada di Luar maka Menepilah!"
            elif pengecekancuaca == 80:
                return "Saat Ini Sedang Hujan, Pakailah Payung Atau Jas Hujan"
            elif pengecekancuaca == 95 or pengecekancuaca == 97:
                return "Hati Hati Sekarang Sedang Terjadi Hujan Petir, Tetaplah di Dalam Rumah! Jika Berada di Luar Maka Segeralah Ke Dalam Ruangan"
        get_weather_saran
    
    except:
        print("Data Tidak Ditemukan")
    try:
        def cekwaktu():
            if current_time >= pagi and current_time < siang:
                
                if pengecekancuaca == 0:
                    return "image: url(:/images/siang.png)"
                if pengecekancuaca == 1 or pengecekancuaca == 2:
                    return "image: url(:/images/siang-berawan.png)"
                if pengecekancuaca == 3 or pengecekancuaca == 4:
                    return "image: url(:/images/berawan.png)"
                if pengecekancuaca == 5 or pengecekancuaca == 10 or pengecekancuaca == 45:
                    return "image: url(:/images/mendung.png)"
                if pengecekancuaca == 60 or pengecekancuaca == 61 or pengecekancuaca == 63:
                    return "image: url(:/images/siang-hujan.png)"
                if pengecekancuaca == 60 or pengecekancuaca == 61 or pengecekancuaca == 63:
                    return "image: url(:/images/siang-hujan.png)"
                if pengecekancuaca == 80 or pengecekancuaca == 95 or pengecekancuaca == 70:
                    return "image: url(:/images/siang-hujan.png)"
            elif current_time >= siang and current_time < sore:
                if pengecekancuaca == 0:
                    return "image: url(:/images/siang.png)"
                if pengecekancuaca == 1 or pengecekancuaca == 2:
                    return "image: url(:/images/siang-berawan.png)"
                if pengecekancuaca == 3 or pengecekancuaca == 4:
                    return "image: url(:/images/berawan.png)"
                if pengecekancuaca == 5 or pengecekancuaca == 10 or pengecekancuaca == 45:
                    return "image: url(:/images/mendung.png)"
                if pengecekancuaca == 60 or pengecekancuaca == 61 or pengecekancuaca == 63:
                    return "image: url(:/images/siang-hujan.png)"
                if pengecekancuaca == 60 or pengecekancuaca == 61 or pengecekancuaca == 63:
                    return "image: url(:/images/siang-hujan.png)"
                if pengecekancuaca == 80 or pengecekancuaca == 95 or pengecekancuaca == 70:
                    return "image: url(:/images/siang-hujan.png)"
            elif current_time >= sore and current_time < malam:
                if pengecekancuaca == 0:
                    return "image: url(:/images/siang.png)"
                if pengecekancuaca == 1 or pengecekancuaca == 2:
                    return "image: url(:/images/siang-berawan.png)"
                if pengecekancuaca == 3 or pengecekancuaca == 4:
                    return "image: url(:/images/berawan.png)"
                if pengecekancuaca == 5 or pengecekancuaca == 10 or pengecekancuaca == 45:
                    return "image: url(:/images/mendung.png)"
                if pengecekancuaca == 60 or pengecekancuaca == 61 or pengecekancuaca == 63:
                    return "image: url(:/images/siang-hujan.png)"
                if pengecekancuaca == 60 or pengecekancuaca == 61 or pengecekancuaca == 63:
                    return "image: url(:/images/siang-hujan.png)"
                if pengecekancuaca == 80 or pengecekancuaca == 95 or pengecekancuaca == 70:
                    return "image: url(:/images/siang-hujan.png)"
            else:
                if pengecekancuaca == 0:
                    return "image: url(:/images/siang.png)"
                if pengecekancuaca == 1 or pengecekancuaca == 2:
                    return "image: url(:/images/siang-berawan.png)"
                if pengecekancuaca == 3 or pengecekancuaca == 4:
                    return "image: url(:/images/berawan.png)"
                if pengecekancuaca == 5 or pengecekancuaca == 10 or pengecekancuaca == 45:
                    return "image: url(:/images/mendung.png)"
                if pengecekancuaca == 60 or pengecekancuaca == 61 or pengecekancuaca == 63:
                    return "image: url(:/images/siang-hujan.png)"
                if pengecekancuaca == 60 or pengecekancuaca == 61 or pengecekancuaca == 63:
                    return "image: url(:/images/siang-hujan.png)"
                if pengecekancuaca == 80 or pengecekancuaca == 95 or pengecekancuaca == 70:
                    return "image: url(:/images/siang-hujan.png)"
                
        

    except:
        print("Data Tidak Ditemukan") 
    
    print(
        "AWANARA\n",
        "--- Hari ini ---\n",
        f"Lokasi : {LokasiID}\n"
        "----------------"
        "\nPagi  : ",
        prakiraan['Pagi'],
        f"\nSuhu : {th0} ",
        f"\nKecepatan Angin : {ws0} ",
        "\nSiang : ",
        prakiraan['Siang'],
        f"\nSuhu : {th6} ",
        f"\nKecepatan Angin : {ws6} ",
        "\nMalam : ",
        prakiraan['Malam'],
        f"\nSuhu : {th12} "
        f"\nKecepatan Angin : {ws12} ",
    )





def pengulangan():
    while datetime.datetime.now().minute % 5 != 0:
        time.sleep(1)
    cekcuaca()
    while True:
        time.sleep(300)
        cekcuaca()
def check_bad_weather():
        def send_notification(message):
            toaster = ToastNotifier()
            toaster.show_toast(message, duration=10,threaded=True)
        if pengecekancuaca >= 60:
            send_notification(f"Cuaca sedang hujan di luar")
        else:
            pass
class Ui_Form(object):
    def setupUi(self, Form):
    
        Form.setObjectName("Form")
        Form.resize(285, 525)
        Form.setFixedSize(QtCore.QSize(285, 525))
        Form.setWindowIcon(QtGui.QIcon('awanari.png'))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 365, 561))
        self.widget.setObjectName("widget")
        self.background = QtWidgets.QLabel(self.widget)
        self.background.setGeometry(QtCore.QRect(-4, -8, 365, 551))
        self.background.setStyleSheet(f"{bg}")
        self.background.setScaledContents(True)
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
        self.icon_suhu.setStyleSheet(cuaca_text.cekwaktu())
        self.icon_suhu.setText("")
        self.icon_suhu.setObjectName("icon_suhu")
        self.bg_kelembapan = QtWidgets.QLabel(self.widget)
        self.bg_kelembapan.setGeometry(QtCore.QRect(10, 200, 81, 81))
        self.bg_kelembapan.setStyleSheet(
            f"{bgicon};\n"
            "border-radius: 5px;\n"
            "")
        self.bg_kelembapan.setText("")
        self.bg_kelembapan.setObjectName("bg_kelembapan")
        self.saran = QtWidgets.QLabel(self.widget)
        self.saran.setGeometry(QtCore.QRect(-10, 350, 301, 181))
        self.saran.setStyleSheet(f"{bgicon};"
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
        self.bg_angin.setStyleSheet(f"{bgicon};\n"
                                    "border-radius: 5px;\n"
                                    "")
        self.bg_angin.setText("")
        self.bg_angin.setObjectName("bg_angin")
        self.bg_indeks = QtWidgets.QLabel(self.widget)
        self.bg_indeks.setGeometry(QtCore.QRect(190, 200, 81, 81))
        self.bg_indeks.setStyleSheet(f"{bgicon};\n"
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
        self.icon1.setStyleSheet("image: url(:/images/kadar-air.png)")
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
        self.suhu.setText(_translate("Form", f"{cuaca_text.ceksuhu()}℃"))
        self.saran_teks.setText(_translate("Form", f"{cuaca_text.get_weather_saran()}"))
        self.saran_teks.setStyleSheet('color:white;font-weight: bold;')
        self.saran_teks.setWordWrap(True)
        self.saran_teks.setMinimumHeight(100)
        self.saran_teks.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)
        self.kelembapan.setText(_translate("Form", "Kelembapan"))
        self.kelembapan.setStyleSheet('font-weight: bold;color:white;font: 8pt Comic Sans MS;')
        self.kelembapan.setMinimumWidth(100)
        self.lokasi.setText(_translate("Form", LokasiID))
        self.lokasi.setStyleSheet('font-weight: bold;color:white')
        self.angin.setText(_translate("Form", "Angin"))
        self.angin.setStyleSheet('font-weight:bold;color:white;font: 12pt Comic Sans MS;')
        self.angin.setMinimumWidth(100)
        self.indeks.setText(_translate("Form", "Indeks UV"))
        self.indeks.setStyleSheet('font-weight:bold;color:white;font: 12pt Comic Sans MS;')
        self.value_kelembapan.setText(_translate("Form", f"{hu}%"))
        self.value_angin.setText(_translate("Form", f"{ws0}Knt"))
        self.value_indeks.setText(_translate("Form", "6 dari 11"))
        self.date.setText(_translate("Form", f"{harini}"))

    def animate_widget(duration):
        # Create the animation for moving to the target position
        animation_forward = QPropertyAnimation(self.icon_suhu, b"pos")
        animation_forward.setDuration(1600)
        animation_forward.setStartValue(QPoint(180, 100))
        animation_forward.setEndValue(QPoint(180, 80))


        # Create the animation for moving back to the start position
        animation_backward =  QPropertyAnimation(self.icon_suhu, b"pos")
        animation_backward.setDuration(1600)
        animation_backward.setStartValue(QPoint(180, 80))
        animation_backward.setEndValue(QPoint(180, 100))


        # Create a sequential animation group
        animation_group =  QSequentialAnimationGroup(self.icon_suhu)
        animation_group.addAnimation(animation_forward)
        animation_group.addAnimation(animation_backward)
       
        # Start the animation
        animation_group.setLoopCount(-1)
        animation_group.start()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    self = Ui_Form()
    self.setupUi(MainWindow)
    self.animate_widget()
    check_bad_weather()
    MainWindow.show()
    sys.exit(app.exec_())
