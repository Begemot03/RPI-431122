from flask import Flask, render_template, request, g, flash, redirect, url_for, make_response, abort
import os
import sqlite3
from DBApi import DBApi
from LoginApi import LoginApi
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from admin.admin import admin

SECRET_KEY = 'fdgfh78@#5?>gfhf89dx,v06k'
MAX_CONTENT_LENGTH = 1024 * 1024

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)

app.config.from_object(__name__)    
app.config.update(dict(DATABASE=os.path.join(app.root_path,'flsite.db')))
app.register_blueprint(admin, url_prefix='/admin')
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    pr = db.relationship('Profiles', backref='users', uselist=False)

    def __repr__(self):
        return f"<users {self.id}>"

class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<profiles {self.id}>"

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

dbase = None

@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = DBApi(db)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/offer")
def offer():
    return render_template("pages/offer.html")

@app.route("/work")
def work():
    return render_template("pages/work.html")

@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return LoginApi().fromDB(user_id, dbase)

@app.route("/auth", methods=["POST", "GET"])
def auth():
    if request.method == "POST":
        hash = generate_password_hash(request.form['password'])
        res = dbase.addUser(request.form['name'], request.form['email'], hash)
        if res:
            flash("Вы успешно зарегистрированы", "success")
            return redirect(url_for('login'))

    return render_template("pages/auth.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    
    if request.method == "POST":
        user = dbase.getUserByEmail(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['password']):
            userlogin = LoginApi().create(user)
            rm = True if request.form.get('remainme') else False
            login_user(userlogin, remember=rm)

            return redirect(request.args.get("next") or url_for("profile"))

        flash("Неверная пара логин/пароль", "error")
    
    return render_template("pages/login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "success")
    return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
    return render_template("pages/profile.html")

@app.route('/userava')
@login_required
def userava():
    img = current_user.getAvatar(app)
    if not img:
        return ""

    h = make_response(img)
    h.headers['Content-Type'] = 'image/png'
    return h

@app.route('/upload', methods=["POST", "GET"])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and current_user.verifyExt(file.filename):
            try:
                img = file.read()
                res = dbase.updateUserAvatar(img, current_user.get_id())
                if not res:
                    flash("Ошибка обновления аватара", "error")
                flash("Аватар обновлен", "success")
            except FileNotFoundError as e:
                flash("Ошибка чтения файла", "error")
        else:
            flash("Ошибка обновления аватара", "error")

    return redirect(url_for('profile'))

@app.route("/stats")
def stats():
    return render_template('pages/stats.html', posts=dbase.getPostsAnonce())

@app.route("/add_post", methods=["POST", "GET"])
def addPost():
    if request.method == "POST":
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.addPost(request.form['name'], request.form['post'], request.form['url'])
            
            if not res:
                flash('Ошибка добавления статьи', category = 'error')
            else:
                flash('Статья добавлена успешно', category='success')
                print("статья добавлена")
        else:
            flash('Ошибка добавления статьи', category='error')
    return render_template('pages/add_post.html')


@app.route("/post/<alias>")
@login_required
def showPost(alias):
    db = get_db()
    dbase = DBApi(db)
    title, post = dbase.getPost(alias)
    if not title:
        abort(404)

    return render_template('pages/post.html', post=post)