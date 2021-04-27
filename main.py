from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

with open('registrants.json') as f:
  REGISTRANTS = json.load(f)

SPORTS = [
  "Dodgeball",
  "Flag Football",
  "Soccer",
  "Volleyball",
  "Ultimate Frisbee",
  "Tennis"
]

@app.route("/")
def index():
  return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
  name = request.form.get("name")
  sport = request.form.get("sport")
  if not name:
    err = "Missing name."
    return render_template("failure.html", message=err)
  if sport not in SPORTS:
    err = "Invalid sport."
    return render_template("failure.html", message=err)
  
  REGISTRANTS[name] = sport

  with open('registrants.json', 'w') as f:
    json.dump(REGISTRANTS, f)

  return redirect("/registrants")

@app.route("/registrants")
def registrants():
  return render_template("registrants.html", registrants=REGISTRANTS)

@app.route("/registrants/<selected_sport>")
def show_sport_registrants(selected_sport):
  return render_template("sport.html", registrants=REGISTRANTS, sport=selected_sport)



if __name__ == "__main__":
  app.run("0.0.0.0")