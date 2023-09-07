from flask import Flask
from web.routes.SARoute import blueprint as SA_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    return app


app = create_app()
app.register_blueprint(SA_blueprint, url_prefix='/SA')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
