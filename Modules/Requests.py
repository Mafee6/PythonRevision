import pip._vendor.requests as http
import pyperclip as clipboard
import json
# HTTP Requests in Python Yay! 
# bash$ pip install requests

PATH = "https://mafeepasswords.magee6.repl.co/api/password"

passwstrlen = input("Enter a password length: ")
passwlength = int(passwstrlen)

if (passwlength > 1001):
    print("Invalid Password Length.")
    quit()

req = http.get(PATH, params = {
    "length": passwlength if passwlength != None else 25
})

passw = "";
if req.status_code == 200:
    passw = json.loads(req.text)["password"]
    print("Take a password: " + str(passw))

    copy = bool(input("Do you want to copy the password to your clipboard?: "))
    if copy:
        clipboard.copy(passw)
elif req.status_code == 400:
    print("Invalid Request")
elif req.status_code == 512:
    print("Server Error")
else:
    print("Error while getting your password.")