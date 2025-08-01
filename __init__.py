from .main import GoogleMapsStreetDock

def classFactory(iface):
    return GoogleMapsStreetDock(iface)