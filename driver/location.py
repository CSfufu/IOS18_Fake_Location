from pymobiledevice3.cli.developer import LocationSimulation


# lat(latittude)代表维度  lng(longitude)代表经度
def set_location(dvt, lat: float, lng: float):
    LocationSimulation(dvt).set(lat, lng)


def clear_location(dvt):
    LocationSimulation(dvt).clear()

