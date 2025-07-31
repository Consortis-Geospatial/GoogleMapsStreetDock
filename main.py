from qgis.PyQt.QtWidgets import QAction, QDockWidget
from qgis.gui import QgsMapTool
from qgis.core import QgsPointXY, QgsCoordinateTransform, QgsCoordinateReferenceSystem
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os
from PyQt5.QtGui import QIcon

class MapClickTool(QgsMapTool):
    def __init__(self, canvas, callback):
        super().__init__(canvas)
        self.canvas = canvas
        self.callback = callback

    def canvasReleaseEvent(self, event):
        point = self.canvas.getCoordinateTransform().toMapCoordinates(event.pos().x(), event.pos().y())
        print(f"Map clicked at: {point}")  # Debug
        self.callback(point)

class GoogleMapsDockPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = iface.mapCanvas()
        self.click_tool = None
        self.dock = None
        self.browser = None

    def initGui(self):
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        self.action = QAction(QIcon(icon_path), "Open Google Maps on Click", self.iface.mainWindow())
        self.action.triggered.connect(self.activate_plugin)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Google Maps Dock", self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("&Google Maps Dock", self.action)
        if self.dock:
            self.iface.removeDockWidget(self.dock)

    def activate_plugin(self):
        print("Activating Google Maps click tool")  # Debug
        self.click_tool = MapClickTool(self.canvas, self.open_in_google_maps)
        self.canvas.setMapTool(self.click_tool)

        if not self.dock:
            self.dock = QDockWidget("Google Maps Viewer", self.iface.mainWindow())
            self.browser = QWebEngineView()
            self.dock.setWidget(self.browser)
            self.iface.addDockWidget(0x1, self.dock)  # Left dock area
            self.dock.show()

    def open_in_google_maps(self, point: QgsPointXY):
        print(f"Transforming point: {point}")  # Debug
        crs_src = self.canvas.mapSettings().destinationCrs()
        crs_dest = QgsCoordinateReferenceSystem.fromEpsgId(4326)  # WGS84 new style
        transform = QgsCoordinateTransform(crs_src, crs_dest, self.canvas.mapSettings().transformContext())
        wgs84_point = transform.transform(point)
        lat, lon = wgs84_point.y(), wgs84_point.x()
        print(f"Opening Google Maps at: {lat}, {lon}")  # Debug
        url = f"https://www.google.com/maps?q={lat},{lon}"
        if self.browser:
            self.browser.setUrl(QUrl(url))
