import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton 
import serial
from pymata4 import pymata4

class MainDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Dialog")
        self.setGeometry(100, 100, 300, 200)

        # Set background picture and scale to fit the dialog size
        self.setStyleSheet("""
            QDialog {
            background-image: url('C:/Work Folder/CATERMATICS AB/Background picture 1.jpg');
            background-repeat: no-repeat;
            background-position: center;
            background-size: cover;
            }
        """)

        layout = QVBoxLayout()

        self.label = QLabel("Distance:")
        layout.addWidget(self.label)

        self.dist_textbox = QLineEdit(self)
        self.dist_textbox.setText("0")
        layout.addWidget(self.dist_textbox)

        self.update_button = QPushButton("Update", self)
        self.update_button.clicked.connect(self.update_distance)
        layout.addWidget(self.update_button)

        self.RedLED_button_ON = QPushButton("Red LED On", self)
        self.RedLED_button_ON.clicked.connect(self.RED_LED_ON)
        layout.addWidget(self.RedLED_button_ON)

        self.RedLED_button_OFF = QPushButton("Red LED Off", self)
        self.RedLED_button_OFF.clicked.connect(self.RED_LED_OFF)
        layout.addWidget(self.RedLED_button_OFF)

        self.setLayout(layout)

        # Initialize the Pymata4 board
        self.board = pymata4.Pymata4()

        # Set up the ultrasonic sensor
        self.trigger_pin = 10
        self.echo_pin = 11
        self.LED_pin = 12
        self.board.set_pin_mode_sonar(self.trigger_pin, self.echo_pin, self.callback)
        self.board.set_pin_mode_digital_output(self.LED_pin)

        self.distance = 0

    def callback(self, data):
        self.distance = data[2]

    def update_distance(self):
        # Measure the distance using the ultrasonic sensor
        self.board.sonar_read(self.trigger_pin)
        self.dist_textbox.setText(str(self.distance))
        print(f"Distance updated to: {self.distance}")

    def RED_LED_ON(self):
        self.board.digital_write(self.LED_pin, 1)
        print("Red LED ON")

    def RED_LED_OFF(self):
        self.board.digital_write(self.LED_pin, 0)
        print("Red LED OFF", self.board.digital_read(2))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MainDialog()
    dialog.show()
    sys.exit(app.exec_())


