from sqlalchemy import create_engine, text
import sys
import csv
import os


def import_csv():

    engine = create_engine('postgresql://postgres:postgres@localhost:5432/flights2')
    connection = engine.connect()

    # Exemplo de caminho absoluto
    f = open("/workspace/5-python-sql/2-sqlalchemy/csv/flights.csv")

    reader = csv.reader(f)

    sql = text("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration )")

    for origin, destination, duration in reader:
     connection.execute(sql, {"origin": origin, "destination":destination, "duration": duration})

import_csv()
