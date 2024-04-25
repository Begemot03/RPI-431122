from flask import Flask, render_template, request, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

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
    if len(request.form['username']) > 2:
      flash('Сообщение отправлено', category='success')
    else:
      flash('Ошибка отправки', category='error')
  return render_template('contacts.html', title="Обратная связь", menu = menu)

if __name__ == "__main__":
    app.run(debug=True)