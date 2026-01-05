STYLE_SHEET = """
QWidget {
    background-color: #050814;
    color: #e7f0ff;
    font-family: 'Segoe UI', 'Rubik', sans-serif;
}

#appTitle {
    font-size: 20px;
    font-weight: 600;
    padding: 10px 16px;
    color: #f7c948;
    text-shadow: 0 0 10px #f7c948;
}
#pageTitle {
    font-size: 18px;
    font-weight: 600;
    color: #52b6ff;
    text-shadow: 0 0 12px #1e6fff;
}
#pageSubtitle {
    color: #a7b3d5;
    margin-bottom: 6px;
}

#card {
    background-color: rgba(5, 10, 30, 0.92);
    border-radius: 16px;
    border: 1px solid #1b3358;
}
#cardTitle {
    font-size: 14px;
    font-weight: 600;
    color: #f7f9ff;
}

#switchBgButton {
    background-color: transparent;
    border-radius: 999px;
    border: 1px solid #52b6ff;
    padding: 6px 12px;
    color: #52b6ff;
    font-size: 11px;
}
#switchBgButton:hover {
    background-color: rgba(16, 48, 96, 0.7);
}

#pillOk {
    background-color: #00d1a3;
    color: #050814;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
}
#pillWarn {
    background-color: #f7c948;
    color: #050814;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
}
#pillBad {
    background-color: #ff7675;
    color: #050814;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 700;
}

QLineEdit, QComboBox {
    background-color: rgba(3, 6, 18, 0.9);
    border: 1px solid #2a3c5f;
    border-radius: 8px;
    padding: 6px 8px;
}
QLineEdit:focus, QComboBox:focus {
    border: 1px solid #52b6ff;
}

QTableWidget {
    background-color: rgba(2, 6, 25, 0.75);
    border: 1px solid #283458;
    border-radius: 10px;
    gridline-color: #283458;
}
QHeaderView::section {
    background-color: rgba(10, 20, 50, 0.9);
    padding: 6px;
    border: none;
    color: #cfe3ff;
    font-weight: 600;
}
QTableWidget::item {
    padding: 6px;
}
QTableWidget::item:selected {
    background-color: rgba(82, 182, 255, 0.25);
}

#logView {
    background-color: rgba(2, 6, 25, 0.85);
    border-radius: 10px;
    border: 1px solid #283458;
}

#metricValue {
    font-size: 20px;
    font-weight: 800;
    color: #f7c948;
    text-align: center;
}
#metricLabel {
    font-size: 12px;
    color: #cbd4ff;
}
"""
