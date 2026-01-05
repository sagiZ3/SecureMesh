from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QGridLayout,
    QTableWidget, QTableWidgetItem, QTextEdit, QLineEdit, QComboBox
)
from PySide6.QtCore import Qt, QTimer
import random
import datetime

from src.securemesh.server.gui.widgets.card_frame import CardFrame
from src.securemesh.server.gui.widgets.status_pill import StatusPill

class ServerDashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        root = QVBoxLayout(self)
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(12)

        # Header
        header = QHBoxLayout()
        title = QLabel("SecureMesh – Server Control Center")
        title.setObjectName("pageTitle")

        self.switch_bg_btn = QPushButton("Change Background")
        self.switch_bg_btn.setObjectName("switchBgButton")

        self.api_pill = StatusPill("API: UP", "pillOk")
        self.db_pill = StatusPill("DB: OK", "pillOk")

        header.addWidget(title)
        header.addStretch(1)
        header.addWidget(self.switch_bg_btn)
        header.addWidget(self.api_pill)
        header.addWidget(self.db_pill)
        root.addLayout(header)

        subtitle = QLabel("ניהול לקוחות, אירועי אבטחה, Correlation IDS, לוגים וסטטוס שירותים.")
        subtitle.setObjectName("pageSubtitle")
        root.addWidget(subtitle)

        grid = QGridLayout()
        grid.setSpacing(10)

        # Clients card
        clients_card = CardFrame("לקוחות מחוברים")
        self.clients_table = QTableWidget(0, 5)
        self.clients_table.setHorizontalHeaderLabels(["Client ID", "IP", "Status", "Last Seen", "Events"])
        self.clients_table.horizontalHeader().setStretchLastSection(True)
        clients_card.content_layout.addWidget(self._clients_filter_row())
        clients_card.content_layout.addWidget(self.clients_table)

        # Events feed card
        events_card = CardFrame("אירועי אבטחה נכנסים")
        self.events_log = QTextEdit()
        self.events_log.setReadOnly(True)
        self.events_log.setObjectName("logView")
        events_card.content_layout.addWidget(self._events_filter_row())
        events_card.content_layout.addWidget(self.events_log)

        # Correlation card
        corr_card = CardFrame("Correlation IDS")
        self.corr_table = QTableWidget(0, 4)
        self.corr_table.setHorizontalHeaderLabels(["Signature", "Clients", "Window", "Severity"])
        self.corr_table.horizontalHeader().setStretchLastSection(True)
        corr_card.content_layout.addWidget(self.corr_table)

        # Metrics row
        metrics = QHBoxLayout()
        metrics.setSpacing(10)
        self.metric_clients = self._metric_card("Connected Clients", "0")
        self.metric_events = self._metric_card("Events (last 5m)", "0")
        self.metric_corr = self._metric_card("Correlated Alerts", "0")
        self.metric_rules = self._metric_card("Active Rules", "0")
        metrics.addWidget(self.metric_clients)
        metrics.addWidget(self.metric_events)
        metrics.addWidget(self.metric_corr)
        metrics.addWidget(self.metric_rules)
        metrics_container = QWidget()
        metrics_container.setLayout(metrics)

        # Storage/API card
        services_card = CardFrame("שירותים: API / Storage")
        self.services_log = QTextEdit()
        self.services_log.setReadOnly(True)
        self.services_log.setObjectName("logView")
        self.services_log.setMaximumHeight(140)
        services_card.content_layout.addWidget(self.services_log)

        # Layout placement
        grid.addWidget(clients_card, 0, 0, 2, 2)
        grid.addWidget(events_card, 0, 2, 2, 2)
        grid.addWidget(corr_card, 2, 0, 1, 2)
        grid.addWidget(services_card, 2, 2, 1, 2)
        grid.addWidget(metrics_container, 3, 0, 1, 4)
        root.addLayout(grid)

        # Demo state
        self._init_demo()

    def _clients_filter_row(self) -> QWidget:
        row = QWidget()
        lay = QHBoxLayout(row)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(8)

        self.client_search = QLineEdit()
        self.client_search.setPlaceholderText("חפש Client ID / IP")
        self.client_status_filter = QComboBox()
        self.client_status_filter.addItems(["All", "Connected", "Warning", "Offline"])

        lay.addWidget(QLabel("Filter:"))
        lay.addWidget(self.client_search, 2)
        lay.addWidget(self.client_status_filter, 1)
        return row

    def _events_filter_row(self) -> QWidget:
        row = QWidget()
        lay = QHBoxLayout(row)
        lay.setContentsMargins(0, 0, 0, 0)
        lay.setSpacing(8)

        self.sev_filter = QComboBox()
        self.sev_filter.addItems(["All", "Low", "Medium", "High", "Critical"])

        lay.addWidget(QLabel("Severity:"))
        lay.addWidget(self.sev_filter)
        lay.addStretch(1)
        return row

    def _metric_card(self, title: str, value: str) -> QWidget:
        card = CardFrame(title)
        v = QLabel(value)
        v.setObjectName("metricValue")
        v.setAlignment(Qt.AlignCenter)
        card.content_layout.addWidget(v)
        card.value_label = v
        card.setMinimumHeight(80)
        return card

    def _init_demo(self):
        self._clients = {}
        self._events_last_5m = 0
        self._corr_alerts = 0
        self._active_rules = 14  # דמו

        self.metric_rules.value_label.setText(str(self._active_rules))

        self.timer = QTimer(self)
        self.timer.setInterval(900)
        self.timer.timeout.connect(self._tick)
        self.timer.start()

        self.services_log.append("[Server] API service started.")
        self.services_log.append("[Server] Storage connected (SQLite/PostgreSQL placeholder).")

    def _tick(self):
        # Add/update clients
        if random.random() < 0.45 or len(self._clients) < 3:
            cid = f"client-{random.randint(1, 12):02d}"
            ip = f"192.168.1.{random.randint(2, 254)}"
            self._clients.setdefault(cid, {"ip": ip, "status": "Connected", "events": 0})
            # random status variation
            if random.random() < 0.08:
                self._clients[cid]["status"] = "Warning"
            elif random.random() < 0.04:
                self._clients[cid]["status"] = "Offline"
            else:
                self._clients[cid]["status"] = "Connected"

        # Incoming event (simulate)
        if random.random() < 0.7 and self._clients:
            cid = random.choice(list(self._clients.keys()))
            sev = random.choices(["Low", "Medium", "High", "Critical"], weights=[50, 30, 15, 5])[0]
            sig = random.choice(["ARP_SPOOF", "SYN_FLOOD", "DNS_SPOOF", "PORT_SCAN", "MITM_PATTERN"])
            now = datetime.datetime.now().strftime("%H:%M:%S")
            msg = f"[{now}] {cid} | {sig} | Severity={sev}"
            self.events_log.append(msg)

            self._clients[cid]["events"] += 1
            self._events_last_5m += 1

            # Correlation rule: if same signature appears from 2+ clients in short time (demo)
            if sev in ("High", "Critical") and random.random() < 0.35:
                self._corr_alerts += 1
                self._add_corr_row(sig, clients=random.randint(2, min(6, len(self._clients))), window="60s", severity=sev)
                self.services_log.append(f"[Correlation] Alert created for {sig} ({sev}).")

        # Update service pills (demo)
        if random.random() < 0.03:
            self.api_pill.setText("API: DEGRADED")
            self.api_pill.setObjectName("pillWarn")
            self.api_pill.style().unpolish(self.api_pill)
            self.api_pill.style().polish(self.api_pill)
        elif random.random() < 0.02:
            self.db_pill.setText("DB: WARN")
            self.db_pill.setObjectName("pillWarn")
            self.db_pill.style().unpolish(self.db_pill)
            self.db_pill.style().polish(self.db_pill)
        else:
            self.api_pill.setText("API: UP")
            self.api_pill.setObjectName("pillOk")
            self.api_pill.style().unpolish(self.api_pill)
            self.api_pill.style().polish(self.api_pill)

            self.db_pill.setText("DB: OK")
            self.db_pill.setObjectName("pillOk")
            self.db_pill.style().unpolish(self.db_pill)
            self.db_pill.style().polish(self.db_pill)

        # Refresh tables + metrics
        self._refresh_clients_table()
        self.metric_clients.value_label.setText(str(len(self._clients)))
        self.metric_events.value_label.setText(str(self._events_last_5m))
        self.metric_corr.value_label.setText(str(self._corr_alerts))

    def _refresh_clients_table(self):
        # basic filters (demo)
        q = (self.client_search.text() or "").strip().lower()
        status = self.client_status_filter.currentText()

        rows = []
        for cid, info in self._clients.items():
            if q and q not in cid.lower() and q not in info["ip"]:
                continue
            if status != "All":
                want = status
                if info["status"] != want:
                    continue
            rows.append((cid, info))

        self.clients_table.setRowCount(len(rows))
        now = datetime.datetime.now().strftime("%H:%M:%S")

        for r, (cid, info) in enumerate(rows):
            self.clients_table.setItem(r, 0, QTableWidgetItem(cid))
            self.clients_table.setItem(r, 1, QTableWidgetItem(info["ip"]))
            self.clients_table.setItem(r, 2, QTableWidgetItem(info["status"]))
            self.clients_table.setItem(r, 3, QTableWidgetItem(now))
            self.clients_table.setItem(r, 4, QTableWidgetItem(str(info["events"])))

    def _add_corr_row(self, signature: str, clients: int, window: str, severity: str):
        r = self.corr_table.rowCount()
        self.corr_table.insertRow(r)
        self.corr_table.setItem(r, 0, QTableWidgetItem(signature))
        self.corr_table.setItem(r, 1, QTableWidgetItem(str(clients)))
        self.corr_table.setItem(r, 2, QTableWidgetItem(window))
        self.corr_table.setItem(r, 3, QTableWidgetItem(severity))
