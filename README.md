<div align=center>
   <img width="64" height="64" alt="icon" src="https://github.com/user-attachments/assets/c220569a-0c2f-4e68-90c5-c0409859434c" />
</div>

# GoogleMapsStreetDock
**GoogleMapsStreetDock** is a QGIS plugin that integrates Google Maps and Street View into a dockable browser panel. By clicking on the QGIS map canvas, users can instantly open Street View centered at the selected location, with options to switch to Map View. The panel supports full navigation, enabling detailed exploration and precise digitization of road networks using high-resolution imagery.

---

## Features

- Click any point on the QGIS map canvas to open Street View by default in a dockable panel.
- Switch between Google Maps and Street View using dedicated buttons in the panel.
- Provides a zoom instruction label ("Press CTRL + mouse wheel up/down to adjust the zoom level of the panel").
- Automatically transforms clicked coordinates to WGS84 (EPSG:4326) for accurate positioning.
- Seamless integration with QGIS toolbar and plugin menu for quick activation.
- Renders Google Maps and Street View using a `QWebEngineView` within a QGIS dock widget.

---

## How It Works

1. Activate the plugin via the toolbar icon or the "Google Maps/Street Dock" menu.
2. Click a location on the QGIS map canvas to select a point.
3. The plugin converts the clicked coordinates to WGS84 and opens Street View in a dockable panel.
4. Use the "Switch to Map View" or "Switch to Street View" buttons to toggle views.
5. Adjust the panel’s zoom level with CTRL + mouse wheel, as indicated by the instruction label.
6. Navigate Street View or Map View for detailed road network digitization.

---

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/Consortis-Geospatial/GoogleMapsStreetDock.git
   ```
2. Copy the folder to your QGIS plugin directory:
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - Windows: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
3. Set up the required Python dependencies (see Dependencies section below).
4. Open QGIS and enable the plugin via Plugins > Manage and Install Plugins.

---

## Setting Up Dependencies (Windows)

To ensure the plugin runs correctly, particularly for the `QWebEngineView` component, follow these steps to install the required Python packages in the QGIS Python environment. These steps are tailored for QGIS 3.38.3 on Windows but may apply to other versions with slight modifications.

1. **Locate the QGIS Python Executable**:
   - Open the QGIS Python Console (Ctrl+Alt+P or via Plugins > Python Console).
   - Run the following commands to identify the Python executable and its path:
     ```python
     import sys
     print(sys.executable)
     print(sys.path)
     ```
   - Note the path to `python.exe` (e.g., `C:\Program Files\QGIS 3.38.3\apps\Python312\python.exe`).

2. **Open Command Prompt and Navigate to Python Directory**:
   - Open a Command Prompt as Administrator.
   - Navigate to the QGIS Python directory:
     ```cmd
     cd "C:\Program Files\QGIS 3.38.3\apps\Python312"
     ```

3. **Ensure pip is Available**:
   - Run the following command to ensure `pip` is installed:
     ```cmd
     python.exe -m ensurepip --default-pip
     ```

4. **Upgrade pip**:
   - Update `pip` to the latest version:
     ```cmd
     python.exe -m pip install --upgrade pip
     ```
   - If you encounter a PATH warning, consider adding `C:\Program Files\QGIS 3.38.3\apps\Python312\Scripts` to your system PATH or ignore it for one-time use.

5. **Install PyQtWebEngine**:
   - Install the `PyQtWebEngine` package, which includes `QtWebEngineWidgets`:
     ```cmd
     python.exe -m pip install PyQtWebEngine
     ```

6. **Verify Installation**:
   - Restart QGIS and activate the plugin. If errors occur, confirm that `PyQtWebEngine` and its dependencies (e.g., `PyQtWebEngine-Qt5`) are installed correctly by running:
     ```python
     import PyQt5.QtWebEngineWidgets
     ```
     in the QGIS Python Console.

---

## Screenshot
Coming Soon...

---

## Developer Notes

- Developed in Python using PyQt, PyQGIS, and QtWebEngine APIs.
- Uses a custom `QgsMapTool` to capture map clicks and transform coordinates.
- Employs `QWebEngineView` to render Google Maps and Street View within the QGIS interface.
- Coordinates are transformed to EPSG:4326 (WGS84) for compatibility with Google Maps.
- Includes buttons for toggling between Map and Street View, with URL parsing to maintain coordinates.
- Dock state is preserved using a unique `objectName`, and manual dock closure is handled gracefully.

---

## Dependencies

- **QGIS 3.x**: Compatible with QGIS version 3.x (tested with 3.38.3), providing the core GIS functionality and PyQGIS API.
- **Python 3**: QGIS 3.38.3 includes an embedded Python 3.12 interpreter. Other QGIS 3.x versions may use Python 3.7 or higher.
- **PyQt5**: Required for GUI components like `QAction`, `QDockWidget`, `QPushButton`, and `QWebEngineView`. Bundled with QGIS 3.x installations (version 5.15.10 or similar).
- **PyQtWebEngine**: Provides the `QtWebEngineWidgets` module for rendering web content via `QWebEngineView`. Must be installed manually (as shown above) if not included in your QGIS setup:
  - Installs `PyQtWebEngine` (e.g., version 5.15.7) and `PyQtWebEngine-Qt5` (e.g., version 5.15.2).
  - On **Linux**, ensure `qt5-webengine` or `libqt5webengine` is installed (e.g., `sudo apt install qt5-webengine` on Ubuntu).
  - On **Windows**, installed via `pip` as shown in the setup steps.
  - On **macOS**, typically bundled with QGIS, but verify WebEngine support in your QGIS build.
- **PyQt5-sip**: A dependency of `PyQtWebEngine`, usually included with QGIS (version 12.13.0 or higher).
- **urllib.parse**: Part of the Python standard library, used for parsing URLs to extract coordinates.

---

## Support and Contributions

- **Homepage**: [https://github.com/Consortis-Geospatial](https://github.com/Consortis-Geospatial)
- **Issue Tracker**: [https://github.com/Consortis-Geospatial/GoogleMapsStreetDock/issues](https://github.com/Consortis-Geospatial/GoogleMapsStreetDock/issues)
- **Author**: Gkaravelis Andreas - Consortis Geospatial
- **Email**: gkaravelis@consortis.gr
- **Repository**: [https://github.com/Consortis-Geospatial/GoogleMapsStreetDock](https://github.com/Consortis-Geospatial/GoogleMapsStreetDock)

---

## License
This plugin is released under the GPL-3.0 license.

<div align=center>
   <img width="64" height="64" alt="icon" src="https://github.com/user-attachments/assets/c220569a-0c2f-4e68-90c5-c0409859434c" />
</div>
