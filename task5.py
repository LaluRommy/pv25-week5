from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtGui import  QShortcut, QKeySequence
import sys
import re
from tugas_ui import Ui_MainWindow

class Form(QtWidgets.QMainWindow):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.lineEdit_4.setInputMask('+62 999 9999 9999')

        self.ui.comboBox.addItems([" ","Male", "Female"])
        self.ui.comboBox_2.addItems([" ", "Elementary School", "Junior High School", "Senior High School", "Diploma", "Bachelor's Degree", "Master's Degree", "Doctorial Degree"])

        self.ui.pushButton.clicked.connect(self.clear)
        self.ui.pushButton_2.clicked.connect(self.save_data)
        
        QShortcut(QKeySequence('Q'), self, self.close)
        
    def show_warning(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("")
        msg.setText(message)
        msg.exec()

    def save_data(self):
        name = self.ui.lineEdit.text()
        email = self.ui.lineEdit_2.text()
        age = self.ui.lineEdit_3.text()
        phone = self.ui.lineEdit_4.text()
        address = self.ui.textEdit.toPlainText()
        gender = self.ui.comboBox.currentText()
        education = self.ui.comboBox_2.currentText()
        
        if not name or not email or not age or not phone or not address or gender ==' ' or education ==' ':
            self.show_warning("All fields are requared.")
            return
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_warning("Please enter a valid email address.")
            return
        
        if not age.isdigit():
            self.show_warning("Please enter a valid age (integer value).")
            return
        
        if len(phone.replace(' ', '').replace('+62', '')) != 11:
            self.show_warning('Please enter a valid 13 digit phone number.')
            return
        
        self.show_warning("Profile saved succesfully")
        self.clear()

    def clear(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.lineEdit_4.clear()
        self.ui.textEdit.clear()
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox_2.setCurrentIndex(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec())
