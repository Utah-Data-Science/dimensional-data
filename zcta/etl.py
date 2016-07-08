import csv
import petl as etl
import os

def call():
    input_filename = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'data.csv' ))

    return (
        etl
        .fromcsv(input_filename)
        .convert('ZIP', int)
        .convert('ZCTA', int)
    )

if __name__ == '__main__':
    etl.tocsv(call())
