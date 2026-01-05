# ui/logo.py
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import Qt


class LogoWatermark(QLabel):
    def __init__(self, parent=None, path: str = "assets/SecureMesh_logo.png"):
        super().__init__(parent)
        self._pix = QPixmap(path)
        self._opacity = 0.25
        self._desired_size = 220
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setFixedSize(self._desired_size, self._desired_size)

    def setOpacity(self, value: float):
        self._opacity = max(0.0, min(1.0, value))
        self.update()

    def paintEvent(self, event):
        if self._pix.isNull():
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setOpacity(self._opacity)

        scaled = self._pix.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        x = (self.width() - scaled.width()) // 2
        y = (self.height() - scaled.height()) // 2
        painter.drawPixmap(x, y, scaled)

        painter.end()
