import sys
import requests, json, urllib.request
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QComboBox, QMainWindow, QWidget, QPushButton, QGridLayout
from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(230, 400))

        self.setWindowTitle('pogodynka')

        layout = QGridLayout()

        self.choose = QComboBox()

        url = "https://danepubliczne.imgw.pl/api/data/synop/id/"
        arr = []
        myId = ['12295', '12600', '12235', '12550', '12160']
        for myCity in myId:
            cos = urllib.request.urlopen(url+myCity)
            data = json.loads(cos.read())
            arr.append(data)

            self.choose.addItem(data["stacja"])
            self.choose.currentIndexChanged.connect(self.indexChanged)

        json_str = json.dumps(arr[0])
        json_object = json.loads(json_str)

        self.station = QLabel()
        pixmap = QPixmap('./station.png')
        self.station.setPixmap(pixmap)
        self.labelStation = QLabel(json_object["stacja"])

        self.temperature = QLabel()
        pixmap1 = QPixmap('./temp.png')
        self.temperature.setPixmap(pixmap1)
        self.labelTemperature = QLabel(json_object['temperatura'] + ' °C')

        self.windSpeed = QLabel()
        pixmap2 = QPixmap('./cos.png')
        self.windSpeed.setPixmap(pixmap2)
        self.labelWindSpeed = QLabel(json_object['predkosc_wiatru'] + ' km/h')

        self.windDirection = QLabel()
        pixmap3 = QPixmap('./direction.png')
        self.windDirection.setPixmap(pixmap3)
        self.labelWindDirection = QLabel(json_object['kierunek_wiatru'] + ' °')

        self.relativeHumidity = QLabel()
        pixmap4 = QPixmap('./humidity.png')
        self.relativeHumidity.setPixmap(pixmap4)
        self.labelRelativeHumidity = QLabel(json_object['wilgotnosc_wzgledna'] + ' %')

        self.pressure = QLabel()
        pixmap5 = QPixmap('./pressure.png')
        self.pressure.setPixmap(pixmap5)
        self.labelPressure = QLabel(json_object['cisnienie'] + ' hPa')



        # G R I D
        layout.addWidget(self.choose, 0, 0, 1, 4)

        layout.addWidget(self.station, 1, 0)
        layout.addWidget(self.labelStation, 1, 1)

        layout.addWidget(self.temperature, 2, 0)
        layout.addWidget(self.labelTemperature, 2, 1)

        layout.addWidget(self.windSpeed, 3, 0)
        layout.addWidget(self.labelWindSpeed, 3, 1)

        layout.addWidget(self.windDirection, 4, 0)
        layout.addWidget(self.labelWindDirection, 4, 1)

        layout.addWidget(self.relativeHumidity, 5, 0)
        layout.addWidget(self.labelRelativeHumidity, 5, 1)

        layout.addWidget(self.pressure, 6, 0)
        layout.addWidget(self.labelPressure, 6, 1)


        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def indexChanged(self, i):
        url = "https://danepubliczne.imgw.pl/api/data/synop/id/"
        arr = []
        myId = ['12295', '12600', '12235', '12550', '12160']
        for myCity in myId:
            cos = urllib.request.urlopen(url + myCity)
            data = json.loads(cos.read())
            arr.append(data)
        if i == 0:
            json_str = json.dumps(arr[i])
            json_object = json.loads(json_str)
            self.labelStation.setText(json_object['stacja'])
            self.labelTemperature.setText(json_object['temperatura'] + ' °C')
            self.labelWindSpeed.setText(json_object['predkosc_wiatru'] + ' km/h')
            self.labelWindDirection.setText(json_object['kierunek_wiatru'] + ' °')
            self.labelRelativeHumidity.setText(json_object['wilgotnosc_wzgledna'] + ' %')
            self.labelPressure.setText(json_object['cisnienie'] + ' hPa')
        elif i == 1:
            json_str = json.dumps(arr[i])
            json_object = json.loads(json_str)
            self.labelStation.setText(json_object['stacja'])
            self.labelTemperature.setText(json_object['temperatura'] + ' °C')
            self.labelWindSpeed.setText(json_object['predkosc_wiatru'] + ' km/h')
            self.labelWindDirection.setText(json_object['kierunek_wiatru'] + ' °')
            self.labelRelativeHumidity.setText(json_object['wilgotnosc_wzgledna'] + ' %')
            self.labelPressure.setText(json_object['cisnienie'] + ' hPa')
        elif i == 2:
            json_str = json.dumps(arr[i])
            json_object = json.loads(json_str)
            self.labelStation.setText(json_object['stacja'])
            self.labelTemperature.setText(json_object['temperatura'] + ' °C')
            self.labelWindSpeed.setText(json_object['predkosc_wiatru'] + ' km/h')
            self.labelWindDirection.setText(json_object['kierunek_wiatru'] + ' °')
            self.labelRelativeHumidity.setText(json_object['wilgotnosc_wzgledna'] + ' %')
            self.labelPressure.setText(json_object['cisnienie'] + ' hPa')
        elif i == 3:
            json_str = json.dumps(arr[i])
            json_object = json.loads(json_str)
            self.labelStation.setText(json_object['stacja'])
            self.labelTemperature.setText(json_object['temperatura'] + ' °C')
            self.labelWindSpeed.setText(json_object['predkosc_wiatru'] + ' km/h')
            self.labelWindDirection.setText(json_object['kierunek_wiatru'] + ' °')
            self.labelRelativeHumidity.setText(json_object['wilgotnosc_wzgledna'] + ' %')
            self.labelPressure.setText(json_object['cisnienie'] + ' hPa')
        elif i == 4:
            json_str = json.dumps(arr[i])
            json_object = json.loads(json_str)
            self.labelStation.setText(json_object['stacja'])
            self.labelTemperature.setText(json_object['temperatura'] + ' °C')
            self.labelWindSpeed.setText(json_object['predkosc_wiatru'] + ' km/h')
            self.labelWindDirection.setText(json_object['kierunek_wiatru'] + ' °')
            self.labelRelativeHumidity.setText(json_object['wilgotnosc_wzgledna'] + ' %')
            self.labelPressure.setText(json_object['cisnienie'] + ' hPa')


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()