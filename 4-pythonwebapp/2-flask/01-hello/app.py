from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello, World!!"

@app.route("/jefferson")
def hello_jefferson():
	return "Hello, Jefferson!!"

if __name__ == "__main__":
	app.run(
		host="0.0.0.0",
	  port=8000
	)
  
