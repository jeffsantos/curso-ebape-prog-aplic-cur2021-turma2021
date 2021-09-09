import os

from sqlalchemy import create_engine, text

engine = create_engine(os.getenv("DATABASE_URL"))
connection = engine.connect()

def main():
    flights = connection.execute("SELECT f.id_flight, lo.name origin, ld.name destination, f.duration FROM flights f \
                                  INNER JOIN locations lo ON f.id_location_orig = lo.id_location \
                                  INNER JOIN locations ld ON f.id_location_dest = ld.id_location;").fetchall()
    for flight in flights:
        print(f"Flight {flight.id_flight}: {flight.origin} to {flight.destination} takes {flight.duration}")

    id_flight = int(input("\nEscolha um vôo: "))

    flight = connection.execute(text("SELECT * FROM flights WHERE id_flight = :id_flight"),
                         {"id_flight": id_flight}).fetchone()
    if flight is None:
        print("Vôo inválido")
        return

    passengers = connection.execute(text("SELECT * FROM passengers WHERE id_flight = :id_flight"),
                         {"id_flight": id_flight}).fetchall()

    print("\nPassageiros:")
    for passenger in passengers:
        print(passenger.name)

    if len(passengers) == 0:
        print("Nenhum passageiro nesse vôo.")
    

if __name__ == "__main__":
    main()