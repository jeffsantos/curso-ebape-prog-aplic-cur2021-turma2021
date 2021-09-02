from sqlalchemy import create_engine, text
import sys

def lista_professores(bairro, zona):

    engine = create_engine('postgresql://postgres:postgres@localhost:5432/secretariadb')
    connection = engine.connect()

    sql = text("SELECT * FROM professores p INNER JOIN bairros b ON b.id_bairro = p.id_bairro WHERE b.nm_bairro = :pbairro AND b.zona = :pzona")

    professores = connection.execute(sql, {"pbairro": bairro, "pzona": zona}).fetchall()

    for professor in professores:
        print(f'{professor.nm_professor} mora no bairro {professor.nm_bairro}')


lista_professores("Copacabana", "1' OR '1' = '1")