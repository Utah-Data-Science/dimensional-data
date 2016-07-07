import csv
from inflection import *
import petl as etl
from petl import boolparser
import os

def call():
    mybool = boolparser(true_strings=['true'], false_strings=['false'])
    input_filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'population.csv' ))

    return (
        etl
        .fromcsv(input_filename)
        .convert('City', titleize)
        .convert('Lat', float)
        .convert('Long', float)
        .convert('TaxReturnsFiled', int)
        .convert('EstimatedPopulation', int)
        .convert('TotalWages', int)
        .convert('Decommisioned', mybool)
        .cut('Zipcode', 'EstimatedPopulation')
    )

if __name__ == '__main__':
    etl.tocsv(call())
