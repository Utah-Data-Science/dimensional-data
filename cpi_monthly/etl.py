import csv
import petl as etl
import os
from petl import dateparser

parsers={'date': dateparser('%Y-%m-%d')}

def call():
    input_filename = os.path.abspath(os.path.join(os.path.dirname(__file__),
        'data.csv' ))

    return (
        etl
        .fromcsv(input_filename)
        .convert('DATE', parsers)
        .convert('CPIAUCSL', float)
    )

if __name__ == '__main__':
    etl.tocsv(call())
