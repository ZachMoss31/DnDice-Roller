#Application driver
from Lib.dicelib import *

#UI Libs
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

#System for command line use

#Best main window use is to subclass it
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("DnDice")
        self.setFixedSize(400,300)
        button = QPushButton("Roll Dice")
        self.setCentralWidget(button)
    

def main():
    
    app = QApplication([])

    #window = QWidget()
    window = MainWindow()
    window.show()
    
    #Event Loop
    app.exec()
    
    #Preprocessing...
    print("Enter a number to roll, or {q} to quit and close.")
    choice = ""
    
    #Driving...
    while choice != 'q':
        choice = input("Enter which kind of dice to roll: ")
        if choice.isdigit():
            RollDice(int(choice), 's')
        elif choice.isalpha():
            CheckChoice(choice)
        else:
            print("Invalid input")
            
    print("Exited rolling.")  

if __name__ == "__main__":
    main()