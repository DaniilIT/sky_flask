from flask import Flask

import config
from blueprints.main.views import main_blueprint
from blueprints.loader.views import loader_blueprint
from blueprints.api.views import api_blueprint


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['JSON_AS_ASCII'] = False
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.register_blueprint(main_blueprint, url_prefix='/')
app.register_blueprint(loader_blueprint, url_prefix='/')
app.register_blueprint(api_blueprint, url_prefix='/')


@app.errorhandler(400)
def database_not_found(error):
    return ('<h1><center><font color="red">Error</font><br>'
           'Database not found.</center></h1><hr>')  # , 404

@app.errorhandler(404)
def page_not_found(error):
    return '<h1><center><font color="red">Error 404</font><br>' \
           'Something goes wrong! Page not found.</center></h1><hr>'  # , 404

    # return '<h1 style="color: red;">Error 404 :(</h1><p>Страница не найдена</p><p>{error}</p>', 404


@app.errorhandler(500)
def error500_page(error):
    return '<h1 style="color: red;">Error 500 :(</h1><p>Внутренняя ошибка сервера</p><p>{error}</p>', 500


if __name__ == '__main__':
    app.run(debug=config.DEBUG)
