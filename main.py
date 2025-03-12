import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QRadioButton, QComboBox, QPushButton, QGroupBox, QFormLayout)
class UserRegistrationForm(QWidget):    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 2 - Layout - User Registration Form")
        self.setGeometry(100, 100, 400, 300)
        
        # Main vertical layout
        main_layout = QVBoxLayout()

        # Identitas
        identitas_group = QGroupBox("Identitas (vertical box layout)")
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel("Nama : I Gede Manik Ariyasa"))
        identitas_layout.addWidget(QLabel("NIM : F1D022046"))
        identitas_layout.addWidget(QLabel("Kelas : Pemrograman Visual D"))
        identitas_group.setLayout(identitas_layout)
        main_layout.addWidget(identitas_group)

        # Navigation 
        navigation_group = QGroupBox("Navigation (horizontal box layout)")
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(QPushButton("Home"))
        navigation_layout.addWidget(QPushButton("About"))
        navigation_layout.addWidget(QPushButton("Contact"))
        navigation_group.setLayout(navigation_layout)
        main_layout.addWidget(navigation_group)

        # User Registration 
        form_group = QGroupBox("User Registration (form layout)")
        form_layout = QFormLayout()

        form_layout.addRow(QLabel("Full Name:"), QLineEdit())
        form_layout.addRow(QLabel("Email:"), QLineEdit())
        form_layout.addRow(QLabel("Phone:"), QLineEdit())

        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")

        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)

        form_layout.addRow(QLabel("Gender:"), gender_layout)

        self.country_combo = QComboBox()
        self.country_combo.addItems(["Select Country", "Indonesia", "USA", "UK"])
        form_layout.addRow(QLabel("Country:"), self.country_combo)

        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        # Actions Section
        actions_group = QGroupBox("Actions (horizontal box layout)")
        actions_layout = QHBoxLayout()
        submit_button = QPushButton("Submit")
        cancel_button = QPushButton("Cancel")
        actions_layout.addWidget(submit_button)
        actions_layout.addWidget(cancel_button)
        actions_group.setLayout(actions_layout)
        main_layout.addWidget(actions_group)
        # main_layout.addLayout(actions_layout)

        # Set main layout
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserRegistrationForm()
    window.show()
    sys.exit(app.exec_())