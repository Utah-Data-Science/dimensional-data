import csv
import petl as etl
import os

def call():
    input_filename = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'data.csv' ))

    return (
        etl
        .fromcsv(input_filename)
        .rename('intptlat', 'Latitude')
        .rename('intptlong', 'Longitude')
        .rename('zcta5', 'ZCTA')
        .convert('Latitude', float)
        .convert('Longitude', float)
    )

if __name__ == '__main__':
    etl.tocsv(call())
