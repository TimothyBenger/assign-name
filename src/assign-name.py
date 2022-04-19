#!venv/bin/python3

import argparse
from argparse import RawDescriptionHelpFormatter
from csv import reader
from photo import Photo
from album import Album

def main():

    args = handle_input_args()
    photos_file = args.photos_location
    
    # Parse the metadata
    photos = []
    with open(f"{photos_file}", 'r') as f:

        photos_metadata = reader(f)

        for photo_metadata in photos_metadata:
            photo = Photo(
                photo_metadata[0], # timestamp
                photo_metadata[1], # latitude
                photo_metadata[2], # longitude
            )
            photos.append(photo)
        
    album = Album(photos)
    album_location = album.get_location()
    album_time = album.get_time()
    print(f"{album_time} in {album_location}")


def handle_input_args():
    with open("src/help_text.txt", 'r') as f:
        description_text = f.read()
    # description_text = "Assign a name to a photo album"

    parser = argparse.ArgumentParser(
        description = description_text,
        formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument(
        "--photos_location",
        default=None,
        required=True,
        help='Pass the location of the CSV file containing photo metadata'
    )

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()