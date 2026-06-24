print("Starting application...")

from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

print("Loading model...")

with open("india_population_model.pkl", "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        year = int(request.form["year"])
        result = model.predict([[year]])
        prediction = f"Predicted India population in {year}: {int(result[0]):,}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)