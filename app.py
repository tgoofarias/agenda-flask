from flask import Flask, render_template, request, redirect, url_for, session,jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "1234567"

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login-user", methods=["POST"])
def login_user():
    email, password = request.form["email"], request.form["password"]
    for user in get_users():
        if (user[1] == email and user[2] == password):
            session["user"] = user
            return redirect(url_for("agenda"))
    return redirect(url_for("index"))

@app.route("/register-page")
def register_page():
    return render_template("register.html")

@app.route("/register-user", methods=["POST"])
def register_user():
    name, email, password, password2 = request.form["name"], request.form["email"], request.form["password"], request.form["password2"]
    if "" in [name, email, password, password2]:
        return redirect(url_for("register_page"))
    if (password == password2):
        connection = sqlite3.connect("schedule.db")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO agenda_usuarios(name, email, password) VALUES ('{name}', '{email}', '{password}')")
        connection.commit()
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route("/agenda")
def agenda():
    return render_template("main-page.html")

@app.route("/user-page")
def user_page():
    return render_template("user-page.html", user=session["user"])

@app.route("/delete-user", methods=["POST"])
def delete_user():
    user = session["user"]
    connection = sqlite3.connect("schedule.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM agenda_usuarios WHERE email='{user[1]}'")
    connection.commit()
    return redirect(url_for("index"))

'''   EVENTOS  '''

@app.route("/add-event-page")
def add_event_page():
    return render_template("add-event-page.html")

@app.route("/add-event", methods=["POST"])
def add_event():
    titulo, descricao, data = request.form["titulo"], request.form["descricao"], request.form["data"]
    connection = sqlite3.connect("schedule.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO agenda_eventos(titulo, descricao, data) VALUES ('{titulo}', '{descricao}', '{data}');")
    connection.commit()
    return redirect(url_for("agenda"))

@app.route("/get-events/<ano>-<mes>-<dia>")
def get_events(ano, mes, dia):
    connection = sqlite3.connect("schedule.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM agenda_eventos WHERE data='{ano}-{mes}-{dia}';")
    results = cursor.fetchall()
    json = []
    for result in results:
        json.append({"titulo": result[0], "descricao": result[1], "data": result[2]})
    return jsonify(json)

def get_users():
    connection = sqlite3.connect("schedule.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM agenda_usuarios")
    all_data = cursor.fetchall()
    return all_data
