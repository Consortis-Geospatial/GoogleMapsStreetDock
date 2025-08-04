from qgis.PyQt.QtWidgets import QAction, QDockWidget, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from qgis.PyQt.QtCore import QUrl, Qt
from qgis.gui import QgsMapTool
from qgis.core import QgsPointXY, QgsCoordinateTransform, QgsCoordinateReferenceSystem
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
import os


class MapClickTool(QgsMapTool):
    def __init__(self, canvas, callback):
        super().__init__(canvas)
        self.canvas = canvas
        self.callback = callback

    def canvasReleaseEvent(self, event):
        point = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())
        self.callback(point)


class GoogleMapsStreetDock:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.click_tool = None
        self.dock = None
        self.browser = None
        self.btn_map = None
        self.btn_street = None

    def initGui(self):
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        self.action = QAction(QIcon(icon_path), "Open Google Maps/Street on Click", self.iface.mainWindow())
        self.action.triggered.connect(self.activate_plugin)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Google Maps/Street Dock", self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("&Google Maps/Street Dock", self.action)
        if self.dock:
            self.iface.removeDockWidget(self.dock)
            self.dock = None

    def activate_plugin(self):
        self.click_tool = MapClickTool(self.canvas, self.open_in_google_maps)
        self.canvas.setMapTool(self.click_tool)

        if not self.dock:
            self.dock = QDockWidget("Google Maps/Street Dock Viewer", self.iface.mainWindow())
            self.dock.setObjectName("GoogleMapsStreetDockViewer")
            self.dock.closeEvent = self.handle_dock_close

            main_widget = QWidget()
            main_layout = QVBoxLayout()
            main_widget.setLayout(main_layout)

            # Buttons
            btn_layout = QHBoxLayout()
            self.btn_map = QPushButton("Switch to Map View")
            self.btn_map.setEnabled(True)
            self.btn_map.clicked.connect(self.switch_to_map_view)

            self.btn_street = QPushButton("Switch to Street View")
            self.btn_street.setEnabled(False)
            self.btn_street.clicked.connect(self.switch_to_street_view)

            btn_layout.addWidget(self.btn_map)
            btn_layout.addWidget(self.btn_street)
            main_layout.addLayout(btn_layout)

            # Instruction label
            label = QLabel("Press CTRL + mouse wheel up/down to adjust the zoom level of the panel")
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size: 10pt; margin: 0; padding: 0;")
            label.setFixedHeight(20)
            main_layout.addWidget(label)

            # Web view
            self.browser = QWebEngineView()
            main_layout.addWidget(self.browser, stretch=1)

            self.dock.setWidget(main_widget)
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)
            self.dock.show()

    def handle_dock_close(self, event):
        self.dock = None
        event.accept()

    def open_in_google_maps(self, point: QgsPointXY):
        crs_src = self.canvas.mapSettings().destinationCrs()
        crs_dest = QgsCoordinateReferenceSystem.fromEpsgId(4326)
        transform = QgsCoordinateTransform(crs_src, crs_dest, self.canvas.mapSettings().transformContext())
        wgs84_point = transform.transform(point)
        lat, lon = wgs84_point.y(), wgs84_point.x()

        url = f"https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={lat},{lon}"
        if self.browser:
            self.browser.setUrl(QUrl(url))

        if self.btn_map and self.btn_street:
            self.btn_map.setEnabled(True)
            self.btn_street.setEnabled(False)

    def switch_to_map_view(self):
        if not self.browser:
            return
        url = self.browser.url().toString()
        lat, lon = self._extract_coords_from_url(url)
        if lat is None or lon is None:
            return
        map_url = f"https://www.google.com/maps?q={lat},{lon}"
        self.browser.setUrl(QUrl(map_url))
        self.btn_map.setEnabled(False)
        self.btn_street.setEnabled(True)

    def switch_to_street_view(self):
        if not self.browser:
            return
        url = self.browser.url().toString()
        lat, lon = self._extract_coords_from_url(url)
        if lat is None or lon is None:
            return
        street_url = f"https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={lat},{lon}"
        self.browser.setUrl(QUrl(street_url))
        self.btn_map.setEnabled(True)
        self.btn_street.setEnabled(False)

    def _extract_coords_from_url(self, url):
        from urllib.parse import urlparse, parse_qs
        parsed = urlparse(url)
        query = parse_qs(parsed.query)
        lat = lon = None

        if "q" in query:
            try:
                coords = query["q"][0].split(",")
                lat = float(coords[0])
                lon = float(coords[1])
            except Exception:
                pass
        elif "viewpoint" in query:
            try:
                coords = query["viewpoint"][0].split(",")
                lat = float(coords[0])
                lon = float(coords[1])
            except Exception:
                pass
        else:
            parts = parsed.path.split("@")
            if len(parts) > 1:
                coords_str = parts[1].split(",")
                try:
                    lat = float(coords_str[0])
                    lon = float(coords_str[1])
                except Exception:
                    pass
        return lat, lon
