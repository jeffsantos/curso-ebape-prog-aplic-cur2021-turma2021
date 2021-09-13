from sqlalchemy import create_engine
import sys

engine = create_engine('postgresql://postgres:postgres@localhost:5432/secretariadb')
connection = engine.connect()

bairro = " ".join(sys.argv[1:])

print(bairro)

professores = connection.execute(f"SELECT * \
                                   FROM professores p \
                                   INNER JOIN bairros b ON b.id_bairro = p.id_bairro \
                                   WHERE nm_bairro = '{bairro}';").fetchall()

for professor in professores:
    print(f'{professor.nm_professor} mora no bairro {professor.nm_bairro}')