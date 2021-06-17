from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
  nome = request.form.get("nome")  
  bairro = request.form.get("bairro")  	
  return render_template("hello.html", nome=nome, bairro=bairro)

if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
	  port=8000
	)