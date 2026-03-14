from flask import Flask, render_template, request, redirect
from queue_manager import QueueManager

app = Flask(__name__)

queue_manager = QueueManager()

@app.route("/")
def home():
    queue = queue_manager.get_queue()
    return render_template("index.html", queue=queue)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        queue_manager.add_patient(name)
        return redirect("/")
    return render_template("register.html")

@app.route("/next")
def next_patient():
    queue_manager.next_patient()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)