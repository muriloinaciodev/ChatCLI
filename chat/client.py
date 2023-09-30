from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich import box
from os import system
import threading
from time import sleep
import requests

c = Console()
p = Prompt()

#serverUrl = "http://localhost:5000"
serverUrl = input("Server URL: ").strip()
msgErro = "[red]Erro ao conectar ao servidor!\nVerifique sua conecção com a internet e a url do servidor e tente novamente.[/]"

def showMessages(msgObject: list):
    """
    receive a list of messages in format:
        {"username":"User", "msg":"message"}
    and print all messages formatted
    """
    for msg in msgObject:
        if msg['username'] == username:
            color = 'green'
        else:
            color = 'red'
        #c.print(f"<[{color}]{msg['username']}[/]> \n{msg['msg']}\n")
        c.print(Panel.fit(
            msg['msg'],
            title=f"<[{color}]{msg['username']}[/]>",
            title_align="left"
        ))

#INPUT USER LOGIN
username = p.ask("Username")
password = p.ask("Password", password=True)
try:
    loginVerify = requests.post(
        serverUrl+"/login", 
        json={"username":username, "password":password}
    ).text 
except:
    c.print(msgErro)
    exit()

match loginVerify:
    case "ls":
        c.print("[green]Login Sucess[/]")
    case "pw":
        c.print("[red]Password Wrong, Try again.[/]")
        exit()
    case "uu":
        c.print("[red]User Undefined[/]")
        if p.ask("Do you want to create it? ", choices=["yes", "no"], default="yes") == "yes":
            try:
                requests.post(
                    serverUrl+"/createUser",
                    json={"username":username, "password":password}
                )
            except:
                c.print(msgErro)
                exit()
            print("Login Sucess")
        else:
            exit()

while True:
    try: talk = requests.get(serverUrl+"/chat").json()
    except: c.print(msgErro); exit()

    system("clear")
    showMessages(talk)

    try:text = p.ask(f"<[green]{username}[/]>")
    except KeyboardInterrupt: print();exit()

    if len(text) == 0: continue

    try:
        requests.post(
            serverUrl+"/send", 
            json={"username":username, "msg":text}
        )
    except: c.print(msgErro); exit()

