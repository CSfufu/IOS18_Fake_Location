import config

from utils import location

def get_location():
    with open(config.config.LocationConfig) as myFile:
        loc = location.parse_loc(myFile.read())
    return loc  
