from flask import Flask, render_template, request

app = Flask(__name__)

menu = [{"name": "Установка", "url": "install-flask"},
{"name": "Первое приложение", "url": "first-app"},
{"name": "Обратная связь", "url": "contact"}]
@app.route("/")
def index():
  return render_template('index.html', menu = menu)

@app.route("/about")
def about():
     return render_template('about.html', title="О сайте")
   
@app.route("/contacts", methods=["POST", "GET"])
def contacts():
  if request.method == 'POST':
    print(request.form)
  return render_template('contacts.html', title="Обратная связь", menu = menu)

if __name__ == "__main__":
    app.run(debug=True)