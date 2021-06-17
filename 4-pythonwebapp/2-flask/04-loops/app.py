from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	alunos = ["Nicole", "Duda", "Matheus", "Miguel"]
	
	return render_template("index.html", alunos=alunos)

if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
	  port=8000
	)
