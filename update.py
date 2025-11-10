from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(703, 578)
        Dialog.setWindowTitle("Update Product")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(350, 20, 221, 51))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 90, 201, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        label_texts = [
            "Product Name", "Description", "Category",
            "Mfg. Date", "Exp. Date", "Barcode",
            "Price", "Quantity"
        ]

        self.labels = []
        for text in label_texts:
            lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
            lbl.setText(f"<html><head/><body><p align='center'><span style=' font-size:14pt; font-weight:600;'>{text}</span></p></body></html>")
            self.verticalLayout.addWidget(lbl)
            self.labels.append(lbl)

        # Input fields
        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(360, 90, 211, 31))
        self.textEdit.setPlaceholderText("Enter product name")

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(360, 130, 211, 41))
        self.textEdit_2.setPlaceholderText("Brief description...")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(360, 200, 211, 22))
        self.comboBox.addItems([
            "", "Analgesics", "Antibiotics", "Antidepressants",
            "Antihistamines", "Antihypertensives"
        ])
        self.comboBox.setToolTip("Select the product category")

        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(360, 240, 211, 22))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QtCore.QDate.currentDate())  # Default to today

        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog)
        self.dateEdit_2.setGeometry(QtCore.QRect(360, 290, 211, 22))
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())  # Default to today

        self.textEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(360, 330, 211, 31))
        self.textEdit_3.setPlaceholderText("Enter barcode (optional)")

        self.textEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(360, 370, 211, 31))
        self.textEdit_4.setPlaceholderText("Enter price (₱)")
        self.textEdit_4.setValidator(QtGui.QDoubleValidator(0.01, 999999.99, 2))

        self.textEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(360, 420, 211, 31))
        self.textEdit_5.setPlaceholderText("Enter quantity")
        self.textEdit_5.setValidator(QtGui.QIntValidator(1, 999999))

        # Save button
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(390, 500, 161, 51))
        self.pushButton.setText("Save Changes")
        self.pushButton.setToolTip("Click to save all changes")

        # Tab order for accessibility
        Dialog.setTabOrder(self.textEdit, self.textEdit_2)
        Dialog.setTabOrder(self.textEdit_2, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.dateEdit)
        Dialog.setTabOrder(self.dateEdit, self.dateEdit_2)
        Dialog.setTabOrder(self.dateEdit_2, self.textEdit_3)
        Dialog.setTabOrder(self.textEdit_3, self.textEdit_4)
        Dialog.setTabOrder(self.textEdit_4, self.textEdit_5)
        Dialog.setTabOrder(self.textEdit_5, self.pushButton)

        # Connect button
        self.pushButton.clicked.connect(self.validate_form)

        # Title
        self.label.setText("<html><head/><body><p align='center'><span style=' font-size:14pt; font-weight:600;'>Update Product</span></p></body></html>")

        self.original_values = self.capture_current_values()
        self.any_change = False
        self.setup_change_tracking()


    def capture_current_values(self):
        return {
            "name": self.textEdit.text(),
            "desc": self.textEdit_2.toPlainText(),
            "category": self.comboBox.currentText(),
            "mfg_date": self.dateEdit.date().toPyDate(),
            "exp_date": self.dateEdit_2.date().toPyDate(),
            "barcode": self.textEdit_3.text(),
            "price": self.textEdit_4.text(),
            "quantity": self.textEdit_5.text(),
        }


    def setup_change_tracking(self):
        fields = [
            self.textEdit, self.textEdit_2, self.comboBox,
            self.dateEdit, self.dateEdit_2,
            self.textEdit_3, self.textEdit_4, self.textEdit_5
        ]
        for field in fields:
            if isinstance(field, QtWidgets.QLineEdit):
                field.textChanged.connect(self.mark_changed)
            elif isinstance(field, QtWidgets.QTextEdit):
                field.textChanged.connect(self.mark_changed)
            elif isinstance(field, QtWidgets.QComboBox):
                field.currentIndexChanged.connect(self.mark_changed)
            elif isinstance(field, QtWidgets.QDateEdit):
                field.dateChanged.connect(self.mark_changed)

    def mark_changed(self):
        self.any_change = True


    def validate_form(self):
        name = self.textEdit.text().strip()
        desc = self.textEdit_2.toPlainText().strip()
        category = self.comboBox.currentText().strip()
        price_text = self.textEdit_4.text().strip()
        quantity_text = self.textEdit_5.text().strip()
        mfg_date = self.dateEdit.date().toPyDate()
        exp_date = self.dateEdit_2.date().toPyDate()

        today = date.today()


        if not self.any_change:
            self.show_error("No changes detected. Please modify some fields before saving.")
            return

        # Check required fields
        if not name or not category or not price_text or not quantity_text:
            self.show_error("Please fill out all required fields:\n- Product Name\n- Category\n- Price\n- Quantity")
            return

        # Date validations
        if exp_date < today:
            self.show_error("Expiration Date cannot be a past date.")
            return

        if mfg_date > exp_date:
            self.show_error("Manufacturing Date cannot be later than Expiration Date.")
            return


        try:
            price = float(price_text)
            if price <= 0:
                self.show_error("Price must be greater than ₱0.")
                return
        except ValueError:
            self.show_error("Price must be a valid number.")
            return

        try:
            qty = int(quantity_text)
            if qty <= 0:
                self.show_error("Quantity must be greater than 0.")
                return
        except ValueError:
            self.show_error("Quantity must be an integer.")
            return

        # Success
        self.show_success("✅ Changes Saved Successfully!")

        # Reset change tracking
        self.any_change = False
        self.original_values = self.capture_current_values()


    def show_success(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def show_error(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Validation Error")
        msg.setText(message)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
