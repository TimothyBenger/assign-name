from photo import Photo
from typing import List
from datetime import datetime

class Album:
    """Represents an album of photos"""
    def __init__(self, photos: List[Photo]) -> None:
        self.photos = photos
    
    def get_location(self) -> str:
        """Return the most common location of the photos in the album"""
        locations = [photo.get_location() for photo in self.photos]
        # one liner inspiration:
        # https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list
        return max(set(locations), key=locations.count)

    def get_time(self) -> str:
        """
        Return a description of the album time.
        1 day: "A day"
        2 - 3 days: "A couple of days"
        3 < days < 6: "A few days"
        6 <= days <= 9: "A week"
        > 9 days: "A spell"
        """
        times = sorted([photo.datetime_object for photo in self.photos])
        first_photo = times[0]
        last_photo = times[-1]
        delta = last_photo - first_photo
        # establish the number of days we were there
        # 0 days difference between first and last photo = 1 day there
        days_delta = delta.days + 1
        if days_delta == 1:
            return "A day"
        elif days_delta <= 3:
            return "A couple of days"
        elif days_delta < 6:
            return "A few days"
        elif days_delta <= 9:
            return "A week"
        else:
            return "A spell"
