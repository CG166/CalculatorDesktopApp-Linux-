import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        ##Customizing Window
        self.setWindowTitle("Calculator")
        self.setGeometry(0, 0, 650, 650) #setGeometry(x, y, width, height)
        #Setting Icon
        self.setWindowIcon(QIcon("Icon.png"))
        #Creating Variable/elements
        self.button = QPushButton("Click Me!", self)
        #Initializing GUI
        self.initGUI()

        #Creating text
        #label = QLabel("Hello World!", self)
        #label.setFont(QFont("Arial", 40))
        #Setting position of the text(label)
        #label.setGeometry(0, 0, 500, 100)
        #label.setStyleSheet("color: blue;"
                           # "background-color: pink;" 
                           # "font-weight: bold;")
        #Setting text(label) alignment
        #label.setAlignment(Qt.AlignTop) #Vertically top
        #label.setAlignment(Qt.AlignBottom) #Vertically bottom
        #label.setAlignment(Qt.AlignVCenter) #Vertically Center(default)

        #label.setAlignment(Qt.AlignRight) #Horizontally right
        #label.setAlignment(Qt.AlignLeft)   #Horizontally left(default)
        #label.setAlignment(Qt.AlignHCenter) #Horizontally center

        #Combo postioning/alignment
        #label.setAlignment(Qt.AlignRight | Qt.AlignTop)

        #Using images
        #image = QLabel(self)
        #image.setGeometry(0, 0, 100, 150)

        #pixmap = QPixmap("Icon.png")
        #image.setPixmap(pixmap)
        #image.setScaledContents(True) #Scales image to take up the entire width and height to the container

        #Aligning/position
        #image.setGeometry((self.width() - image.width()) // 2, 0, image.width(), image.height())

    def initGUI(self):
        #Setting central widget
        #central_widget = QWidget()
        #self.setCentralWidget(central_widget)

        #Creating items
        #label1 = QLabel("#1", self)
        #label2 = QLabel("#2", self)
        #label3 = QLabel("#3", self)
        #label4 = QLabel("#4", self)

        #label1.setStyleSheet("background-color: orange;")
        #label2.setStyleSheet("background-color: pink;")
        #label3.setStyleSheet("background-color: blue;")
        #label4.setStyleSheet("background-color: yellow;")

        #Vertical Layout Manager
        #vbox = QVBoxLayout()  for Horizantal just replace with QHBoxLayout()

        #vbox.addWidget(label1)
        #vbox.addWidget(label2)
        #vbox.addWidget(label3)
        #vbox.addWidget(label4)

        #central_widget.setLayout(vbox)

        #Grid Layout
        #grid = QGridLayout() 

        #grid.addWidget(label1, 0, 0)
        #grid.addWidget(label2, 0, 1)
        #grid.addWidget(label3, 1, 0)
        #grid.addWidget(label4, 2, 1)

        #central_widget.setLayout(grid)

                #Creating the application widget (for easy layout structuring)
        self.appWidget = QWidget(self)

        #Using Buttons
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)

    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")
        self.button.setDisabled(True)






        

def main():
    app = QApplication(sys.argv)
    ##Setting up basic window/app
    window = Calculator()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()



    self.styleButton(self.clearButton, "images/clear.png", int(2.7 * self.numButtonWidth), self.numButtonHeight)
    self.styleButton(self.backButton, "images/backArrow.png", int(1.2 * self.numButtonWidth), self.numButtonHeight)
    self.styleButton(self.equalsButton, "images/equalSign.png", self.numButtonWidth, self.numButtonHeight)