from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates_folder')

register = lambda file : open(file, "a+").writelines(f"{request.form['username']} {request.form['password']}\n") or "usuario cadastrado"

login = lambda file : "SUCESSO" if (f"{request.form['username']}", f"{request.form['password']}") in [tuple (line.strip().split(" ")) for line in open (file, "r")] else "FRACASSO"

file = "Aplicação.txt"

reqresp_login = lambda : login (file) if request.method == 'POST' else render_template('login.html')

reqresp_register = lambda : register (file) if request.method == 'POST' else render_template('register.html')

app.add_url_rule('/login/', 'login', reqresp_login, methods=['GET', 'POST'])
app.add_url_rule('/register/', 'register', reqresp_register, methods=['GET', 'POST'])
app.run(host='0.0.0.0', port=8080)
