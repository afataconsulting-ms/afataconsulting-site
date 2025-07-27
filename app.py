from flask import Flask, render_template, request, flash
from services.messaging import send_teams_message 
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/send-message", methods=["POST"])
def send_message():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    send_teams_message(name, email, message)

    flash("Votre message a bien été envoyé sur Teams. Merci !", "success")
    return render_template("confirmation.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)


