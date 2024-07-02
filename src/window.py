from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QListWidget, QApplication, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from dbanalyzer import draw_graph, get_names
import sys

class ItemList(QListWidget):
    def __init__(self):
        super().__init__()
        self.populate_list()

        font = QFont()
        font.setPointSize(18)
        self.setFont(font)
        self.itemClicked.connect(self.on_click)

    def populate_list(self):
        names = get_names()
        for item in names:
            list_item = QListWidgetItem(item)
            self.addItem(list_item)

    def on_click(self, item):
        name = item.text()
        draw_graph(name)

    def filter_list(self, text):
        for index in range(self.count()):
            item = self.item(index)
            item.setHidden(text.lower() not in item.text().lower())


class Screen(QMainWindow):
    def __init__(self):
        super().__init__()

        with open("Diffnes.qss", "r") as file:
            self.setStyleSheet(file.read())

        self.setWindowTitle("Product list")
        self.resize(1280, 720)

        # Create central widget and layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        
        # Create search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.setStyleSheet(
            "QLineEdit {"
            "   border: 2px solid #2196F3;"
            "   border-radius: 10px;"
            "   padding: 8px;"
            "   font-size: 20px;"
            "}"
            "QLineEdit:focus {"
            "   border-color: #FF9800;"
            "}"
        )
        self.search_bar.setAlignment(Qt.AlignCenter)  # Center-align text
        self.search_bar.textChanged.connect(self.filter_list)
        self.layout.addWidget(self.search_bar)
        
        # Create QListWidget
        self.item_list = ItemList()
        self.layout.addWidget(self.item_list)
        self.setCentralWidget(self.central_widget)

    def showEvent(self, event):
        super().showEvent(event)
        # Set focus to another widget when the window is first shown
        self.item_list.setFocus()
    
    def filter_list(self, text):
        self.item_list.filter_list(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Screen()
    widget.show()
    app.exec()

