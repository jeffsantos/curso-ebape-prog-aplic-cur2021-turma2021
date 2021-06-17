from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
  agora = datetime.datetime.now()
  
  is_it_christmas = False

  if agora.month == 12 and agora.day == 25:
    is_it_christmas = True
		
  return render_template("index.html", is_it_christmas=is_it_christmas)

if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
	  port=8000
	)
