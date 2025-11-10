from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(696, 771)
        Dialog.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.mainLabel = QtWidgets.QLabel(Dialog)
        self.mainLabel.setGeometry(QtCore.QRect(190, 20, 321, 41))
        self.mainLabel.setStyleSheet("color:rgb(0, 0, 0); font-size:28pt; font:bold;\n")
        self.mainLabel.setObjectName("mainLabel")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 110, 171, 31))
        self.label_2.setStyleSheet("font-size:18pt; font:bold")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 111, 31))
        self.label_3.setStyleSheet("font-size:18pt;font:bold")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(70, 230, 121, 31))
        self.label_4.setStyleSheet("font-size:18pt;font:bold")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 290, 121, 31))
        self.label_5.setStyleSheet("font-size:18pt;font:bold")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(70, 350, 191, 31))
        self.label_6.setStyleSheet("font-size:18pt;font:bold")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(70, 410, 121, 31))
        self.label_7.setStyleSheet("font-size:18pt;font:bold")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(70, 470, 121, 31))
        self.label_8.setStyleSheet("font-size:18pt;font:bold")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(70, 530, 241, 41))
        self.label_9.setStyleSheet("font-size:18pt;font:bold")
        self.label_9.setObjectName("label_9")
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(277, 700, 141, 51))  # Centered horizontally
        self.addButton.setStyleSheet("color:rgb(255, 255, 255); font-size:16pt; background-color:rgb(0, 128, 0); font:bold")  # Redesigned to green
        self.addButton.setObjectName("addButton")
        self.productName = QtWidgets.QLineEdit(Dialog)
        self.productName.setGeometry(QtCore.QRect(340, 100, 311, 41))
        self.productName.setStyleSheet("font-size:16pt;")
        self.productName.setObjectName("productName")
        self.barcode = QtWidgets.QLineEdit(Dialog)
        self.barcode.setGeometry(QtCore.QRect(340, 160, 311, 41))
        self.barcode.setStyleSheet("font-size:16pt;")
        self.barcode.setObjectName("barcode")
        self.quantity = QtWidgets.QLineEdit(Dialog)
        self.quantity.setGeometry(QtCore.QRect(340, 280, 311, 41))
        self.quantity.setStyleSheet("font-size:16pt;")
        self.quantity.setObjectName("quantity")
        self.categoryChoice = QtWidgets.QComboBox(Dialog)
        self.categoryChoice.setGeometry(QtCore.QRect(340, 220, 311, 41))
        self.categoryChoice.setStyleSheet("font-size:16pt")
        self.categoryChoice.setObjectName("categoryChoice")
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.expDate = QtWidgets.QDateEdit(Dialog)
        self.expDate.setGeometry(QtCore.QRect(339, 338, 309, 44))
        self.expDate.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.expDate.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.expDate.setAutoFillBackground(False)
        self.expDate.setStyleSheet("font-size:16pt;background-color:rgb(255, 255, 255)")
        self.expDate.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.expDate.setCalendarPopup(True)
        self.expDate.setCurrentSectionIndex(0)
        self.expDate.setObjectName("expDate")
        self.expDate.setDate(QtCore.QDate.currentDate())  # Set to SYSDATE (current date)
        self.supplierName = QtWidgets.QLineEdit(Dialog)
        self.supplierName.setGeometry(QtCore.QRect(340, 400, 311, 41))
        self.supplierName.setStyleSheet("font-size:16pt;")
        self.supplierName.setObjectName("supplierName")
        self.price = QtWidgets.QLineEdit(Dialog)
        self.price.setGeometry(QtCore.QRect(340, 460, 311, 41))
        self.price.setStyleSheet("font-size:16pt;")
        self.price.setObjectName("price")
        self.productDescription = QtWidgets.QTextEdit(Dialog)
        self.productDescription.setGeometry(QtCore.QRect(340, 520, 311, 141))
        self.productDescription.setObjectName("productDescription")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.addButton.clicked.connect(self.validateInputs)

        self.existing_barcodes = set()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Register Product"))
        self.mainLabel.setText(_translate("Dialog", "Register Product"))
        self.label_2.setText(_translate("Dialog", "Product Name"))
        self.label_3.setText(_translate("Dialog", "Barcode"))
        self.label_4.setText(_translate("Dialog", "Category"))
        self.label_5.setText(_translate("Dialog", "Quantity"))
        self.label_6.setText(_translate("Dialog", "Expiration Date"))
        self.label_7.setText(_translate("Dialog", "Supplier"))
        self.label_8.setText(_translate("Dialog", "Price"))
        self.label_9.setText(_translate("Dialog", "Product Description"))
        self.addButton.setText(_translate("Dialog", "Add Product"))
        self.categoryChoice.setItemText(0, _translate("Dialog", "Select Category"))
        self.categoryChoice.setItemText(1, _translate("Dialog", "Antihistamine"))
        self.categoryChoice.setItemText(2, _translate("Dialog", "Antibiotics"))
        self.categoryChoice.setItemText(3, _translate("Dialog", "Vitamins"))
        self.categoryChoice.setItemText(4, _translate("Dialog", "Paracetamol"))
        self.categoryChoice.setItemText(5, _translate("Dialog", "Painkiller"))
        self.categoryChoice.setCurrentIndex(0)  # Start with "Select Category"

    def validateInputs(self):
        fill_up = []
        other_errors = []

        product_name = self.productName.text().strip()
        barcode = self.barcode.text().strip()
        quantity = self.quantity.text().strip()
        exp_date = self.expDate.date()
        price = self.price.text().strip()
        category_index = self.categoryChoice.currentIndex()

        # Check product name
        if not product_name:
            fill_up.append("Product Name")

        # Check barcode
        if not barcode:
            fill_up.append("Barcode")
        else:
            try:
                int(barcode)
                if barcode in self.existing_barcodes:
                    other_errors.append("Barcode must be unique. This one already exists.")
            except ValueError:
                other_errors.append("Barcode must be a number.")

        # Check category
        if category_index == 0:
            fill_up.append("Category")

        # Check quantity
        if not quantity:
            fill_up.append("Quantity")
        else:
            try:
                int(quantity)
                if int(quantity) <= 0:
                    other_errors.append("Quantity must be greater than 0.")
            except ValueError:
                other_errors.append("Quantity must be a number.")

        # Check expiration date
        if not exp_date.isValid():
            fill_up.append("Expiration Date")

        # Check price
        if not price:
            fill_up.append("Price")
        else:
            try:
                if float(price) <= 0:
                    other_errors.append("Price must be greater than 0.")
            except ValueError:
                other_errors.append("Price must be a number.")

        # Alert for unfilled fields
        if fill_up:
            QMessageBox.warning(None, "Input Error", "Fill up " + ", ".join(fill_up))
            return

        # Alert for other validation errors
        if other_errors:
            QMessageBox.warning(None, "Input Error", "\n".join(other_errors))
            return

        # If everything is valid
        self.existing_barcodes.add(barcode)
        QMessageBox.information(None, "Success", "Product added successfully!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
