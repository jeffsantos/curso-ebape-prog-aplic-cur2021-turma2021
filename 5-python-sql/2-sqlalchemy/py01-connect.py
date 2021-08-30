from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:postgres@localhost:5432/secretariadb')

connection = engine.connect()


# lista = connection.execute("SELECT * FROM professores;").fetchall()

# for i in lista:
#     print(f"O professor(a) {i.nm_professor} mora no bairro {i.id_bairro}")


professores = connection.execute("SELECT * FROM professores p \
                                  INNER JOIN bairros b ON b.id_bairro = p.id_bairro ").fetchall()

for professor in professores:
    print(f"O professor(a) {professor.nm_professor} mora no bairro {professor.nm_bairro}")