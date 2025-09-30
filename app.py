from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Contact Page with Form
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # For now just print the details in terminal
        print(f"Message from {name} ({email}): {message}")
        return f"<h2>Thanks {name}, your message has been received!</h2>"

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
