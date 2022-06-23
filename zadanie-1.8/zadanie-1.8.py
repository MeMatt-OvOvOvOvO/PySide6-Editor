import sys
from random import random

from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget, QToolBar, QStatusBar, QGridLayout, QLabel, QTextEdit, QFileDialog
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence, Qt, QColor, QFont

fontSize = [10, 11, 12, 13, 14, 18, 24, 36]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(450, 450))
        self.setWindowTitle('Zadanie 1.8')
        self.file = None
        layout = QGridLayout()
        self.textEdit = QTextEdit()
        self.label1 = QLabel('Twoj tekst')
        self.label = QLabel('')


        #pasek stanu
        self.setStatusBar(QStatusBar(self))

        # menu
        menu = self.menuBar()

        # Plik
        nomyPlik = QAction('&nowy plik', self)
        nomyPlik.setStatusTip('nowy plik')
        nomyPlik.triggered.connect(self.nowy)
        #nomyPlik.setCheckable(True)
        nomyPlik.setShortcut(QKeySequence('Ctrl+n'))

        zapiszPlik = QAction('&zapisz plik', self)
        zapiszPlik.setStatusTip('zapisz plik')
        zapiszPlik.triggered.connect(self.zapiszPlik)
        zapiszPlik.setShortcut(QKeySequence('Ctrl+s'))

        otworzPlik = QAction('&otworz plik', self)
        otworzPlik.setStatusTip('otworz plik')
        otworzPlik.triggered.connect(self.otworzPlik)
        otworzPlik.setShortcut(QKeySequence('Ctrl+q'))
        #################
        plikMenu = menu.addMenu('Plik')

        plikMenu.addAction(nomyPlik)
        plikMenu.addSeparator()

        plikMenu.addAction(zapiszPlik)
        plikMenu.addSeparator()

        plikMenu.addAction(otworzPlik)
        plikMenu.addSeparator()

        # Formatowanie
        pogrForm = QAction('&pogrubienie tekstu', self)
        pogrForm.setStatusTip('zaznacz tekst aby go pogrubic')
        pogrForm.triggered.connect(self.pogrub)
        pogrForm.setShortcut(QKeySequence('Ctrl+b'))

        pochForm = QAction('&pochylenie tekstu', self)
        pochForm.setStatusTip('zaznacz tekst aby go pochylic')
        pochForm.triggered.connect(self.pochyl)
        pochForm.setShortcut(QKeySequence('Ctrl+g'))

        podkForm = QAction('&podkreslenie tekstu', self)
        podkForm.setStatusTip('zaznacz tekst aby go podkreslic')
        podkForm.triggered.connect(self.podkreslenie)
        podkForm.setShortcut(QKeySequence('Ctrl+t'))
        ###################
        formMenu = menu.addMenu('Formatowanie')

        formMenu.addAction(pogrForm)
        formMenu.addSeparator()

        formMenu.addAction(pochForm)
        formMenu.addSeparator()

        formMenu.addAction(podkForm)
        formMenu.addSeparator()

        # Wyrownywanie
        lewoWyr = QAction('&wyrownaj do lewej', self)
        lewoWyr.setStatusTip('zaznacz linijki aby wyrownac do lewej')
        lewoWyr.triggered.connect(self.doLewej)
        lewoWyr.setShortcut(QKeySequence('Ctrl+l'))

        prawoWyr = QAction('&wyrownaj do prawej', self)
        prawoWyr.setStatusTip('zaznacz linijki aby wyrownac do prawej')
        prawoWyr.triggered.connect(self.doPrawej)
        prawoWyr.setShortcut(QKeySequence('Ctrl+p'))

        srodekWyr = QAction('&wysrodkuj', self)
        srodekWyr.setStatusTip('zaznacz linijki aby wysrodkowac')
        srodekWyr.triggered.connect(self.doSrodka)
        srodekWyr.setShortcut(QKeySequence('Ctrl+w'))

        jusWyr = QAction('&justowanie', self)
        jusWyr.setStatusTip('zaznacz linijki aby justowac')
        jusWyr.triggered.connect(self.doJust)
        jusWyr.setShortcut(QKeySequence('Ctrl+j'))



        ##################
        wyrMenu = menu.addMenu('Wyrownywanie')

        wyrMenu.addAction(lewoWyr)
        wyrMenu.addSeparator()

        wyrMenu.addAction(prawoWyr)
        wyrMenu.addSeparator()

        wyrMenu.addAction(srodekWyr)
        wyrMenu.addSeparator()

        wyrMenu.addAction(jusWyr)
        wyrMenu.addSeparator()

        # Czcionka
        kolorCzcionki = QAction('&czarny', self)
        kolorCzcionki.setStatusTip('zaznacz text do pokolorowania')
        kolorCzcionki.triggered.connect(self.czarny)
        kolorCzcionki.setShortcut(QKeySequence('Ctrl+k'))

        kolorCzcionki1 = QAction('&czerwony', self)
        kolorCzcionki1.setStatusTip('zaznacz text do pokolorowania')
        kolorCzcionki1.triggered.connect(self.czerwony)
        kolorCzcionki1.setShortcut(QKeySequence('Ctrl+h'))

        kolorCzcionki2 = QAction('&zielony', self)
        kolorCzcionki2.setStatusTip('zaznacz text do pokolorowania')
        kolorCzcionki2.triggered.connect(self.zielony)
        kolorCzcionki2.setShortcut(QKeySequence('Ctrl+u'))

        krojCzcionki = QAction('&Segoe UI', self)
        krojCzcionki.setStatusTip('Segoe UI')
        krojCzcionki.triggered.connect(self.czcionka)
        krojCzcionki.setShortcut(QKeySequence('Ctrl+m'))

        krojCzcionki1 = QAction('&Script MT Bold', self)
        krojCzcionki1.setStatusTip('Script MT Bold')
        krojCzcionki1.triggered.connect(self.czcionka1)
        krojCzcionki1.setShortcut(QKeySequence('Ctrl+r'))

        krojCzcionki2 = QAction('&Segoe Print', self)
        krojCzcionki2.setStatusTip('Segoe Print')
        krojCzcionki2.triggered.connect(self.czcionka2)
        krojCzcionki2.setShortcut(QKeySequence('Ctrl+y'))

        ##################
        czcMenu = menu.addMenu('Czcionka')

        fileSubMenu = czcMenu.addMenu('&Kolor czcionki')
        fileSubMenu.addAction(kolorCzcionki)
        fileSubMenu.addAction(kolorCzcionki1)
        fileSubMenu.addAction(kolorCzcionki2)

        czcMenu.addSeparator()

        fileSubMenu1 = czcMenu.addMenu('&Kroj  czcionki')
        fileSubMenu1.addAction(krojCzcionki)
        fileSubMenu1.addAction(krojCzcionki1)
        fileSubMenu1.addAction(krojCzcionki2)


        czcMenu.addSeparator()


        # G R I D
        layout.addWidget(self.label1)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    def nowy(self):
        self.textEdit.setText('')

    def czcionka(self):
        self.textEdit.setFontFamily('Segoe UI')

    def czcionka1(self):
        self.textEdit.setFontFamily('Script MT Bold')

    def czcionka2(self):
        self.textEdit.setFontFamily('Segoe Print')

    def czarny(self):
        black = QColor(0, 0, 0)
        self.textEdit.setTextColor(black)
    def czerwony(self):
        red = QColor(255, 0, 0)
        self.textEdit.setTextColor(red)
    def zielony(self):
        green = QColor(0, 128, 0)
        self.textEdit.setTextColor(green)

    def doLewej(self):
        self.textEdit.setAlignment(Qt.AlignLeft)

    def doPrawej(self):
        self.textEdit.setAlignment(Qt.AlignRight)

    def doSrodka(self):
        self.textEdit.setAlignment(Qt.AlignCenter)

    def doJust(self):
        self.textEdit.setAlignment(Qt.AlignJustify)

    def podkreslenie(self):
        self.textEdit.setFontUnderline(not self.textEdit.fontUnderline())

    def pochyl(self):
        self.textEdit.setFontItalic(not self.textEdit.fontItalic())

    def pogrub(self):
        self.textEdit.setFontWeight(700) if self.textEdit.fontWeight() == 400 else self.textEdit.setFontWeight(400)

    def otworzPlik(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Proprietary FileFormat (*.mjmj All files (*.*)")
        try:
            with open(file, 'r') as f:
                text = f.read()
        except Exception as e:
            self.error(str(e))
        else:
            self.file = file
            self.textEdit.setText(text)
            self.setWindowTitle(self.file if self.file else "Not Saved")

    def zapiszPlik(self):
        if self.file is None:
            return self.zapiszJako()
        text = self.textEdit.toHtml()

        try:
            with open(self.file, 'w') as f:
                f.write(text)

        except Exception as e:
            self.error(str(e))

    def zapiszJako(self):
        file, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Proprietary FileFormat (*.mjmj All files (*.*)")
        if not file:
            return

        text = self.textEdit.toHtml()
        try:
            with open(file, 'w') as f:
                f.write(text)
        except Exception as e:
            self.error(str(e))
        else:
            self.file = file
            self.setWindowTitle(self.file if self.file else "Nie zapisano")

    def error(self, error):
        print(error)

    def cos(self):
        print('cos')

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()