import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget
from PySide6.QtCore import Qt

from ui.style import STYLE_SHEET
from ui.background import BackgroundLayer
from pages.server_dashboard import ServerDashboardPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SecureMesh – Server GUI")
        self.resize(1300, 760)

        central = QWidget()
        self.setCentralWidget(central)
        central.setStyleSheet("background: transparent;")

        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Top bar
        top = QHBoxLayout()
        top.setContentsMargins(12, 8, 12, 8)
        title = QLabel("SecureMesh Server")
        title.setObjectName("appTitle")
        top.addWidget(title)
        top.addStretch(1)
        root.addLayout(top)

        # Stack (כרגע מסך יחיד)
        self.stack = QStackedWidget()
        root.addWidget(self.stack)

        self.dashboard = ServerDashboardPage()
        self.stack.addWidget(self.dashboard)

        # Background under everything
        self.bg = BackgroundLayer(self)
        self.bg.lower()

        # Hook background switching button
        self.dashboard.switch_bg_btn.clicked.connect(self.bg.next_background)

        self.setStyleSheet(STYLE_SHEET)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.bg.resize(self.size())

def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
