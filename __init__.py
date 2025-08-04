import platform
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from qgis.core import QgsMessageLog, Qgis

def show_pyqtwebengine_install_help():
    url = "https://github.com/Consortis-Geospatial/GoogleMapsStreetDock"
    system = platform.system()

    if system == "Windows":
        msg = (
            "<b>Missing required module: PyQtWebEngine</b><br><br>"
            "To install it:<br>"
            "1. Close QGIS.<br>"
            "2. Open the OSGeo4W Shell (from Start Menu).<br>"
            "3. Run the command:<br><code>python3 -m pip install PyQtWebEngine</code><br>"
            "4. Restart QGIS.<br><br>"
            f"<a href='{url}'>Visit the installation guide</a>"
        )
    elif system == "Linux":
        msg = (
            "<b>Missing required module: PyQtWebEngine</b><br><br>"
            "Run in terminal:<br>"
            "<code>sudo apt install python3-pyqt5.qtwebengine</code><br><br>"
            "Or with pip:<br>"
            "<code>python3 -m pip install PyQtWebEngine</code><br><br>"
            f"<a href='{url}'>Visit the installation guide</a>"
        )
    elif system == "Darwin":
        msg = (
            "<b>Missing required module: PyQtWebEngine</b><br><br>"
            "On macOS, reinstall QGIS from:<br>"
            "<a href='https://www.qgis.org/en/site/forusers/download.html'>QGIS official website</a><br><br>"
            f"<a href='{url}'>Visit the plugin help page</a>"
        )
    else:
        msg = (
            "<b>Missing required module: PyQtWebEngine</b><br><br>"
            "Run:<br><code>python3 -m pip install PyQtWebEngine</code><br><br>"
            f"<a href='{url}'>Visit the installation guide</a>"
        )

    # Log it to QGIS log panel
    QgsMessageLog.logMessage(
        msg.replace("<br>", "\n").replace("<code>", "").replace("</code>", ""),
        "GoogleMapsStreetDock",
        Qgis.Critical
    )

    # Show custom dialog with clickable link
    dlg = QDialog()
    dlg.setWindowTitle("GoogleMapsStreetDock - Missing Dependency")
    dlg.setMinimumWidth(500)

    layout = QVBoxLayout()
    label = QLabel(msg)
    label.setOpenExternalLinks(True)
    label.setWordWrap(True)
    layout.addWidget(label)

    btn = QPushButton("Close")
    btn.clicked.connect(dlg.accept)
    layout.addWidget(btn, alignment=Qt.AlignRight)

    dlg.setLayout(layout)
    dlg.exec_()

def check_dependencies():
    try:
        from PyQt5.QtWebEngineWidgets import QWebEngineView
    except ImportError:
        show_pyqtwebengine_install_help()
        return False
    return True

def classFactory(iface):
    if not check_dependencies():
        return None
    from .main import GoogleMapsStreetDock
    return GoogleMapsStreetDock(iface)
