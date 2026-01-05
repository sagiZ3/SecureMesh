from PySide6.QtWidgets import QLabel

class StatusPill(QLabel):
    def __init__(self, text: str, object_name: str, parent=None):
        super().__init__(text, parent)
        self.setObjectName(object_name)
