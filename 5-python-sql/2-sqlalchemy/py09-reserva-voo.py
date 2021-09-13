import os

from sqlalchemy import create_engine, text

#engine = create_engine('postgresql://postgres:postgres@localhost:5432/flightsdb')
engine = create_engine(os.getenv("DATABASE_URL"))
connection = engine.connect()

def main():


    # -----------------------
    # 1. Mostra a lista de voos cadastrados
    # -----------------------
    flights = connection.execute("SELECT f.id_flight, lo.name origin, ld.name destination, f.duration FROM flights f \
                                  INNER JOIN locations lo ON f.id_location_orig = lo.id_location \
                                  INNER JOIN locations ld ON f.id_location_dest = ld.id_location;").fetchall()

    for flight in flights:
        print(f"Flight {flight.id_flight}: {flight.origin} to {flight.destination} takes {flight.duration}")


    # -----------------------
    # 2. Pede para o usuário escolher um voo
    # 
    # Garante que apenas um voo válido pode ser escolhido
    # -----------------------
    try: 
        id_flight = int(input("\nEscolha um vôo: "))
    except ValueError: 
        print("Voo tem que ser um numero.")
        return

    flight = connection.execute(text("SELECT * FROM flights WHERE id_flight = :id_flight"), {"id_flight": id_flight}).fetchone()

    if flight is None:
        print("Vôo inválido")
        return

    # -----------------------
    # 3. Mostra todos os passageiros que não estão em nenhum voo
    # -----------------------
    print("\nPassageiros que não têm reservas:")
    passengers = connection.execute(text("SELECT * FROM passengers WHERE id_flight IS NULL")).fetchall()

    if len(passengers) == 0:
        print("Todos os passageiros já têm reservas.")  
        return

    for passenger in passengers:
        print(passenger.name)

    
    # -----------------------
    # 4. Pede para o usuário escolher um passageiro
    #
    # Nesse ponto do programa, o usuário já escolheu um voo e um passageiro
    #
    # O que aconteceria se digitasse um nome de passageiro que não existe? 
    # Como exercício, altere o programa para tratar nomes existentes e permitir 
    # que um nome existente possa ser digitado sem distinção de letras maiúsculas e
    # minúsculas
    # -----------------------
    nome_passageiro = input("\nEscolha um passageiro: ")


    # -----------------------
    # 5. Coloca o passageiro no voo escolhido
    # 
    # Isto é, atualiza o id_flight para o passageiro escolhido
    # -----------------------
    connection.execute(text("UPDATE passengers SET id_flight = :preencher1 WHERE name = :preencher2"), {"preencher1": id_flight, "preencher2": nome_passageiro})   

    print(f"Passageiro {nome_passageiro} inserido no voo {id_flight}") 
    

if __name__ == "__main__":
    main()