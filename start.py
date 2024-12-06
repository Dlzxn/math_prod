import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

app=QApplication(sys.argv)

main_menu=QWidget()
main_menu.setWindowTitle("МАТРИЦА ПО-РУССКИ")
main_menu.setGeometry(500, 500, 1000, 1000)
main_menu.setMinimumSize(1000, 500)
main_menu.setStyleSheet("""
    color: black;              /* Цвет текста */
    background-color: gray; /* Цвет фона */
""")

font = QFont("Arial", 24)  # Шрифт Arial, размер 24
__text=QLabel("Решение матриц", parent=main_menu)
__text.move(350, 20)
__text.setFont(font)

button_start=QPushButton("Нажми для перехода", main_menu)
button_start.setGeometry(400, 70, 100, 50)


# layout=QVBoxLayout()
# layout.addWidget(__text)

# main_menu.setLayout(layout)
main_menu.show()


sys.exit(app.exec())