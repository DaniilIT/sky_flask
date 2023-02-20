from flask import Flask

from blueprints.main.views import main_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)


@app.errorhandler(404)  # можно вызвать `abort(413)`
def error404_page(error):
    return '<h1 style="color: red;">Error 404 :(</h1><p>Страница не найдена</p>', 404


@app.errorhandler(500)
def error500_page(error):
    return '<h1 style="color: red;">Error 500 :(</h1><p>Внутренняя ошибка сервера</p>', 500


if __name__ == '__main__':
    app.run(debug=True)
