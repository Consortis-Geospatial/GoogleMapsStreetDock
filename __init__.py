from .main import GoogleMapsDockPlugin

def classFactory(iface):
    return GoogleMapsDockPlugin(iface)