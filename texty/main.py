""" making a simple text editor app in python """

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

class screen(QMainWindow):

    def __init__(self):
        super(screen, self).__init__()
        uic.loadUi('untitled.ui', self)
        self.show()

        self.setWindowTitle("TEXTY")

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)


    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;Python Files (*.py)", options = options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

def main():
    app = QApplication([])
    window = screen()
    app.exec_()


if __name__ == '__main__' :
    main()