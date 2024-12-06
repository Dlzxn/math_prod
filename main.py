import sys
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QButtonGroup, QPushButton, QTextEdit
from PyQt6.QtGui import QFont

app = QApplication(sys.argv)

window=QWidget()
window.setWindowTitle("Math Prog")
window.setGeometry(400, 700, 500, 500) 

label=QLabel("Решение матриц", parent=window)
label.move(50, 40)

font = QFont("Arial", 24)  # Шрифт Arial, размер 24
font.setBold(True)  # Сделать текст жирным
label.setFont(font)
label.setStyleSheet("color: black;")  # Устанавливаем синий цвет текста
label.setStyleSheet("""
    color: red;              /* Цвет текста */
    background-color: yellow; /* Цвет фона */
    border: 2px solid black;  /* Черная рамка вокруг текста */
""")
layout = QVBoxLayout()


def on_button_click():
    def get_text():
        print(text.toPlainText())

    fram=QWidget()
    fram.setWindowTitle("Dev")
    fram.show()
    fram.setGeometry(100, 200, 300, 400)
    print("ffffff____")
    text=QTextEdit()
    text.setPlaceholderText("GHBBFB")
    layout.addWidget(text)
    window.setLayout(layout)
    button=QPushButton("Get")
    button.clicked.connect(get_text)
    layout.addWidget(button)



# layout = QHBoxLayout()

# label1 = QLabel("Label 1")
# label2 = QLabel("Label 2")
# label3 = QLabel("Label 3")

# layout.addWidget(label1)
# layout.addWidget(label2)
# layout.addWidget(label3)

# Создание кнопки
button = QPushButton("Click Me", window)
button.setGeometry(100, 100, 200, 40)

# Связь сигнала с функцией
button.clicked.connect(on_button_click)

# window.setLayout(layout)

window.show()

sys.exit(app.exec())