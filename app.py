from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

url_database = {}


def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None

    if request.method == "POST":
        original_url = request.form["url"]

        short_code = generate_short_code()
        url_database[short_code] = original_url

        short_url = request.host_url + short_code

    return render_template("index.html", short_url=short_url)


@app.route("/<short_code>")
def redirect_url(short_code):
    if short_code in url_database:
        return redirect(url_database[short_code])

    return "URL not found"


if __name__ == "__main__":
    app.run(debug=True)