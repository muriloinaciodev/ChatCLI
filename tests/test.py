import requests

url = "http://localhost:5000"
url = "https://1caa-45-235-158-78.ngrok-free.app/"

def testRouteChatFromServer():
    """Return list of message"""
    response = requests.get(url+"/chat")
    assert isinstance(response.json(), list)

def testRouteSendFromServer():
    """receive a dict with keys username and msg, and return sucess"""
    response = requests.post(url+"/send", json={"username":"Murilo","msg":"Teste"})
    assert response.text == "Success!"

def testRouteLoginFromServer_LoginSuccess():
    """Receive valid username and password and login is success"""
    response = requests.post(url+"/login", json={"username":"Murilo","password":"murilo11"})
    assert response.text == "ls"

def testRouteLoginFromServer_PasswordWrong():
    """Receive valid username but wrong password and login failed"""
    response = requests.post(url+"/login", json={"username":"Murilo","password":"batata"})
    assert response.text == "pw"

def testRouteCreateUserFromServer():
    """receive a dict with username and password and create an user in accounts.json. Return "User Created" on sucess"""
    response = requests.post(url+"/createUser", json={"username":"Teste","password":"Teste"})
    assert response.text == "User Created"



testRouteChatFromServer()
testRouteSendFromServer()
testRouteLoginFromServer_LoginSuccess()
testRouteLoginFromServer_PasswordWrong()
testRouteCreateUserFromServer()
