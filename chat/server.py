from flask import Flask, jsonify, request
from json import load, dump
from rich.console import Console

c = Console()
app = Flask(__name__)

@app.route("/chat")
def chat():
    """Return all messages in JSON"""
    with open("../data/chat.json", "rt") as arq:
        allMsg = load(arq)
    return jsonify(allMsg)

@app.route("/send", methods=["POST", "GET"])
def send():
    with open("../data/chat.json", "rt") as arq:
        allMsg = load(arq)
    allMsg.append(request.get_json())
    with open("../data/chat.json", "wt") as arq:
        dump(allMsg, arq)
    c.print(f"Mensagem enviada em /send:\n\t[cyan]{request.get_json()}[/]")
    return "Success!"

@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Verify username and password in
    accounts.json and returns:
        ls = Login Sucess;
        pw = Password Wrong; 
        uu = Undefined User;
    """
    userData = request.get_json()
    username = userData["username"]
    password = userData["password"]
    c.print(f"Tentativa de login com as credenciais:\n\tUsername: [cyan]{username}[/]\n\tpassword: [cyan]{password}[/]")

    with open("../data/accounts.json", "rt") as arq:
        accounts = load(arq)

    for account in accounts:
        if (account["username"] == username):
            if (account["password"] == password):
                c.print("[green]ls - Login Success[/]")
                return "ls"
            c.print("[red]pw - Password Wrong[/]")
            return "pw"
    c.print("[dark_orange3]uu - Undefined User[/]")
    return "uu"

@app.route("/createUser", methods=["POST", "GET"])
def createUser():
    userData = request.get_json()
    with open("../data/accounts.json", "rt") as arq:
        accounts = load(arq)
    accounts.append(userData)
    with open("../data/accounts.json", "wt") as arq:
        dump(accounts, arq)

    c.print("User created")
    return "User created"



app.run()
