# GoogleMapsDockPlugin
**GoogleMapsDockPlugin** is a QGIS plugin that integrates Google Maps into a dockable browser panel. By clicking on the QGIS map canvas, users can instantly center the Google Maps view at the selected location. The panel also supports full Street View navigation, enabling detailed exploration and precise digitization of road networks using high-resolution imagery.

---

## Features

- Click any point on the QGIS map canvas to open Google Maps in a dockable panel.
- Navigate Google Maps and access Street View within the panel, replicating a standard browser experience.
- Automatically transforms clicked coordinates to WGS84 (EPSG:4326) for accurate positioning.
- Seamless integration with QGIS toolbar and plugin menu for quick activation.
- Renders Google Maps using a `QWebEngineView` within a QGIS dock widget.

---

## How It Works

1. Activate the plugin via the toolbar icon or the "Google Maps Dock" menu.
2. Click a location on the QGIS map canvas to select a point.
3. The plugin converts the clicked coordinates to WGS84.
4. A dockable panel opens (or updates) with Google Maps centered at the clicked location.
5. Use the Google Maps interface in the panel to explore Street View for detailed road network digitization.

---

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/Consortis-Geospatial/GoogleMapsDock.git
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
- Employs a custom `QgsMapTool` to capture map clicks and transform coordinates.
- Uses `QWebEngineView` to render Google Maps and Street View within the QGIS interface.
- Coordinates are transformed to EPSG:4326 (WGS84) for compatibility with Google Maps.

---

## Dependencies

- **QGIS 3.x**: Compatible with QGIS version 3.x (tested with 3.38.3), providing the core GIS functionality and PyQGIS API.
- **Python 3**: QGIS 3.38.3 includes an embedded Python 3.12 interpreter. Other QGIS 3.x versions may use Python 3.7 or higher.
- **PyQt5**: Required for GUI components like `QAction`, `QDockWidget`, and `QWebEngineView`. Bundled with QGIS 3.x installations (version 5.15.10 or similar).
- **PyQtWebEngine**: Provides the `QtWebEngineWidgets` module for rendering web content via `QWebEngineView`. Must be installed manually (as shown above) if not included in your QGIS setup:
  - Installs `PyQtWebEngine` (e.g., version 5.15.7) and `PyQtWebEngine-Qt5` (e.g., version 5.15.2).
  - On **Linux**, ensure `qt5-webengine` or `libqt5webengine` is installed (e.g., `sudo apt install qt5-webengine` on Ubuntu).
  - On **Windows**, installed via `pip` as shown in the setup steps.
  - On **macOS**, typically bundled with QGIS, but verify WebEngine support in your QGIS build.
- **PyQt5-sip**: A dependency of `PyQtWebEngine`, usually included with QGIS (version 12.13.0 or higher).

---

## License
This plugin is released under the GPL-3.0 license.
