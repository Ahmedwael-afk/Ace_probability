from Gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import scipy.stats
import sys, os





class AppWindow(QtWidgets.QMainWindow,Ui_MainWindow): #Test    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.verticalSlider.valueChanged.connect(self.update_slider)
        self.pushButton.clicked.connect(self.Ace_probability)
        self.player = QMediaPlayer()


    def playAudioFile(self):
        url = QUrl.fromLocalFile(self.File_Path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        # currentVolume = self.player.volume() #
        # self.player.setVolume(currentVolume - 30)
        self.player.play()



    def update_slider(self,event):
        self.label.setPixmap(QtGui.QPixmap("Images/player.jpg"))
        self.label_2.setPixmap(QtGui.QPixmap("Images/serving.jpg"))
        self.lcd.display(event)
        self.event = event
    
    def Ace_probability(self):
        self.label_2.setPixmap(QtGui.QPixmap("Images/field_mario.jpg"))
        self.x = scipy.stats.norm.cdf(self.event,160,20)
        self.label_5.setWordWrap(True)
        if self.x >= 0.999:
            self.label_2.setPixmap(QtGui.QPixmap("Images/serving_ace.jpg"))
            self.label.setPixmap(QtGui.QPixmap("Images/super_player.jpg"))
            self.label_5.setText("YOUR SERVE WILL 100% SCORE AN ACE!!!!\n"+ "\nP = " + str(round(self.x,3)))
            self.label_3.setPixmap(QtGui.QPixmap("Images/Insane_serve.jpg"))
            self.File_Path = os.path.join(os.getcwd(),"Images/Ace.mp3")
            self.playAudioFile()
        elif (self.x >= 0.5) and (self.x < 1):
            self.label.setPixmap(QtGui.QPixmap("Images/celebrating.jpg"))
            self.label_5.setText("WOW, your serve will most likely score an ACE!!\n" + "\nP = " + str(round(self.x,3)))
            self.label_3.setPixmap(QtGui.QPixmap("Images/score.jpg"))
            self.File_Path = os.path.join(os.getcwd(),"Images/Ace.mp3")
            self.playAudioFile()
        else:
            self.label.setPixmap(QtGui.QPixmap("Images/crying.jpg"))
            self.label_5.setText("WOOPSIE, this serve is so weak, you probably won't score an ACE.. \n" + "\nP = " + str(round(self.x,3))) 
            self.label_3.setPixmap(QtGui.QPixmap("Images/missed.jpg"))
            self.File_Path = os.path.join(os.getcwd(),"Images/missed.mp3")
            self.playAudioFile()









app = QtCore.QCoreApplication.instance()
if app is None:
    app = QtWidgets.QApplication(sys.argv)
w = AppWindow()

w.show() # Create the widget and show it
sys.exit(app.exec_()) # Run the app