from flask import Flask
from web.controller.SAController import sa_blueprint
from web.controller.SCAController import sca_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app


app = create_app()
app.register_blueprint(sa_blueprint)
app.register_blueprint(sca_blueprint)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
