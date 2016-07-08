import csv
import petl as etl
from petl import boolparser
import os

def call():
    mybool = boolparser(true_strings=['true'], false_strings=['false'])
    input_filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data.csv' ))

    return (
        etl
        .fromcsv(input_filename)
    )

if __name__ == '__main__':
    etl.tocsv(call())
