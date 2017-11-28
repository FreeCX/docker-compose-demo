from flask import Flask, render_template, redirect, request
from werkzeug.contrib.fixers import ProxyFix
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# загрузим конфиг из файла
app.config.from_object('config')

# нужно для корректной работы проброса через gunicorn и nginx
app.wsgi_app = ProxyFix(app.wsgi_app)

# создаём объект БД
db = SQLAlchemy(app)


# наша таблица в БД
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(16), nullable=False)
    text = db.Column(db.String(256))

    def __init__(self, user, text='<empty post>'):
        self.user = user
        self.text = text


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # получаем все посты
        posts = Post.query.all()
        # рендерим страницу
        return render_template('index.html', posts=posts)
    elif request.method == 'POST':
        # получаем данные со страницы
        user, text = request.form['user-name'], request.form['user-text']
        # создаём пост
        new_post = Post(user, text)
        # добавляем в БД
        db.session.add(new_post)
        db.session.commit()
        # редиректим на страницу с GET
        return redirect('/')
    else:
        # не будем поддерживать остальные методы
        return 'Noooooooo!', 402


if __name__ == '__main__':
    app.run()
