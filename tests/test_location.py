from src.photo import Photo
from csv import reader

# We'll take the first line from TEST_INPUT as sample data; it will be:
# 2019-10-31T18:52:59Z,40.627883,14.366858
TEST_INPUT = 'sample_data/3.csv'

EXPECTED_OUTPUT = {
    'place_id': 15363820,
    'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
    'osm_type': 'node',
    'osm_id': 1729259909,
    'lat': '40.6278198',
    'lon': '14.3670577',
    'display_name': 'Nonna Emilia, Via Marina Grande, Sorrento, Napoli, Campania, 80067, Italia',
    'address': {
        'amenity': 'Nonna Emilia',
        'road': 'Via Marina Grande',
        'city': 'Sorrento',
        'county': 'Napoli',
        'ISO3166-2-lvl6': 'IT-NA',
        'state': 'Campania',
        'ISO3166-2-lvl4': 'IT-72',
        'postcode': '80067',
        'country': 'Italia',
        'country_code': 'it'
        },
    'boundingbox': [
        '40.6277698',
        '40.6278698',
        '14.3670077',
        '14.3671077'
        ]
    }

def test_location_data():
    photos = []
    with open(f"{TEST_INPUT}", 'r') as f:

        photos_metadata = reader(f)
        # take first photo from sample file
        sample_photo_data = [photo for photo in photos_metadata][0]
        sample_photo = Photo(
                sample_photo_data[0], # timestamp
                sample_photo_data[1], # latitude
                sample_photo_data[2], # longitude
            )
        assert sample_photo.get_location_data() == EXPECTED_OUTPUT