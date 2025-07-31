--------------QGIS PYTHON CONSOLE------------
import sys
print(sys.executable)
print(sys.path)

---------------------CMD---------------------
C:\Program Files\QGIS 3.38.3\bin>cd "C:\PROGRA~1\QGIS33~1.3\apps\Python312"

C:\PROGRA~1\QGIS33~1.3\apps\Python312>python.exe -m ensurepip --default-pip
Looking in links: c:\Users\GKARAV~1\AppData\Local\Temp\tmpyj54ibtc
Requirement already satisfied: pip in c:\progra~1\qgis33~1.3\apps\python312\lib\site-packages (24.0)

C:\PROGRA~1\QGIS33~1.3\apps\Python312>python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\progra~1\qgis33~1.3\apps\python312\lib\site-packages (24.0)
Collecting pip
  Downloading pip-25.1.1-py3-none-any.whl.metadata (3.6 kB)
Downloading pip-25.1.1-py3-none-any.whl (1.8 MB)
   ---------------------------------------- 1.8/1.8 MB 7.8 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.0
    Uninstalling pip-24.0:
      Successfully uninstalled pip-24.0
  WARNING: The scripts pip.exe, pip3.12.exe and pip3.exe are installed in 'C:\PROGRA~1\QGIS33~1.3\apps\Python312\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed pip-25.1.1

C:\PROGRA~1\QGIS33~1.3\apps\Python312>python.exe -m pip install PyQtWebEngine
Collecting PyQtWebEngine
  Using cached PyQtWebEngine-5.15.7-cp38-abi3-win_amd64.whl.metadata (1.9 kB)
Requirement already satisfied: PyQt5-sip<13,>=12.13 in c:\progra~1\qgis33~1.3\apps\python312\lib\site-packages (from PyQtWebEngine) (12.13.0)
Collecting PyQtWebEngine-Qt5<5.16.0,>=5.15.0 (from PyQtWebEngine)
  Using cached PyQtWebEngine_Qt5-5.15.2-py3-none-win_amd64.whl.metadata (584 bytes)
Requirement already satisfied: PyQt5>=5.15.4 in c:\progra~1\qgis33~1.3\apps\python312\lib\site-packages (from PyQtWebEngine) (5.15.10)
Using cached PyQtWebEngine-5.15.7-cp38-abi3-win_amd64.whl (184 kB)
Using cached PyQtWebEngine_Qt5-5.15.2-py3-none-win_amd64.whl (60.0 MB)
Installing collected packages: PyQtWebEngine-Qt5, PyQtWebEngine
Successfully installed PyQtWebEngine-5.15.7 PyQtWebEngine-Qt5-5.15.2

C:\PROGRA~1\QGIS33~1.3\apps\Python312>