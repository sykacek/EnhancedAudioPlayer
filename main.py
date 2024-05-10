import sys
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QMainWindow,
    QSlider,
    QVBoxLayout,
    QLayout,
    QApplication,
    QFileDialog,
    QSizePolicy,
    QStatusBar,
    QWidget
)

from PySide6.QtMultimedia import (
    QMediaPlayer,
    QAudioOutput,
    QAudioDevice,

)

from PySide6.QtCore import (
    QSize,
    QUrl,
    Qt
)

#class for storing data
class data():
    def __init__(self):
        self.fileNamePlayer1 = ""


class mainWindow(QMainWindow):

    
    def __init__(self):
        super().__init__()

        self.info = data()

        #initialize player



        #initialize GUI
        self.setWindowTitle("Enhanced Audio Player")
        self.resize(QSize(600, 400))

        self.labelPlayer1 = QLabel()
        self.labelPlayer1.setText("Select a file")

        self.buttonPlayer1 = QPushButton()
        self.buttonPlayer1.setText("Select a file")
        self.buttonPlayer1.pressed.connect(self.buttonPlayer1_handler)

        layout = QVBoxLayout()
        layout.addWidget(self.labelPlayer1)
        layout.addWidget(self.buttonPlayer1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        


    #Qt action handlers
    def buttonPlayer1_handler(self):
        self.info.fileNamePlayer1, _ = QFileDialog.getOpenFileName(self, "Open a file")
        self.labelPlayer1.setText(self.info.fileNamePlayer1)



app = QApplication(sys.argv)

window = mainWindow()
window.show()

sys.exit(app.exec())

