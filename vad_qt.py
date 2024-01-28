import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QRect, QUrl
from PyQt5.QtGui import QRegion, QIcon
from sk2 import Ui_MainWindow


class VeteAlDiablo(QMainWindow, Ui_MainWindow):
    def __init__(self, **kwargs):
        super(VeteAlDiablo, self).__init__(**kwargs)
        self.setupUi(self)
        self.setMaximumSize(240,240)


        self.ebt(self.bt1)
        self.ebt(self.bt2)
        self.ebt(self.bt3)
        self.bt1.clicked.connect(lambda:self.reproduce('idiota.mp3'))
        self.bt2.clicked.connect(lambda:self.reproduce('callate.mp3'))
        self.bt3.clicked.connect(lambda:self.reproduce('vete_al_diablo.mp3'))
        self.btx.clicked.connect(self.close)
        ico = QIcon()
        ico.addFile(r'x_w.ico')
        self.btx.setIcon(ico)
        self.player = QMediaPlayer()
        self.player.setVolume(100)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet('QWidget#centralwidget{background-image: url(bn_240.png);}')
        self._vpos = None
        self.setWindowIcon(QIcon('vad.ico'))
        self.setWindowTitle('Vete al diablo v0.1qt')


    def ebt(self, bt):
        bt.setMask(QRegion(QRect(-1,-1,62,62), QRegion.Ellipse))
        bt.setStyleSheet(
            "QPushButton {background-color: white; border: 0.8px solid black; "
            "border-radius: 29.4px} QPushButton:pressed "
            "{background-color: #d5d2c8;}"
        )

    def reproduce(self, archivo):
        self.player.setMedia(QMediaContent(QUrl(archivo)))
        self.player.play()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self._vpos = e.pos()

    def mouseReleaseEvent(self, e):
        self._vpos = None

    def mouseMoveEvent(self, e):
        if self.isMaximized():
            return
        if e.buttons() == Qt.LeftButton and self._vpos:
            pos = e.pos() - self._vpos
            self.move(self.pos() + pos)

    
if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    vad = VeteAlDiablo()
    vad.show()
    sys.exit(app.exec_())