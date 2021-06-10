from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return "Meu Google Maps!!!!"


@app.route("/place/<string:address>")
def hello(address):
    print(address)
    return redirect(f"https://google.com/maps/place/{address}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
