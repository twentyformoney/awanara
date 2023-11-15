import requests
from bs4 import BeautifulSoup as bs
lokasitempat = "KalimantanTimur"
LokasiID = 501349
url = f"https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-{lokasitempat}.xml"
response = requests.get(url,verify=False)
r = response.text

prakiraan = {'Pagi': '' , 'Siang': '', 'Malam': ''}
kode = {
'0': 'Cerah / Clear Skies',
'1': 'Cerah Berawan / Party Cloudy',
'2': 'Cerah Berawan / Partly Cloudy',
'3': 'Berawan / Mostly Cloudy',
'4': 'Berawan Tebal / Overcast',
'5': 'Udara Kabur / Haze',
'10': 'Asap / Smoke',
'45': 'Kabut / Fog',
'60': 'Hujan Ringan / Light Rain',
'61': 'Hujan Sedang / Rain',
'63': 'Hujan Lebat / Heavy Rain',
'80': 'Hujan Lokal / Isolated Shower',
'95': 'Hujan Petir / Severe Thunderstorm',
'97': 'Hujan Petir / Severe Thunderstorm'
}

LokasiTerkini = bs(r,"xml")

# Jakarta Pusat
try:
    KotaCuaca = LokasiTerkini.find(id={LokasiID}).find(id="weather")

    h0 = KotaCuaca.find(h='0').value.string
    h6 = KotaCuaca.find(h='6').value.string
    h12 = KotaCuaca.find(h='12').value.string

    prakiraan['Pagi'] = kode[h0]
    prakiraan['Siang'] = kode[h6]
    prakiraan['Malam'] = kode[h12]
except:
    print("Data Tidak Ditemukan (Kota tidak tersedia)")
    quit()

print(
    "AWANARA\n",
	"--- Hari ini ---",
	"\nPagi  : ",
	prakiraan['Pagi'],
	"\nSiang : ",
    
	prakiraan['Siang'],
	"\nMalam : ",
	prakiraan['Malam'],
	)