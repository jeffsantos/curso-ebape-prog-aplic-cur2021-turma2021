from sqlalchemy import create_engine, text 
import sys

engine = create_engine('postgresql://postgres:postgres@localhost:5432/secretariadb')
connection = engine.connect()

bairro = " ".join(sys.argv[1:])

zona = input("Informe também a zona: ")

sql = text("SELECT * \
            FROM professores p \
            INNER JOIN bairros b ON b.id_bairro = p.id_bairro \
            WHERE b.nm_bairro = :pbairro AND b.zona = :pzona")


professores = connection.execute(sql, {"pbairro":bairro, "pzona":zona}).fetchall()

for professor in professores:
    print(f'{professor.nm_professor} mora no bairro {professor.nm_bairro}')