import os

from flask import Flask

from . import blockchain
from . import db

def create_app(test_config=None):
    """
        +====================+
        |   Create the app   |
        +====================+
    """
    app = Flask(__name__, instance_relative_config=True)

    """
        +====================+
        |   Config the app   |
        +====================+
    """
    # Default
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'bun_dau_coin.sqlite'),
        PORT="30000"
    )

    # Get/Apply user config
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    """
        +=========================+
        |   Check app necessary   |
        |    and create missing   |
        +=========================+
    """
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    # (re)create database
    db.init_app(app)


    """
        +=============+
        |   Routing   |
        +=============+
    """
    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, BSC!'

    @app.route('/fry')
    def fry():
        genesis = blockchain.genesisBlock()
        return str(genesis.timestamp) + " | " + genesis.data

    return app