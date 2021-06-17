from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	msg = "Hello"
	return render_template("index.html", message=msg)


@app.route("/bye")
def bye():
	msg = "Bye, bye!!"
	return render_template("index.html", message=msg)



if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
	  port=8000
	)

