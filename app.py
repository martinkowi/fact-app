from flask import Flask, render_template
import random

app = Flask(__name__)

facts = [
	"Die Donau fließt durch 10 Länder",
	"Island hat keine Armee",
	"Die EU hat 24 Amtssprachen",
	"Der Vatikan ist der kleinste Staat der Welt",
	"Der Eifelturm wird im Sommer Größer"
]

@app.route("/")
def index():

	fact = random.choice(facts)

	return render_template("index.html", fact=fact)


@app.route("/facts")
def all_facts():
	return render_template("facts.html", facts=facts)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
