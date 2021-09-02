from sqlalchemy import create_engine, text
import sys
import csv

def import_csv():

    #engine = create_engine('postgresql://postgres:postgres@localhost:5432/flights2')
    #connection = engine.connect()

    f = open("csv/flights.csv")

    reader = csv.reader(f)

    for origem, destino, duracao in reader:
        print(origem, destino, duracao)

    print(reader)

import_csv()






