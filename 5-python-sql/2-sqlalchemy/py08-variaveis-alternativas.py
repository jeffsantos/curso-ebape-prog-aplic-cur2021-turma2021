import os

from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres:postgres@localhost:5432/flightsdb')
#engine = create_engine(os.getenv("DATABASE_URL"))
connection = engine.connect()

def main():
    lista_voos = connection.execute("SELECT f.id_flight, lo.name origin, ld.name destination, f.duration FROM flights f \
                                  INNER JOIN locations lo ON f.id_location_orig = lo.id_location \
                                  INNER JOIN locations ld ON f.id_location_dest = ld.id_location;").fetchall()

    for item in lista_voos:
        print(f"Flight {item.id_flight}: {item.origin} to {item.destination} takes {item.duration}")

    try: 
        id_lido = int(input("\nEscolha um vôo: "))
    except ValueError: 
        print("Voo tem que ser um numero.")
        return

    item = connection.execute(text("SELECT * FROM flights WHERE id_flight = :preencher1"), {"preencher1": id_lido}).fetchone()  

    if item is None:
        print("Vôo inválido")
        return

    lista_passageiros = connection.execute(text("SELECT * FROM passengers WHERE id_flight = :preencher1"),
                         {"preencher1": id_lido}).fetchall()

    print("\nPassageiros:")
    for item in lista_passageiros:
        print(item.name)

    if len(lista_passageiros) == 0:
        print("Nenhum passageiro nesse vôo.")        


main()