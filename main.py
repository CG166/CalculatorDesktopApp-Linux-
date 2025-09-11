import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,  QSize

import functions
import resources_rc

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        ##Customizing Window
        self.setWindowTitle("Calculator")
        self.setGeometry(0, 0, 600, 655) #setGeometry(x, y, width, height)
        #Setting Icon
        self.setWindowIcon(QIcon(":/images/icon.png"))

        #Button sizes
        self.numButtonWidth = 80
        self.numButtonHeight = 89

        self.symButtonWidth = 80
        self.symButtonHeight = 80

        #Creating button container
        self.buttonContainer = QWidget(self)

        #Creating buttons
        self.plusButton = QPushButton(self.buttonContainer)
        self.minusButton = QPushButton(self.buttonContainer)
        self.muliplicationButton = QPushButton(self.buttonContainer)
        self.divisionButton = QPushButton(self.buttonContainer)
        self.decimalButton = QPushButton(self.buttonContainer)

        self.button0 = QPushButton(self.buttonContainer)
        self.button1 = QPushButton(self.buttonContainer)
        self.button2 = QPushButton(self.buttonContainer)
        self.button3 = QPushButton(self.buttonContainer)
        self.button4 = QPushButton(self.buttonContainer)
        self.button5 = QPushButton(self.buttonContainer)
        self.button6 = QPushButton(self.buttonContainer)
        self.button7 = QPushButton(self.buttonContainer)
        self.button8 = QPushButton(self.buttonContainer)
        self.button9 = QPushButton(self.buttonContainer)

        self.clearButton = QPushButton(self.buttonContainer)
        self.backButton = QPushButton(self.buttonContainer)
        self.equalsButton = QPushButton(self.buttonContainer)

        #Functional Variables
        self.queue = []
        self.displayText = ""
        
        #Initializing GUI
        self.initGUI()
    
    def initGUI(self):

        #Setting window background
        self.background = QLabel(self)
        self.background.setScaledContents(True)
        self.background.setPixmap(QPixmap(":/images/background.png"))
        self.background.setGeometry(0, 0, self.width(), self.height())

        #Setting the background/layout layout
        baseLayout = QVBoxLayout(self.background)

        #Creating display box         
        self.displayBox = QLineEdit()
        self.displayBox.setAlignment(Qt.AlignRight)
        self.displayBox.setReadOnly(True)
        self.displayBox.setCursorPosition(len(self.displayText))
        self.displayBox.setStyleSheet("""
            QLineEdit {
                color: #51b6c3;
                background-color: transparent;
                font-size: 75px;
                font-family: 'Comic Sans MS', cursive;
                border: none;
                font-weight: bold;
             }
        """)

        #Placing displaybox into it's own layout segment
        displayBoxLayout = QHBoxLayout()
        displayBoxLayout.addSpacing(50)
        displayBoxLayout.addWidget(self.displayBox)
        displayBoxLayout.addSpacing(50)

        #Adding displaybox segment to base layout
        baseLayout.addStretch(1)
        baseLayout.addLayout(displayBoxLayout)

        #Styling Number Buttons
        self.styleButton(self.plusButton, ":/images/plus.png", self.symButtonWidth, self.symButtonHeight)
        self.styleButton(self.minusButton, ":/images/minus.png", self.symButtonWidth, self.symButtonHeight)
        self.styleButton(self.muliplicationButton, ":/images/multiplication.png", self.symButtonWidth, self.symButtonHeight)
        self.styleButton(self.divisionButton, ":/images/division.png", self.symButtonWidth, self.symButtonHeight)
        self.styleButton(self.decimalButton, ":/images/decimal.png", self.symButtonWidth, self.symButtonHeight)

        self.styleButton(self.button0, ":/images/0.png", self.numButtonWidth, self.numButtonHeight)
        self.styleButton(self.button1, ":/images/1.png", self.numButtonWidth, self.numButtonHeight)
        self.styleButton(self.button2, ":/images/2.png", self.numButtonWidth, self.numButtonHeight)
        self.styleButton(self.button3, ":/images/3.png", self.numButtonWidth, self.numButtonHeight)
        self.styleButton(self.button4, ":/images/4.png", self.numButtonWidth, self.numButtonHeight)
        self.styleButton(self.button5, ":/images/5.png", self.numButtonWidth, self.numButtonHeight)
        self.styleButton(self.button6, ":/images/6.png", self.numButtonWidth, self.numButtonHeight)
        self.styleButton(self.button7, ":/images/7.png", self.numButtonWidth, self.numButtonHeight)
        self.styleButton(self.button8, ":/images/8.png", self.numButtonWidth, self.numButtonHeight)
        self.styleButton(self.button9, ":/images/9.png", self.numButtonWidth, self.numButtonHeight)

        self.styleButton(self.clearButton, ":/images/clear.png", int(3 * self.numButtonWidth), self.numButtonHeight-1)
        self.styleButton(self.backButton, ":/images/backArrow.png", int(1.2 * self.numButtonWidth), self.numButtonHeight)
        self.styleButton(self.equalsButton, ":/images/equalSign.png", self.numButtonWidth, self.numButtonHeight)

        #Button Grid Layout (button rows 1-3)
        buttonGrid = QGridLayout()

        buttonGrid.addWidget(self.plusButton, 0, 0)
        buttonGrid.addWidget(self.minusButton, 0, 1)
        buttonGrid.addWidget(self.muliplicationButton, 0, 2)
        buttonGrid.addWidget(self.divisionButton, 0, 3)
        buttonGrid.addWidget(self.decimalButton, 0, 4)
    
        buttonGrid.addWidget(self.button0, 2, 0)
        buttonGrid.addWidget(self.button1, 1, 0)
        buttonGrid.addWidget(self.button2, 1, 1)
        buttonGrid.addWidget(self.button3, 1, 2)
        buttonGrid.addWidget(self.button4, 1, 3)
        buttonGrid.addWidget(self.button5, 1, 4)
        buttonGrid.addWidget(self.button6, 2, 1)
        buttonGrid.addWidget(self.button7, 2, 2)
        buttonGrid.addWidget(self.button8, 2, 3)
        buttonGrid.addWidget(self.button9, 2, 4)
        buttonGrid.addWidget(self.equalsButton, 3, 4)

        #Sublayout for bottom row of buttons
        bottomRow = QHBoxLayout()
        bottomRow.addWidget(self.clearButton)
        bottomRow.addWidget(self.backButton)

        buttonGrid.addLayout(bottomRow, 3, 0, 1, 4)

        #Button layout styling
        buttonGrid.setContentsMargins(25, 25, 28, 15)
        buttonGrid.setSpacing(15)
        self.buttonContainer.setLayout(buttonGrid)

        #Placing Button container into it's own layout segment
        buttonSegmentLayout = QHBoxLayout()
        buttonSegmentLayout.addWidget(self.buttonContainer)

        #Adding button section segment to base layout
        baseLayout.addStretch(1)
        baseLayout.addLayout(buttonSegmentLayout)
        baseLayout.addStretch(1)

        #Functionality Section
        self.connectButtons()

    def styleButton(self, button, image, width, height):
        button.setFixedSize(width, height)
        pixmap = QPixmap(image)
        icon = QIcon(pixmap)
        button.setIcon(icon)
        button.setIconSize(QSize(width, height))
        button.raise_()

    def connectButtons(self):
        btnNames = ['button0', 'button1', 'button2', 'button3', 'button4', 'button5', 'button6', 'button7', 'button8', 'button9', 
        'plusButton', 'minusButton', 'muliplicationButton', 'divisionButton', 'decimalButton']

        btnContent = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '.']
        
        for btnName, char in zip(btnNames, btnContent):
            button = getattr(self, btnName)
            button.clicked.connect(lambda _, c=char: self.addChar(c))

        self.clearButton.clicked.connect(self.clear)
        self.backButton.clicked.connect(self.backSpace)
        self.equalsButton.clicked.connect(self.calculate)

    def addChar(self, c):
        
        if self.displayText:
            last_char = self.displayText[-1]
        else:
            if self.isOp(c) and c != '-' or c == '.':
                return
            last_char = None

        if c == '-' and last_char == '-':
            self.displayText = self.displayText[:-1]
            self.displayText  += '+'
            self.displayBox.setText(self.displayText)
        elif c == '-' and last_char != '+' and self.isOp(last_char):
            self.displayText += c
            self.displayBox.setText(self.displayText)
        elif c == '+' and self.isOp(last_char):
            pass
        elif c == '.' and last_char == '.':
            pass
        elif c == '.' and self.isClear() == False:
            pass
        elif self.isOp(c) and self.isOp(last_char):
            self.displayText = self.displayText[:-1]
            self.displayText  += c
            self.displayBox.setText(self.displayText)
        else:
            self.displayText += c
            self.displayBox.setText(self.displayText)

    def clear(self):
        self.displayText = ""
        self.queue = []
        self.displayBox.setText(self.displayText)
        
    def backSpace(self):
        self.queue = []
        self.displayText = self.displayText[:-1]
        self.displayBox.setText(self.displayText)

    def calculate(self):
        self.tokenize()
        #print(f"State of queue before it is input into the evaluation function is {self.queue}")
        self.displayText = functions.evaluate(self.queue)
        self.displayBox.setText(self.displayText)

    def tokenize(self):
        #print(f"Display text before tokenization {self.displayText}")
        token = ""
        textEnd = len(self.displayText) - 1
        for i, c in enumerate(self.displayText):
            if (not self.isOp(c) and i != textEnd) or (i == 0) or (c == '-' and self.isOp(self.displayText[i-1]) and self.displayText[i-1] != '.') :
                token += c
            elif self.isOp(c):
                self.queue.append(float(token))
                #print(f"Number {token} appended to list. State of queue is {self.queue}")
                self.queue.append(c)
                #print(f"Operation {c} appended to list. State of queue is {self.queue}")
                token = ""
            elif not self.isOp(c) and i == textEnd:
                token += c
                #print(f"Last number {token} to be appended to list {self.queue}")
                self.queue.append(float(token))

    def isOp(self, c):
        if c == '+' or c == '-' or c == '*' or c == '/':
            return True
        else:
            return False

    #This function checks if it is clear to add a decimal point(there is no previous decimal point
    # so that the floats can be separated cleanly)
    # Functions by checking to see if we run into an operator before we run into another decimal point when
    # iterating through the existing text in reverse.  
    def isClear(self):
        #Retrieve the last number/token
        token = ""
        for c in reversed(self.displayText):
            if self.isOp(c):
                break
            else:
                token += c
        #print(f"The token being analyzed is {token}")
        #Check if the last token already has a period
        for c in token:
            if c == '.':
                return False
        return True


def main():
    app = QApplication(sys.argv)
    ##Setting up basic window/app
    window = Calculator()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()