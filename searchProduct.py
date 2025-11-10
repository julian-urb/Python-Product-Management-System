from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(744, 430)
        Dialog.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.searchLabel = QtWidgets.QLabel(Dialog)
        self.searchLabel.setGeometry(QtCore.QRect(40, 10, 251, 41))
        self.searchLabel.setStyleSheet("font-size:24pt; font:bold")
        self.searchLabel.setObjectName("searchLabel")
        self.productList = QtWidgets.QTableWidget(Dialog)
        self.productList.setGeometry(QtCore.QRect(10, 90, 721, 311))
        self.productList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.productList.setObjectName("productList")
        self.productList.setColumnCount(4)
        self.productList.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.productList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.productList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.productList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.productList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.productList.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.productList.setItem(8, 3, item)
        self.productList.horizontalHeader().setDefaultSectionSize(175)
        self.searchField = QtWidgets.QLineEdit(Dialog)
        self.searchField.setGeometry(QtCore.QRect(330, 30, 321, 45))
        self.searchField.setStyleSheet("font-size:18pt")
        self.searchField.setText("")
        self.searchField.setObjectName("searchField")
        self.searchButton = QtWidgets.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(660, 40, 61, 23))
        self.searchButton.setStyleSheet("background-color:rgb(124, 124, 124); color:rgb(255, 255, 255); font:bold")
        self.searchButton.setObjectName("searchButton")
        self.clearButton = QtWidgets.QPushButton(Dialog)
        self.clearButton.setGeometry(QtCore.QRect(620, 40, 21, 23))
        self.clearButton.setStyleSheet("background-color:rgb(131, 45, 29); color:rgb(255, 255, 255); font:bold")
        self.clearButton.setObjectName("clearButton")
        self.searchByName = QtWidgets.QPushButton(Dialog)
        self.searchByName.setGeometry(QtCore.QRect(70, 50, 75, 23))
        self.searchByName.setStyleSheet("background-color:rgb(144, 144, 144); color:rgb(255, 255, 255)")
        self.searchByName.setObjectName("searchByName")
        self.searchByCategory = QtWidgets.QPushButton(Dialog)
        self.searchByCategory.setGeometry(QtCore.QRect(160, 50, 91, 23))
        self.searchByCategory.setStyleSheet("background-color:rgb(144, 144, 144); color:rgb(255, 255, 255)")
        self.searchByCategory.setObjectName("searchByCategory")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.search_mode = 'name'  
        self.categories = ['Antihistamine', 'Paracetamol', 'Vitamins', 'Antibiotic', 'Painkiller']
        self.products = {
            'Ibuprofen': 'Painkiller',
            'Biogesic': 'Paracetamol',
            'Cetirizine': 'Antihistamine',
            'Levocetirizine': 'Antihistamine',
            'Aspirin': 'Painkiller',
            'Loratadine': 'Antihistamine',
            'Mefenamic': 'Painkiller',
            'Decolgen': 'Paracetamol'
        }
        self.product_rows = {
            'Ibuprofen': 1,
            'Biogesic': 2,
            'Cetirizine': 3,
            'Levocetirizine': 4,
            'Aspirin': 5,
            'Loratadine': 6,
            'Mefenamic': 7,
            'Decolgen': 8
        }
        self.searchCombo = None  

        self.searchButton.clicked.connect(self.search_products)
        self.clearButton.clicked.connect(self.clear_search)
        self.searchByName.clicked.connect(self.set_search_name)
        self.searchByCategory.clicked.connect(self.set_search_category)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.searchLabel.setText(_translate("Dialog", "Search Product"))
        item = self.productList.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.productList.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Quantity"))
        item = self.productList.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Reorder Level"))
        item = self.productList.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Price"))
        __sortingEnabled = self.productList.isSortingEnabled()
        self.productList.setSortingEnabled(False)
        item = self.productList.item(1, 0)
        item.setText(_translate("Dialog", "Ibuprofen"))
        item = self.productList.item(1, 1)
        item.setText(_translate("Dialog", "40"))
        item = self.productList.item(1, 2)
        item.setText(_translate("Dialog", "3"))
        item = self.productList.item(1, 3)
        item.setText(_translate("Dialog", "₱45.00"))
        item = self.productList.item(2, 0)
        item.setText(_translate("Dialog", "Biogesic"))
        item = self.productList.item(2, 1)
        item.setText(_translate("Dialog", "35"))
        item = self.productList.item(2, 2)
        item.setText(_translate("Dialog", "1"))
        item = self.productList.item(2, 3)
        item.setText(_translate("Dialog", "₱7.00"))
        item = self.productList.item(3, 0)
        item.setText(_translate("Dialog", "Cetirizine"))
        item = self.productList.item(3, 1)
        item.setText(_translate("Dialog", "12"))
        item = self.productList.item(3, 2)
        item.setText(_translate("Dialog", "2"))
        item = self.productList.item(3, 3)
        item.setText(_translate("Dialog", "₱16.00"))
        item = self.productList.item(4, 0)
        item.setText(_translate("Dialog", "Levocetirizine"))
        item = self.productList.item(4, 1)
        item.setText(_translate("Dialog", "6"))
        item = self.productList.item(4, 2)
        item.setText(_translate("Dialog", "2"))
        item = self.productList.item(4, 3)
        item.setText(_translate("Dialog", "₱25.00"))
        item = self.productList.item(5, 0)
        item.setText(_translate("Dialog", "Aspirin"))
        item = self.productList.item(5, 1)
        item.setText(_translate("Dialog", "22"))
        item = self.productList.item(5, 2)
        item.setText(_translate("Dialog", "1"))
        item = self.productList.item(5, 3)
        item.setText(_translate("Dialog", "₱10.00"))
        item = self.productList.item(6, 0)
        item.setText(_translate("Dialog", "Loratadine"))
        item = self.productList.item(6, 1)
        item.setText(_translate("Dialog", "18"))
        item = self.productList.item(6, 2)
        item.setText(_translate("Dialog", "3"))
        item = self.productList.item(6, 3)
        item.setText(_translate("Dialog", "₱12.00"))
        item = self.productList.item(7, 0)
        item.setText(_translate("Dialog", "Mefenamic"))
        item = self.productList.item(7, 1)
        item.setText(_translate("Dialog", "55"))
        item = self.productList.item(7, 2)
        item.setText(_translate("Dialog", "3"))
        item = self.productList.item(7, 3)
        item.setText(_translate("Dialog", "₱15.00"))
        item = self.productList.item(8, 0)
        item.setText(_translate("Dialog", "Decolgen"))
        item = self.productList.item(8, 1)
        item.setText(_translate("Dialog", "2"))
        item = self.productList.item(8, 2)
        item.setText(_translate("Dialog", "1"))
        item = self.productList.item(8, 3)
        item.setText(_translate("Dialog", "₱9.00"))
        self.productList.setSortingEnabled(__sortingEnabled)
        self.searchButton.setText(_translate("Dialog", "Search"))
        self.clearButton.setText(_translate("Dialog", "X"))
        self.searchByName.setText(_translate("Dialog", "Search Name"))
        self.searchByCategory.setText(_translate("Dialog", "Search Category"))

    def set_search_name(self):
        self.search_mode = 'name'
        if self.searchCombo:
            self.searchCombo.hide()
        self.searchField.show()
        self.searchField.setText("")

    def set_search_category(self):
        self.search_mode = 'category'
        self.searchField.hide()
        if not self.searchCombo:
            self.searchCombo = QtWidgets.QComboBox(self.searchField.parent())
            self.searchCombo.setGeometry(self.searchField.geometry())
            self.searchCombo.setStyleSheet("font-size:18pt")
            self.searchCombo.addItems(self.categories)
        self.searchCombo.show()
        self.searchCombo.setCurrentIndex(-1)  

    def clear_search(self):
        if self.search_mode == 'name':
            self.searchField.setText("")
        elif self.search_mode == 'category' and self.searchCombo:
            self.searchCombo.setCurrentIndex(-1)
        self.show_all_rows()

    def search_products(self):
        query = ""
        if self.search_mode == 'name':
            query = self.searchField.text().strip().lower()
            if not query:
                QMessageBox.warning(None, "Warning", "Please fill in the search field to search for a product.")
                return
            matching_rows = [row for name, row in self.product_rows.items() if query in name.lower()]
            if not matching_rows:
                QMessageBox.information(None, "No Results", "The searched product does not exist.")
                return
        elif self.search_mode == 'category':
            if not self.searchCombo or self.searchCombo.currentIndex() == -1:
                QMessageBox.warning(None, "Warning", "Please select a category to search for products.")
                return
            category = self.searchCombo.currentText()
            matching_rows = [self.product_rows[name] for name, cat in self.products.items() if cat == category]
        
        self.filter_table(matching_rows)

    def filter_table(self, matching_rows):
        for row in range(1, 9):  
            self.productList.setRowHidden(row, row not in matching_rows)

    def show_all_rows(self):
        for row in range(1, 9):
            self.productList.setRowHidden(row, False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
