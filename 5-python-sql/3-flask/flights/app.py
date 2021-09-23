from flask import Flask, render_template, request

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgresql://postgres:postgres@localhost:5432/flightsdb')
connection = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = connection.execute("SELECT f.id_flight, lo.name origin, ld.name destination, f.duration FROM flights f \
                                  INNER JOIN locations lo ON f.id_location_orig = lo.id_location \
                                  INNER JOIN locations ld ON f.id_location_dest = ld.id_location").fetchall()

    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
  nm_passenger = request.form.get("name_passenger") 

  try:
    id_flight = int(request.form.get("id_flight"))
  except ValueError: 
    return render_template("error.html", message="Voo inválido!!")


  connection.begin()

  try: 
    flight = connection.execute(text("SELECT * FROM flights WHERE id_flight = :id_flight"), {"id_flight": id_flight}).fetchone()

    if flight is None:
        connection.rollback()
        return render_template("error.html", message="Esse voo não existe!!")

    connection.execute(text("INSERT INTO passengers (name, id_flight) VALUES (:name, :id_flight)"), {"name": nm_passenger, "id_flight": id_flight})
    connection.commit()
    return render_template("success.html")

  except Exception as e:
    connection.rollback()
    return render_template("error.html", message=e)

@app.route("/flights/<int:id_flight>")
def flight(id_flight):
    flight = connection.execute(text("SELECT * FROM flights WHERE id_flight = :id_flight"), {"id_flight": id_flight}).fetchone()

    if flight is None:
        return render_template("error.html", message="Esse voo não existe!!")

    passengers_list  = connection.execute(text("SELECT name FROM passengers WHERE id_flight = :id_flight"), {"id_flight":id_flight}).fetchall()

    return render_template("flight.html", flight=flight, passengers_list=passengers_list)


if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
	  port=5000
	)