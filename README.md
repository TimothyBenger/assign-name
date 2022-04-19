## Installation

$ python3 -m venv venv
$ pip install -r requirements.txt
$ ./src/assign-name.py --photos_location <path/to/photos>

## Usage

```console
$ ./src/assign-name.py --photos_location sample_data/1.csv
A couple of days in New York
```

## Example Data

Example input:

Date                Latitude   Longitude
2019-03-30 14:12:19 40.703717 -74.016094
2019-03-30 15:34:49 40.782222 -73.965278
2019-03-31 12:18:04 40.748433 -73.985656

Example Output:

“A couple of days in New York”


## Tests

python -m pytest

## Roadmap

Test organisation needs to be improved as test file is cluttered. We could
achieve this through the use of a conftest file to generate our mock objects.

We're returning the city, or failing that the country, where the album of
photos were located. We need to think about whether simply using the country is
actually descriptive enough. We also need to account for geographically
distributed albums of photos, and in particular about how can we capture the
essence of the album in those cases.

We use the most commonly referenced location in the proposed album name. This
could mean potentially including photos from NZ in an album we're suggesting
calling 'a weekend in New York'. So we should consider using all the locations,
using some kind of composite location name, or curating the album further.

Test coverage for Photo.get_location, Album.get_location, Album.get_time

Runtime. The geopy library is quite slow, we could speed this up by using a
more robust API for the reverse geocoding.
