import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QLabel, QComboBox, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QWidget
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class ProductFilterForm(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Filter")
        self.setGeometry(200, 100, 540, 500)

        # Title
        self.title_label = QLabel("Product Filter")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))

        # Category Dropdown
        self.category_label = QLabel("Category")
        self.category_label.setAlignment(Qt.AlignCenter)
        self.category_label.setFont(QFont("Arial", 14, QFont.Bold))

        self.category_combo = QComboBox()
        self.category_combo.addItems([
            "", "Analgesics", "Antibiotics", "Antidepressants",
            "Antihistamines", "Antihypertensives"
        ])


        self.stock_label = QLabel("Stock Status")
        self.stock_label.setAlignment(Qt.AlignCenter)
        self.stock_label.setFont(QFont("Arial", 14, QFont.Bold))

        self.stock_combo = QComboBox()
        self.stock_combo.addItems([
            "", "Low Stock", "Out of Stock", "In Stock"
        ])


        self.exp_label = QLabel("Exp. Status")
        self.exp_label.setAlignment(Qt.AlignCenter)
        self.exp_label.setFont(QFont("Arial", 14, QFont.Bold))

        self.exp_combo = QComboBox()
        self.exp_combo.addItems([
            "", "Expiring Soon", "Expired", "Valid"
        ])

        # Buttons
        self.apply_button = QPushButton("Apply Filter")
        self.apply_button.setStyleSheet("background-color: #28a745; color: white; font-weight: bold;")
        self.apply_button.clicked.connect(self.apply_filter)

        self.clear_button = QPushButton("Clear Filter")
        self.clear_button.clicked.connect(self.clear_filter)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)

        form_layout = QVBoxLayout()
        form_layout.addWidget(self.category_label)
        form_layout.addWidget(self.category_combo)
        form_layout.addWidget(self.stock_label)
        form_layout.addWidget(self.stock_combo)
        form_layout.addWidget(self.exp_label)
        form_layout.addWidget(self.exp_combo)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.clear_button)
        button_layout.addWidget(self.apply_button)

        layout.addLayout(form_layout)
        layout.addStretch()
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setLayout(layout)

    def apply_filter(self):
        """Handles validation and simulates filter checking."""
        category = self.category_combo.currentText()
        stock = self.stock_combo.currentText()
        exp = self.exp_combo.currentText()


        if not category and not stock and not exp:
            QMessageBox.warning(self, "Validation Error", "Please select at least one filter option.")
            return

        fake_data = [
            {"category": "Analgesics", "stock": "Low Stock", "exp": "Valid"},
            {"category": "Antibiotics", "stock": "In Stock", "exp": "Expiring Soon"},
        ]

        filtered = [
            item for item in fake_data
            if (not category or item["category"] == category)
            and (not stock or item["stock"] == stock)
            and (not exp or item["exp"] == exp)
        ]

        if not filtered:
            QMessageBox.information(self, "No Results", "No products match the selected filters.")
        else:
            QMessageBox.information(
                self, "Filter Applied",
                f"{len(filtered)} product(s) found matching the filter."
            )

    def clear_filter(self):
        """Resets dropdowns."""
        self.category_combo.setCurrentIndex(0)
        self.stock_combo.setCurrentIndex(0)
        self.exp_combo.setCurrentIndex(0)
        QMessageBox.information(self, "Filters Cleared", "All filters have been reset.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductFilterForm()
    window.show()
    sys.exit(app.exec_())
