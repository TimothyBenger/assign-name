import logging
from datetime import datetime
from geopy.geocoders import Nominatim

class Photo:
    """Represents a single photo"""
    def __init__(self, timestamp, latitude, longitude) -> None:

        # Time as both a string and a python datetime object
        self.timestamp = timestamp
        self.datetime_object = self._convert_time(self.timestamp)
        
        # Tuple to represent the geo-coordinates
        self.latitude = latitude
        self.longitude = longitude
        self.geocoordinate = (self.latitude, self.longitude)

    def get_location(self):
        """
        Return the city, or failing that, the country where the photo was taken
        """
        location_data = self.get_location_data()

        city = location_data['address'].get('city')
        
        if city is not None:
            return city
        else:
            country = location_data['address'].get('country')
            if country is not None:
                return country
            else:
                logging.warning(
                    'Could not get location data for a photo in this album.',
                    'Check geo-cordinates of all photos are valid')
                return
        
    
    def get_location_data(self):
        """
        Given the geo-coordinates of the place, return a location object.
        The object comes from the geopy library and provides metadata such
        as road name, city etc.
        """
        locator = Nominatim(user_agent="assign-name")
        coordinates = f"{self.latitude}, {self.longitude}"
        location = locator.reverse(coordinates)
        return location.raw
    
    def _convert_time(self, timestamp: str) -> datetime:
        """
        Converts a datetime string in either the format:
            YYYY-MM-DD hh:mm:ss
        ... or the format:
            YYY-MM-DDThh:mm:ssZ
        ... to a python datetime object
        """
        if "T" in timestamp:
            return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        try:
            return datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            logging.error(
                "Invalid time format specified. See help page for guidance."
            )
            return

    def __repr__(self) -> str:
        """
        Display the photo's attributes
        """
        return "<Photo(timestamp={}, location=({},{}))>"\
            .format(
                self.timestamp,
                self.latitude,
                self.longitude
            )